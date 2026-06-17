# 🏦 FinSight AI: Bank Statement Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![AG2](https://img.shields.io/badge/Agent_Framework-AG2-green)](https://github.com/ag2ai/ag2)

**Automated extraction, structuring, RAG-powered querying, and AI-agent financial analysis of bank statement PDFs.**

This project converts unstructured bank statement PDFs into structured data using computer vision (YOLO), OCR, and Large Language Models. It supports natural language queries and generates insightful monthly/yearly financial reports.

---

## ✨ Key Features

- **Advanced Document Parsing** — Custom YOLOv8 layout detection + OCR + LLM table extraction
- **RAG Pipeline** — Powerful retrieval-augmented generation with vector databases
- **Autonomous AI Agents** — Built with **AG2** (migrated from pyautogen in Feb 2026)
- **Financial Intelligence** — Income/expense categorization, trend analysis, monthly & yearly summaries
- **Multimodal & Local LLM Support** — Works with Gemini, Ollama (Llama 3, Gemma 2, etc.)
- **User Interface** — Streamlit web application (`apps.py`)
- **Evaluation Framework** — DeepEval integration for RAG quality testing

---

## 🛠 Technology Stack

- **Document Processing**: YOLOv8 (custom layout model), PyMuPDF, pytesseract, pymupdf4llm
- **RAG & Vector Store**: LangChain, Chroma, Faiss
- **Agent Framework**: **AG2** (latest)
- **LLMs**: Google Gemini, Local models via Ollama
- **Frontend**: Streamlit
- **Analysis**: pandas, Plotly


---

## 📁 Repository Structure
```
AI-Bank-Statement-Document-Automation/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── logging.py
│   │   ├── models/
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── document_processor.py      # YOLO + OCR + LLM extraction
│   │   │   ├── rag_service.py
│   │   │   ├── agent_service.py           # CrewAI + LangGraph + deepagents
│   │   │   └── financial_service.py
│   │   ├── utils/
│   │   │   ├── pdf_utils.py
│   │   │   └── embedding_utils.py
│   │   └── main.py
│   ├── tests/
│   └── pyproject.toml
├── frontend/
│   └── streamlit_app/
│       ├── pages/
│       ├── components/
│       └── app.py
├── notebooks/
│   ├── ai_agent_dev.ipynb
│   ├── ai_bank_statement_dev.ipynb
│   ├── RAG_algorithm_test.ipynb
│   ├── multimodal-rag-test.ipynb
│   └── pii_detection.ipynb
├── data/
│   ├── uploads/                    # Uploaded bank statements
│   ├── processed/                  # Extracted structured data
│   └── vector_stores/              # chroma_db, faiss_index
├── docker/
│   └── docker-compose.yml
├── scripts/
│   ├── setup.sh
│   └── download_models.sh
├── docs/
├── .env.example
├── .gitignore
├── README.md
└── pyproject.toml
```


---

## 🚀 Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/shivamparmar07/finsight.git
cd finsight

# Setup virtual environment and install dependencies
./src/build-python-virual-environment.sh
./src/activate_virual_environment.sh
./src/install-requirement.sh

# Install Tesseract OCR (Ubuntu/Debian)
./src/install-pytesseract-for-linux.sh
```

## Create a .env file and add your GOOGLE_API_KEY (for Gemini).

### 2. Run the Application
#### Development Notebooks

```bash
cd src/dev
jupyter notebook
```

#### Streamlit Web UI

```bash
cd src
streamlit run apps.py
```


## 🗺 Roadmap

 - Complete production-ready end-to-end pipeline
 - Advanced time-series forecasting for cash flow prediction
 - Multi-bank statement support with automatic categorization
 - Docker + API deployment
 - Rich interactive dashboard with more visualizations

------------------------------------------------------------------------

## 📄 License
### This project is licensed under the Apache License 2.0.

-------------------------------------------------------------------------

#### ⭐ Star this repo if you find it useful!


