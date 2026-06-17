# pyrefly: ignore [missing-import]
import streamlit as st
import os
import pandas as pd
import plotly.express as px
import tempfile
import json
import pymupdf4llm
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Bank Statement Analyzer", page_icon="🏦", layout="wide")

# --- Helper Functions ---
def parse_pdf_to_markdown(pdf_bytes):
    """Uses pymupdf4llm to convert PDF to markdown, preserving tables better."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf_bytes)
        tmp_path = tmp.name
    
    md_text = pymupdf4llm.to_markdown(tmp_path)
    os.remove(tmp_path)
    return md_text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks, model_provider):
    if model_provider == "Google Gemini":
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
    else:
        # Placeholder for local Ollama embeddings
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index_v2")
    return vector_store

def get_conversational_chain(model_provider):
    prompt_template = """
    Answer the question based on the provided bank statement context. 
    If the answer is not in the context, say "Data not found in the statement".
    
    Context:
    {context}
    
    Question: {question}
    Answer:
    """
    
    if model_provider == "Google Gemini":
        model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    else:
        # Placeholder for Ollama local model
        model = Ollama(model="llama3")

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)

def query_statement(user_question, model_provider):
    if model_provider == "Google Gemini":
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
    else:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        
    db = FAISS.load_local("faiss_index_v2", embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(user_question)
    chain = get_conversational_chain(model_provider)
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    return response["output_text"]

def extract_mock_transactions(md_text):
    """
    In a full production version, you would pass `md_text` to the LLM and ask it 
    to extract transactions into a JSON schema. For the sake of this UI demo, 
    we generate mock data that resembles what the LLM would output.
    """
    data = {
        "Date": ["2026-06-01", "2026-06-05", "2026-06-10", "2026-06-12", "2026-06-15", "2026-06-20"],
        "Description": ["Salary Deposit", "Grocery Store", "Electric Bill", "Restaurant", "Internet Bill", "Online Shopping"],
        "Category": ["Income", "Groceries", "Utilities", "Dining", "Utilities", "Shopping"],
        "Amount": [5000.00, -150.25, -85.50, -60.00, -50.00, -120.00]
    }
    return pd.DataFrame(data)

# --- UI Setup ---
st.title("🏦 AI Bank Statement Analyzer")

# Sidebar
with st.sidebar:
    st.header("Settings")
    model_provider = st.selectbox("Select AI Model", ["Google Gemini", "Ollama (Local)"])
    
    if model_provider == "Google Gemini" and not os.getenv("GOOGLE_API_KEY"):
        st.warning("⚠️ GOOGLE_API_KEY not found in environment.")
        
    if model_provider == "Ollama (Local)":
        st.info("Ensure Ollama is running locally (e.g. `ollama run llama3`).")

    st.markdown("---")
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Upload Bank Statement (PDF)", type=["pdf"])
    
    if uploaded_file and st.button("Process Document"):
        with st.spinner("Parsing PDF with PyMuPDF..."):
            md_text = parse_pdf_to_markdown(uploaded_file.read())
            st.session_state["md_text"] = md_text
            
            with st.spinner("Extracting Transactions & Building Vector Store..."):
                chunks = get_text_chunks(md_text)
                get_vector_store(chunks, model_provider)
                
                # Mock transaction extraction for Dashboard
                st.session_state["df"] = extract_mock_transactions(md_text)
                
            st.success("Processing Complete!")

# Main Content
tab1, tab2 = st.tabs(["📊 Financial Dashboard", "💬 Chat with Document"])

with tab1:
    st.subheader("Financial Overview")
    if "df" in st.session_state:
        df = st.session_state["df"]
        
        # Layout metrics
        total_income = df[df['Amount'] > 0]['Amount'].sum()
        total_expense = abs(df[df['Amount'] < 0]['Amount'].sum())
        net_flow = total_income - total_expense
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"${total_income:,.2f}")
        col2.metric("Total Expenses", f"${total_expense:,.2f}")
        col3.metric("Net Cash Flow", f"${net_flow:,.2f}", delta=float(net_flow))
        
        st.markdown("---")
        
        # Charts
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.markdown("**Spending by Category**")
            expense_df = df[df['Amount'] < 0].copy()
            expense_df['Amount'] = abs(expense_df['Amount'])
            fig_pie = px.pie(expense_df, values='Amount', names='Category', hole=0.4)
            st.plotly_chart(fig_pie, use_container_width=True)
            
        with col_chart2:
            st.markdown("**Cash Flow Timeline**")
            df_sorted = df.sort_values('Date')
            # Cumulative balance
            df_sorted['Balance'] = df_sorted['Amount'].cumsum()
            fig_line = px.line(df_sorted, x='Date', y='Balance', markers=True)
            st.plotly_chart(fig_line, use_container_width=True)
            
        st.markdown("**Extracted Transactions**")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Please upload and process a bank statement to view the dashboard.")

with tab2:
    st.subheader("Ask Questions About Your Statement")
    if "md_text" in st.session_state:
        user_q = st.text_input("E.g., 'What was my highest expense?' or 'How much did I spend on Utilities?'")
        if user_q:
            with st.spinner("Thinking..."):
                reply = query_statement(user_q, model_provider)
                st.write("**Answer:**")
                st.info(reply)
                
        with st.expander("View Raw Parsed Markdown"):
            st.text(st.session_state["md_text"])
    else:
        st.info("Please upload a bank statement first.")
