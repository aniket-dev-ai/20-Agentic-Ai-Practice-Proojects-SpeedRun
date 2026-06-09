from llm.geminiAi import agent 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from print import inspect_agent_response

prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that answers questions based on retrieved information."),
            ("human", "{query}"),
        ]
    )

def main():
    query = "GTA 6 story is inspired by what?"
    print(f"Query: {query}")
    print(type(agent))
    chain = prompt | agent 
    print("Retrieving information...")
    response = chain.invoke({"query": query})
    print(f"Response: \n")
    inspect_agent_response(response)
    
if __name__ == "__main__":
    main()