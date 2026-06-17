# 🏦 FinSight AI: Bank Statement Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
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
- **User Interface** — Streamlit web application (`app.py`)
- **Evaluation Framework** — DeepEval integration for RAG quality testing

---
## ✨ UI Showcase
<img width="1868" height="935" alt="Opera Snapshot_2026-06-18_033226_localhost" src="https://github.com/user-attachments/assets/cbb9ecae-7d41-4fc5-850e-18753b89aea6" />
<img width="1868" height="935" alt="Opera Snapshot_2026-06-18_034253_localhost" src="https://github.com/user-attachments/assets/8e2648df-9799-4c90-a9d8-d1addc769ecc" />
<img width="1868" height="935" alt="Opera Snapshot_2026-06-18_034241_localhost" src="https://github.com/user-attachments/assets/b6af763c-2f2f-4e37-9f63-5dc5148d1b20" />
<img width="1864" height="497" alt="Opera Snapshot_2026-06-18_034332_localhost" src="https://github.com/user-attachments/assets/2337b005-bca4-48f5-b70f-969d87ddd078" />


## 🛠 Technology Stack

- **Document Processing**: YOLOv8 (custom layout model), PyMuPDF, pytesseract, pymupdf4llm
- **RAG & Vector Store**: LangChain, Chroma, Faiss
- **Agent Framework**: **AG2** (latest)
- **LLMs**: Google Gemini, Local models via Ollama
- **Frontend**: Streamlit
- **Analysis**: pandas, Plotly

---

## 📁 Repository Structure
```text
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
./scripts/build-python-virual-environment.sh
./scripts/activate_virual_environment.sh
./scripts/install-requirement.sh

# Install Tesseract OCR (Ubuntu/Debian)
./scripts/install-pytesseract-for-linux.sh
```

> **Note:** Create a `.env` file in the root directory and add your `GOOGLE_API_KEY` (for Gemini).

### 2. Run the Application

#### Streamlit Web UI

```bash
cd frontend/streamlit_app
streamlit run app.py
```

#### Development Notebooks

```bash
cd notebooks
jupyter notebook
```

---

## 🗺 Roadmap

 - Complete production-ready end-to-end pipeline
 - Advanced time-series forecasting for cash flow prediction
 - Multi-bank statement support with automatic categorization
 - Docker + API deployment
 - Rich interactive dashboard with more visualizations

------------------------------------------------------------------------

#### ⭐ Star this repo if you find it useful!
```
