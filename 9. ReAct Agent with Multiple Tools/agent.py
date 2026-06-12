from langchain.agents import create_agent
from tool_merge import ALL_TOOLS
from llm.gemini import model  
from tools.file_writer import create_pdf

with open("./prompts/react_prompt.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

agent = create_agent(
    tools=ALL_TOOLS,
    system_prompt=SYSTEM_PROMPT,
    model=model,
)

def run_agent(query): 
    response = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": query}
        ]
    }
    )
    return response

def create_structured_report(query):
     create_pdf(query)
     return "Structured report created."
