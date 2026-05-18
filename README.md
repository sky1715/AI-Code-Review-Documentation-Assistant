# 🤖 AI Code Reviewer & Documentation Assistant

> An intelligent developer tool that reviews your Python code for bugs, generates documentation, and suggests refactors — powered by **Groq (Llama 3.3)**, **LangChain**, and **RAG (ChromaDB)**.


---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## 📖 About the Project

This is my **final year project** — a production-grade GenAI application that acts as an AI-powered code review assistant. It combines three advanced concepts:

- **Large Language Models (LLMs)** via Groq's free API for fast inference
- **Retrieval Augmented Generation (RAG)** using ChromaDB to give the AI context from your own codebase
- **Prompt Engineering** with structured output templates for consistent, useful reviews

Instead of sending just your code to an LLM, the app first searches your indexed codebase for relevant context, then sends both to Groq — making the review context-aware and far more accurate.

---

## ✨ Features

- 🐛 **Bug Detection** — Identifies bugs, logical errors, and security issues with severity ratings
- 📝 **Documentation Generator** — Auto-generates Google-style docstrings for all functions and classes
- 🔄 **Code Refactor** — Suggests cleaner, more Pythonic rewrites
- 💬 **Chat Interface** — Ask questions about your code in natural language
- 🧠 **RAG Pipeline** — Indexes your codebase so the AI understands project-wide context
- 🚀 **Deployed Live** — Publicly accessible on Hugging Face Spaces

---

## 🏗 Architecture

```
User Input (Streamlit UI)
        │
        ▼
  RAG Pipeline
  ┌─────────────────────────────────┐
  │  HuggingFace Embeddings         │
  │       ↓                         │
  │  ChromaDB Vector Store          │
  │       ↓                         │
  │  LangChain Retriever            │
  │  (Top 3 relevant code chunks)   │
  └─────────────────────────────────┘
        │
        ▼
  Groq LLM (Llama 3.3 70B)
  + Structured Prompt Templates
        │
        ▼
  Output: Bug Report / Docstrings / Refactored Code
```

**Two-phase RAG:**
1. **Indexing** (once) — Your `.py` files are chunked, embedded, and stored in ChromaDB
2. **Querying** (every request) — User code is embedded, similar chunks retrieved, both sent to LLM

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| LLM | Groq — Llama 3.3 70B | Fast, free inference |
| Orchestration | LangChain | RAG pipeline & chains |
| Vector DB | ChromaDB | Store & search embeddings |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` | Convert code to vectors |
| UI | Streamlit | Web interface |
| Secrets | python-dotenv | Safe API key management |
| Deployment | Hugging Face Spaces | Public live demo |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A free [Groq API key](https://console.groq.com) (no credit card needed)
- Git

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up your API key**

Create a `.env` file in the project root:
```
GROQ_API_KEY=your-groq-api-key-here
```

Get your free key at [console.groq.com](https://console.groq.com).

**5. Index your codebase**
```bash
python -m ingest.indexer
```

This reads all `.py` files in `sample_code/`, embeds them, and stores them in ChromaDB. Run this once (or whenever you update your codebase).

**6. Launch the app**
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📁 Project Structure

```
ai-code-reviewer/
│
├── app.py                  # Streamlit UI — main entry point
├── requirements.txt        # All dependencies
├── .env                    # API keys (not committed to Git)
├── .gitignore
│
├── core/
│   ├── llm.py              # Groq client setup
│   ├── prompts.py          # All prompt templates (system + user)
│   ├── reviewer.py         # Core logic: review, docstring, refactor
│   └── rag.py              # ChromaDB retriever
│
├── ingest/
│   └── indexer.py          # Reads .py files, embeds, stores in ChromaDB
│
├── sample_code/            # Example codebase to index
│   ├── utils.py
│   └── database.py
│
└── chroma_db/              # Auto-generated vector store (not committed)
```

---

## 💻 Usage

### Code Review
1. Paste your Python code into the **Code Review** tab
2. Click **Review Code**
3. Get a structured report: `BUGS`, `IMPROVEMENTS`, `SEVERITY`

### Generate Documentation
1. Paste your code into the **Generate Docs** tab
2. Click **Generate Docstrings**
3. Get your code back with full Google-style docstrings added

### Refactor Code
1. Paste your code into the **Refactor** tab
2. Click **Refactor**
3. Get a cleaner, more Pythonic version

### Example — Input
```python
def calculate(x, y, op):
    if op == 'add':
        return x + y
    if op == 'divide':
        return x / y
```

### Example — Output
```
BUGS:
- Division by zero when y=0 and op='divide' (no guard check)

IMPROVEMENTS:
- Add an else clause or raise ValueError for unsupported operations
- Use a dictionary dispatch pattern instead of repeated if statements

SEVERITY: Medium
```

---

## ☁️ Deployment

The app is deployed on **Hugging Face Spaces** and publicly accessible at:

🔗 **[Live Demo →](https://ai-code-review-documentation-assistant-dnfyspivrjqjdxs8btznji.streamlit.app/)**



---

## 📚 What I Learned

Building this project taught me end-to-end GenAI application development:

- **Prompt Engineering** — how system vs user prompts shape LLM behaviour, structured output formatting, and temperature tuning for code tasks
- **RAG Architecture** — how embeddings work, why vector similarity search enables context-aware AI, and how LangChain orchestrates the full retrieval pipeline
- **Production Python habits** — virtual environments, `.env` for secrets, modular folder structure, error handling with try/except, and logging
- **LLM API integration** — working with Groq's OpenAI-compatible API, managing tokens and rate limits
- **Streamlit** — building interactive Python web apps without HTML/CSS
- **Cloud deployment** — packaging an AI app and deploying it with environment secrets on Hugging Face Spaces

---

## 🔮 Future Improvements

- [ ] GitHub integration — review PRs directly via GitHub API
- [ ] Multi-language support — extend beyond Python to JavaScript, Java
- [ ] Security scanner — dedicated OWASP vulnerability detection prompt
- [ ] CI/CD plugin — integrate as a pre-commit hook or GitHub Action
- [ ] Chat memory — persist conversation history across sessions
- [ ] Upload entire repos — zip file upload and bulk indexing

---

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/sky1715)
- LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/suraj-kumar1619/)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> Built as a final year project to demonstrate production-grade GenAI development with LLMs, RAG, and prompt engineering.

