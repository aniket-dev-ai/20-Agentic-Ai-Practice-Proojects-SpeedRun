from prompts.Summary_generator_prompt import summary_prompt
from langchain_core.output_parsers import StrOutputParser

def generate_summary_with_streaming(text: str , LLM) :
    """
    Generate a summary of the given text.

    Args:
        text (str): The text to summarize.

    Returns:
        str: A summary of the text.
    """
    chain = summary_prompt | LLM | StrOutputParser()
    
    response = chain.stream(input={ "text": text })
    for chunk in response:
        print(chunk, end="", flush=True)
    