# 🎥 YouTube RAG Chatbot

An intelligent conversational AI system that enables you to chat with YouTube videos using advanced RAG (Retrieval-Augmented Generation) technology. Ask questions about video content and get contextually accurate answers based on the video's transcript.

## ✨ Features

### 🚀 Core Capabilities
- **YouTube Video Analysis**: Extract and analyze transcripts from any YouTube video
- **RAG-Powered Q&A**: Ask questions and get accurate answers based on the video content
- **Multi-Query Retrieval**: Enhanced context gathering using sophisticated retrieval strategies with FAISS vector storage
- **Streaming Responses**: Real-time answer generation with live streaming updates
- **Conversation Memory**: Maintains context across multiple questions in your chat session
- **Reasoning Transparency**: Expandable reasoning sections showing the AI's thought process

### 🎨 User Experience
- **Simple Two-Step Workflow**: Enter YouTube URL → Start chatting
- **Embedded Video Player**: Watch the video directly in the chat interface
- **Clean Interface**: Streamlit-powered web application with intuitive design
- **Real-Time Processing**: See responses generated live as the AI processes your questions
- **Session Persistence**: Chat history maintained throughout your session

### 🔧 Technical Architecture
- **FAISS Vector Store**: Efficient similarity search with optimized text chunking
- **HuggingFace Embeddings**: Local embedding models for privacy and speed
- **OpenRouter Integration**: Access to various state-of-the-art language models
- **LangChain Framework**: Robust RAG pipeline with multi-query retrieval
- **Modular Design**: Clean, maintainable codebase with separated concerns

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)
- OpenRouter API key

### Quick Start with uv

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd youtube-chatbot-rag
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```

3. **Run the application**
   ```bash
   uv run streamlit run youtube_chatbot.py
   ```

The application will open in your default browser at `http://localhost:8501`

### Alternative Installation with pip

If you prefer using pip:

```bash
# Clone the repository
git clone <your-repository-url>
cd youtube-chatbot-rag

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Run the application
streamlit run youtube_chatbot.py
```

## 📖 Usage Guide

### Step 1: Get Your API Key
1. Sign up at [OpenRouter](https://openrouter.ai/)
2. Get your API key from the dashboard
3. Choose your preferred model (recommended: `deepseek/deepseek-r1` for good balance of speed and quality)

### Step 2: Configure the Application
1. **Enter YouTube URL**: Paste any YouTube video URL and click "Search"
2. **Configure Models in Sidebar**:
   - **HuggingFace Embedding Model**: `intfloat/e5-small-v2` (recommended) or any sentence-transformer model
   - **OpenRouter API Key**: Your API key from step 1
   - **OpenRouter Model**: Choose from available models (e.g., `deepseek/deepseek-r1`)
3. **Click Submit**: Initialize the RAG system

### Step 3: Start Chatting
- Ask questions about the video content
- View the embedded video player for reference
- Expand the "🧠 Reasoning" section to see the AI's thought process
- Continue the conversation - the system remembers context

### Recommended Model Combinations

**Fast & Efficient Setup**:
- Embedding: `intfloat/e5-small-v2`
- LLM: `deepseek/deepseek-r1`

**High Quality Setup**:
- Embedding: `intfloat/e5-large-v2`
- LLM: `anthropic/claude-3.5-sonnet`

## 📸 Screenshots

### Main Interface
*[Placeholder for main URL input interface screenshot]*

### Chat Interface
*[Placeholder for chat interface with embedded video player]*

### Reasoning View
*[Placeholder for expanded reasoning section screenshot]*

## 🎨 UI & Design

The current UI is built with Streamlit's default components and styling. While functional, I acknowledge the design could be more polished. **If you have CSS/frontend skills and would like to contribute UI improvements, I'd love to incorporate your changes!** Feel free to:

- Enhance the visual design and styling
- Improve the layout and user experience
- Add custom CSS for better aesthetics
- Suggest better component arrangements

Just submit your improvements and I'll review and merge them. The focus has been on functionality first, but a better UI would definitely enhance the user experience.

## ⚠️ Current Limitations

- **Language Support**: Currently supports English transcripts only
- **Local Models Only**: Uses local HuggingFace embedding models (no API-based embeddings)
- **Transcript Dependency**: Requires videos to have available transcripts
- **Session-Based**: Conversation history doesn't persist across browser sessions
- **Single Video**: Can only chat with one video at a time per session

## 🚀 Future Roadmap

I'm excited about expanding this project with several advanced features:

### 🎯 Video Timestamp Integration
- **Smart Navigation**: When you ask about specific topics, the video player will automatically jump to relevant timestamps
- **Context-Aware Playback**: Highlight and play video segments that directly relate to your questions
- **Visual Cues**: Show timestamp markers for discussed topics

### 📝 Note-Taking & Productivity Integration
- **Automatic Note Generation**: Create structured notes from your conversations
- **Export Capabilities**: Save insights to Notion, Obsidian, or other note-taking apps
- **Bookmark System**: Mark and organize important video segments and insights
- **Summary Generation**: Automatically create comprehensive video summaries

### 🌐 Enhanced AI Capabilities
- **Internet Search Integration**: Supplement video content with real-time web information for comprehensive answers
- **Deep Search**: Advanced research capabilities that can cross-reference multiple sources
- **Multi-Video Analysis**: Compare and analyze content across multiple videos simultaneously
- **Content Suggestions**: Recommend related videos and topics based on your interests

### 🔧 Technical Enhancements
- **Multi-Language Support**: Expand beyond English to support global content
- **Database Integration**: Persistent storage for conversations and insights
- **Advanced Retrieval**: Implement more sophisticated RAG techniques for better accuracy
- **Performance Optimization**: Faster processing and improved response times

### 🎓 Specialized Features
- **Educational Mode**: Generate quizzes, study guides, and learning paths from video content
- **Research Assistant**: Academic citation generation and reference management
- **Content Creation Tools**: Help create articles, presentations, and summaries based on video insights

## 🤝 Contributing

Contributions are welcome! Whether it's:
- UI/UX improvements
- Bug fixes
- New features
- Documentation enhancements
- Performance optimizations

Feel free to open issues or submit pull requests.

## 📄 License

This project is open source and available under the MIT License.

---

**Built with Python, Streamlit, LangChain, and AI** 🤖

Transform how you learn from and interact with video content through intelligent conversations!
