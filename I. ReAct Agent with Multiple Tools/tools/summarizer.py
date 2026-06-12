from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite",)

@tool
def summarize_text(text: str) -> str:
    """Summarizes the given text using a language model."""
    prompt = f"Please summarize the following text:\n\n{text}"
    
    chain = model | StrOutputParser()
    
    response = chain.invoke(prompt)
    return response
