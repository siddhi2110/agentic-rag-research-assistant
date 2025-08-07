from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(chunks, embeddings)
    return vectorstore
