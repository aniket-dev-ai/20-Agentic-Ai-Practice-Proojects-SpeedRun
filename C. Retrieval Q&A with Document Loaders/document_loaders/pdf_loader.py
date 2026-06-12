import pymupdf4llm
import pymupdf


file_path="../The GTA VI Document (v1.0).pdf"

doc = pymupdf.open(file_path)

with open("pdfText.txt" , "w" , encoding="utf-8") as f:
    for page in doc:
        text = page.get_text()
        f.write(str(text))