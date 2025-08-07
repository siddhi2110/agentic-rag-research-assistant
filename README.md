# Agentic RAG-Powered AI Research Assistant

This project is a lightweight AI research assistant that leverages **LangChain**, **ChromaDB**, and **OpenAI API** to answer questions based on a custom corpus using **Retrieval-Augmented Generation (RAG)**.

## 🔍 About the Project

This assistant allows users to ask questions like “What is AI Safety?” and get accurate responses grounded in relevant documents. It demonstrates the power of agentic RAG with embeddings, vector stores, and LLMs in a modular and beginner-friendly setup.

## 🛠 Tech Stack
- Python
- LangChain
- OpenAI API
- ChromaDB
- HuggingFace Embeddings

## 📂 Features
- Upload your own corpus in `corpus.txt`
- Generates embeddings and stores them in ChromaDB
- Accepts natural language queries and returns AI-generated answers
- Modular code for retriever, vectorstore, and agent logic

## 🚀 How to Run
1. Clone the repo:
   
   git clone https://github.com/siddhi2110/agentic-rag-research-assistant.git
   cd agentic-rag-research-assistant
   
2. Create and activate a virtual environment:
   
       python -m venv .venv
       .venv\Scripts\activate

3. Install requirements:

       pip install -r requirements.txt

4. Add your OpenAI key in a .env file:

       OPENAI_API_KEY=your_api_key_here

5. Run the assistant:

       python main.py
