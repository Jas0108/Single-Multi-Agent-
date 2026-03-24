# AI STEM Tutor

A multi-agent AI tutoring system for STEM subjects using local Ollama models.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ollama installed locally
- Mistral model downloaded

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ai-tutor
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup Ollama**
```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Download Mistral model
ollama pull mistral

# Start Ollama server
ollama serve
```

5. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

### Usage

#### Single Agent
```bash
python main.py
```

#### Multi-Agent System
```bash
python main_multi.py
```

## 🏗️ Architecture

- **Single Agent**: General STEM tutor
- **Multi-Agent**: Subject-specific tutors (Math, Physics, Chemistry)
- **Supervisor**: Routes queries to appropriate agents

## 📦 Dependencies

- `langchain` - Core framework
- `langgraph` - Multi-agent orchestration
- `langchain-community` - Community integrations
- `langchain-ollama` - Ollama integration

## 🔧 Configuration

Edit `.env` file to customize:
- Model selection
- Base URL
- Logging settings

## 📄 License

[Your License Here]

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Submit pull request

## ⚠️ Important Notes

- Requires Ollama to be running locally
- Mistral model must be downloaded
- Default port: 11434
