from calculator_tool.tool import calculator
from wikipedia_tool.tool import wiki_tool
from langchain.agents import create_agent
from llm.geminiAi import model


system = "You are a helpful assistant that can use tools to answer questions. You have access to the following tools: calculator, wiki_tool. Use them to answer the user's question. If you don't know the answer, say you don't know. Always use the tools when necessary and don't make up answers." 

agent = create_agent(
    tools=[calculator, wiki_tool],
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


