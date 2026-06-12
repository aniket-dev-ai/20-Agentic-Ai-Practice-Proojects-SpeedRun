from langchain_ollama import OllamaEmbeddings

embeddings_model = OllamaEmbeddings(
    model="qwen3-embedding:0.6b",
    dimensions=1024
)