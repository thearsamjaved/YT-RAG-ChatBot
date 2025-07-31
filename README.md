# 🎥 YouTube RAG Chatbot

An intelligent conversational AI system that enables you to chat with YouTube videos using advanced RAG (Retrieval-Augmented Generation) technology. Ask questions about video content and get contextually accurate answers with transparent AI reasoning.

![YouTube RAG Chatbot](https://img.shields.io/badge/AI-Powered-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-121212?logo=chainlink&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

## ✨ Features

### 🚀 Core Capabilities
- **Intelligent Video Analysis**: Extract and analyze YouTube video transcripts using advanced NLP
- **RAG-Powered Conversations**: Ask questions and get contextually accurate answers based on video content
- **Multi-Query Retrieval**: Enhanced context gathering through sophisticated retrieval strategies
- **Streaming Responses**: Real-time response generation with live updates
- **Transparent AI Reasoning**: Expandable reasoning sections showing the AI's thought process
- **Conversation Memory**: Maintains context across multiple questions in a session

### 🎨 User Experience
- **Intuitive Interface**: Clean, two-step workflow (URL input → Chat interface)
- **Real-Time Video Preview**: Embedded video player in the chat interface
- **Responsive Design**: Optimized for various screen sizes
- **Error Handling**: Comprehensive validation and user feedback
- **Session Persistence**: Chat history maintained throughout the session

### 🔧 Technical Features
- **Modular Architecture**: Clean separation of concerns with maintainable code
- **FAISS Vector Store**: Efficient similarity search with optimized text chunking
- **HuggingFace Integration**: Support for various embedding models
- **OpenRouter API**: Flexible LLM provider integration
- **Multi-Format URL Support**: Handles various YouTube URL formats

## 🛠️ Installation

### Prerequisites
- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Quick Start with uv (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd youtube-chatbot-rag
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run the application**
   ```bash
   uv run streamlit run youtube_chatbot.py
   ```

### Alternative Installation with pip

1. **Clone and navigate**
   ```bash
   git clone <repository-url>
   cd youtube-chatbot-rag
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run youtube_chatbot.py
   ```

## 📖 Usage Guide

### Step 1: Configure Your Setup
1. **Get API Keys**:
   - OpenRouter API key from [OpenRouter](https://openrouter.ai/)
   - Choose your preferred LLM model (e.g., `deepseek/deepseek-r1`)

2. **Select Embedding Model**:
   - HuggingFace model (e.g., `intfloat/e5-small-v2`)
   - Or any compatible sentence transformer model

### Step 2: Start Chatting
1. **Enter YouTube URL**: Paste any YouTube video URL in the input field
2. **Configure Models**: Use the sidebar to input your API keys and model preferences
3. **Submit Configuration**: Click "Submit" to initialize the RAG system
4. **Start Conversation**: Ask questions about the video content

### Step 3: Explore Features
- **View Reasoning**: Click the "🧠 Reasoning" expander to see AI's thought process
- **Watch Video**: Use the embedded player to reference specific parts
- **Continue Conversation**: Ask follow-up questions with maintained context

## 📁 Project Structure

```
youtube-chatbot-rag/
├── youtube_chatbot.py          # Main entry point and URL processing
├── pages/
│   └── chatbot_screen.py       # Chat interface and streaming responses
├── working_logic.py            # RAG pipeline and core processing
├── pyproject.toml             # Project dependencies and configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables (Optional)
Create a `.env` file for default configurations:

```env
OPENROUTER_API_KEY=your_api_key_here
DEFAULT_EMBEDDING_MODEL=intfloat/e5-small-v2
DEFAULT_LLM_MODEL=deepseek/deepseek-r1
```

### Model Recommendations

**Fast & Efficient Setup**:
- Embedding: `all-MiniLM-L6-v2` (384 dimensions, very fast)
- LLM: `deepseek/deepseek-r1` (good balance of speed and quality)

**High Quality Setup**:
- Embedding: `intfloat/e5-large-v2` (1024 dimensions, better accuracy)
- LLM: `anthropic/claude-3-sonnet` (superior reasoning capabilities)

## ⚠️ Limitations

### Current Limitations
- **Language Support**: Currently optimized for English transcripts
- **Video Length**: Very long videos (>3 hours) may face processing constraints
- **Real-time Content**: Cannot access live streams or premieres
- **API Dependencies**: Requires stable internet connection for transcript fetching
- **Memory Constraints**: Large transcripts may require significant RAM
- **Session-based**: Conversation history doesn't persist across browser sessions

### Known Issues
- Some YouTube videos may not have available transcripts
- Rate limiting may occur with high-frequency API calls
- Regional restrictions may affect transcript availability

## 🚀 Future Roadmap

### 🤖 Agentic Capabilities
- **Intelligent Retriever Reuse**: Smart caching and reuse of vector stores across sessions
- **Multi-Document Analysis**: Compare and analyze multiple videos simultaneously
- **Automatic Summarization**: Generate comprehensive summaries of entire transcripts
- **Context-Aware Follow-ups**: Proactive question suggestions based on video content

### 🌐 Enhanced Integration
- **Internet Search Integration**: Supplement video content with real-time web information
- **Note-Taking System**: Save important insights and create shareable notes
- **Bookmark Management**: Mark and organize important video segments
- **Export Capabilities**: Generate reports, summaries, and analysis documents

### 🧠 Advanced AI Features
- **Multi-Modal Analysis**: Support for video frames and visual content analysis
- **Sentiment Analysis**: Understand emotional context and tone
- **Topic Modeling**: Automatic categorization and theme extraction
- **Personalized Recommendations**: Suggest related content based on interests

### 🔧 Technical Enhancements
- **Database Integration**: Persistent storage for conversations and analysis
- **User Authentication**: Personal accounts with saved preferences
- **API Rate Limiting**: Smart request management and caching
- **Performance Optimization**: Faster processing and reduced latency
- **Mobile Optimization**: Responsive design for mobile devices

### 🎯 Specialized Features
- **Educational Mode**: Structured learning paths and quiz generation
- **Research Assistant**: Academic citation and reference generation
- **Content Creation**: Help create summaries, articles, and presentations
- **Multi-Language Support**: Transcript processing in multiple languages

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Implement your feature or fix
4. **Add tests**: Ensure your changes are well-tested
5. **Commit changes**: `git commit -m 'Add amazing feature'`
6. **Push to branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**: Describe your changes and improvements

### Development Setup
```bash
# Install development dependencies
uv sync --dev

# Run code formatting
black .
isort .

# Run type checking
mypy .

# Run tests
pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain** for providing the RAG framework
- **Streamlit** for the intuitive web application framework
- **OpenRouter** for API access to various LLMs
- **HuggingFace** for embedding models and transformers
- **YouTube Transcript API** for transcript extraction capabilities

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/youtube-chatbot-rag/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/youtube-chatbot-rag/discussions)
- **Documentation**: Check the [Wiki](https://github.com/yourusername/youtube-chatbot-rag/wiki) for detailed guides

---

**Made with ❤️ and AI** - Transform how you interact with video content through intelligent conversations!