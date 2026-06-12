from pathlib import Path

import pymupdf
from langchain.tools import tool


@tool
def extract_pdf_text(file_path: str) -> str:
    """
    Extract all text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text from the PDF.
    """

    try:
        pdf_path = Path(file_path)

        if not pdf_path.exists():
            return f"File not found: {file_path}"

        doc = pymupdf.open(pdf_path)

        pages = []

        for page in doc:
            pages.append(page.get_text())

        doc.close()

        return "\n\n".join(pages)

    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"