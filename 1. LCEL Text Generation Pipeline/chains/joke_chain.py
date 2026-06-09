from prompts.joke_prompt import joke_prompt
from langchain_core.output_parsers import StrOutputParser

def generate_joke(topic: str , LLM) :
    """
    Generate a joke about the given topic.

    Args:
        topic (str): The topic for the joke.

    Returns:
        str: A joke about the topic.
    """
    chain = joke_prompt | LLM | StrOutputParser()
    
    response = chain.invoke(input={ "topic": topic })
    return response