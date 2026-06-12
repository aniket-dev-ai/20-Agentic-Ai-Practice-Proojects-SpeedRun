from langchain_core.prompts import ChatPromptTemplate


motivational_quote_prompt = ChatPromptTemplate.from_template(
    """
    You are a humourus motivational speaker.

    Generate a short motivational quote about: {topic}

    Keep the quote under 2-3 lines.
    """
)
