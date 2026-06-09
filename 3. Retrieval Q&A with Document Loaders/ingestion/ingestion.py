import sys
from pathlib import Path
from langchain_core.documents import Document

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from embeddings.embedding import vector_store

PROJECT_ROOT = Path(__file__).resolve().parent.parent
print(f"Project root: {PROJECT_ROOT}")

documents = []

chunks_dir = PROJECT_ROOT / "text_splitters" / "chunks"

for chunk_file in chunks_dir.glob("*.txt"): 
    text = chunk_file.read_text(encoding="utf-8")

    documents.append(
        Document(
            page_content=text,
            metadata={
                "source": chunk_file.name
            }
        )
    )

print(f"Loaded {len(documents)} chunks") 

vector_store.add_documents(documents)

print("Documents added to vector store")