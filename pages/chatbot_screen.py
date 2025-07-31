import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qwq import ChatQwQ
from working_logic import WorkLogic

st.set_page_config(layout="wide")

st.markdown(
    """
            <style>div[data-testid="InputInstructions"] > span:nth-child(1) {
    visibility: hidden;
}</style>
            """,
    unsafe_allow_html=True,
)

st.session_state.should_switch_page = False

if "video_id" not in st.session_state:
    st.session_state.video_id = None
if "worklogic" not in st.session_state:
    st.session_state.worklogic = None
if "youtube_url_value" not in st.session_state:
    st.session_state.youtube_url_value = ""


def clear_input():
    st.session_state.embedding_model_id = None
    st.session_state.openrouter_api = None
    st.session_state.model_id = None


def initiate_working_logic_class():
    try:
        worklogic = WorkLogic(
            embedding_model_id=st.session_state.embedding_model_id,
            llm_id=st.session_state.model_id,
            openrouter_api=st.session_state.openrouter_api,
        )
        if st.session_state.video_id is None:
            st.error("Video ID Does Not Exist")
        else:
            worklogic.video_setup(st.session_state.video_id)
            st.session_state.worklogic = worklogic
            return worklogic
    except Exception as e:
        st.error(f"Something Wnet Wrong During Initialization {e}")
        return None


st.sidebar.header("Menu")
placeHolder = st.empty()

with st.sidebar.form("API aNd Model Selection Form", clear_on_submit=False):
    embedding_model_id = (
        st.text_input(
            label="Enter HF Embedding Model ID",
            placeholder="HF Model For Local Use",
            key="embedding_model_id",
            label_visibility="hidden",
        ),
    )
    openrouter_api = (
        st.text_input(
            label="OpenRouter API",
            placeholder="OpenRouter API For LLM",
            key="openrouter_api",
            label_visibility="hidden",
        ),
    )
    model_id = (
        st.text_input(
            label="OpenRouter Model ID",
            placeholder="Paste OpenRouter Model ID",
            key="model_id",
            label_visibility="hidden",
        ),
    )
    submit, clear = st.columns(2, vertical_alignment="bottom", gap="small")
    with submit:
        st.form_submit_button(
            label="Submit", type="primary", on_click=initiate_working_logic_class
        )
    with clear:
        st.form_submit_button(label="Clear", on_click=clear_input)
if "youtube_url_value" in st.session_state and st.session_state.youtube_url_value:
    st.sidebar.video(st.session_state.youtube_url_value)

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("Hi, there"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        reasoning_expander = st.expander(label="🧠 Reasoning")

        message_placeholder = st.empty()

        reasoning_content = ""

        response_content = ""

        result = st.session_state.worklogic.ask_question(prompt)

        with reasoning_expander:
            reasoning_placeholder = st.empty()
            for chunk in result:
                if "reasoning_content" in chunk.additional_kwargs:
                    reasoning_content += chunk.additional_kwargs["reasoning_content"]
                    reasoning_placeholder.markdown(reasoning_content)
                response_content += chunk.content
                message_placeholder.markdown(response_content)
        st.session_state.messages.append(
            {"role": "assistant", "content": response_content}
        )
