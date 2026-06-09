from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from Retreival.retrieve import retrieve
load_dotenv()

toolkit = [retrieve]
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

agent = create_agent(
    tools=toolkit,
    model=model
    )