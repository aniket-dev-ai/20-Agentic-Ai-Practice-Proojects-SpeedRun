from llm.gemini import model
from custom_tool import tools
from langchain.agents import create_agent

with open("system_prompt.txt", "r") as f:
    system = f.read()

agent = create_agent(
    tools=tools,
    system_prompt=system,
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