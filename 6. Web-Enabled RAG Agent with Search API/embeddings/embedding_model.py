from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b",
    dimensions=1024
)

def embedding(doc , vector_store):
    print("Generating embeddings and adding to vector store...")
    vector_store.add_documents(doc)
    print("Embeddings generated and added to vector store successfully.")
    return True