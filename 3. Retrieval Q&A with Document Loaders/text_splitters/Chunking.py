import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("../document_loaders/pdfText.txt" , "r" , encoding="utf-8") as f:
    document = f.read()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_text(document)

output_dir = "./chunks"
os.makedirs(output_dir, exist_ok=True)

for i, text in enumerate(texts):
    print(f"creating chunk {i} with length {len(text)}")
    with open(f"./chunks/chunk_{i}.txt", "w", encoding="utf-8") as f:
        f.write(text)