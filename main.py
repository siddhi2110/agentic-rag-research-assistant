from load_and_split import load_documents, split_documents
from vectorstore import create_vector_store

# Step 1: Load and split the documents
documents = load_documents()
chunks = split_documents(documents)

# Step 2: Create a vector store using free HuggingFace embeddings
vectorstore = create_vector_store(chunks)

# Step 3: Ask the user a question
query = input("\n🧠 Ask your AI Research Assistant a question: ")

# Step 4: Retrieve top matching chunks
retriever = vectorstore.as_retriever(search_type="similarity", k=3)
relevant_docs = retriever.invoke(query)

# Step 5: Show matching chunks
print("\n🔍 Top Matching Results:\n")
for i, doc in enumerate(relevant_docs, 1):
    print(f"{i}. {doc.page_content[:200]}...\n")
