from prompts.Motivational_quote_generator_prompt import motivational_quote_prompt
from langchain_core.output_parsers import StrOutputParser


def generate_motivational_quote_with_batch(topics: list , LLM) :
    """
    Generate motivational quotes about the given topics.

    Args:
        topics (list): A list of topics for the motivational quotes.

    Returns:
        list: A list of motivational quotes about the topics.
    """
    
    inputs = [
        {"topic": topic}
        for topic in topics
    ]
    
    chain = motivational_quote_prompt | LLM | StrOutputParser()
    
    response = chain.batch(inputs)
    return response