from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import FetchedTranscript
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.vectorstores.base import VectorStoreRetriever
from langchain_qwq import ChatQwen


class WorkLogic:
    def __init__(
        self,
        embedding_model_id,
        openrouter_api,
        llm_id,
    ):
        self.embedding_model_id = embedding_model_id
        self.openrouter_api = openrouter_api
        self.llm_id = llm_id
        # Initialize models once
        self.embedding_model = HuggingFaceEmbeddings(model_name=self.embedding_model_id)
        self.llm_model = ChatQwen(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.openrouter_api,
            model=self.llm_id,
            streaming=True,
        )
        self.messages = [
            (
                "system",
                """You are an assistant for answering questions about a YouTube video. Use the following retrieved context from the video transcript to answer the question. If you don't know the answer from the context provided, just say that you don't know. Don't try to make up an answer.""",
            )
        ]
        self.retriever = None
        self.rag_chain = None

    def video_setup(self, video_id: str):
        try:
            transcript = self._extract_transcript(video_id)
            if not transcript:
                print("Failed To Retrieve A Transcript")
                return False
            documets = self._split_text(transcript)
            if not documets:
                print("Failed To Split Into Documents")
            vector_store = FAISS.from_documents(
                documents=documets, embedding=self.embedding_model
            )
            self.retriever = MultiQueryRetriever.from_llm(
                retriever=vector_store.as_retriever(search_kwargs={"k": 4}),
                llm=self.llm_model,
            )
            self.create_rag_chain()
            print("Successfuly Created The RAG Chain")
            return True
        except Exception as e:
            print(f"An error occounred in videosetup function: {e}")
            self.retriever = None
            self.rag_chain = None
            return False

    def _extract_transcript(self, video_id) -> str | None:
        """Extract transcript once and cache result"""
        try:
            yt_api = YouTubeTranscriptApi()
            transcript = yt_api.fetch(video_id=video_id, languages=["en"])
            return "".join(snippet.text for snippet in transcript)
        except Exception as e:
            print(f"Error extracting transcript: {e}")
            return None

    def _split_text(self, transcript: str) -> list[Document] | None:
        """Split text using cached transcript"""
        if not transcript:
            return None

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=200,
            separators=[" "],  # Fixed: should be list, not string
        )

        try:
            return splitter.create_documents([transcript])
        except Exception as e:
            print(f"Error splitting documents: {e}")
            return None

    def add_question_to_memory(self, inputs):
        question = inputs["question"]
        context = inputs["context"]
        self.messages.append(("human", f"Question: {question} \n\n Context:{context}"))
        return inputs

    def add_response_to_memory(self, answer):
        self.messages.append(("ai", f"Answer:{answer.content}"))
        return answer

    def create_rag_chain(self):
        prompt = ChatPromptTemplate(
            self.messages + [("human", "Question: {question} \n\n Context:{context}")]
        )

        self.rag_chain = (
            {
                "context": self.retriever
                | RunnableLambda(lambda docs: [doc.page_content for doc in docs]),
                "question": RunnablePassthrough(),
            }
            | RunnableLambda(self.add_question_to_memory)
            | prompt
            | self.llm_model
            # | RunnableLambda(self.add_response_to_memory)
        )

    def ask_question(self, question: str):
        if not self.rag_chain:
            return "Error System is not initialized please provide a url first."
        return self.rag_chain.stream(question)
