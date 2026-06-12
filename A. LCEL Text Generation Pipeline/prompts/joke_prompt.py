from langchain_core.prompts import ChatPromptTemplate


joke_prompt = ChatPromptTemplate.from_template(
    """
    You are a funny comedian.

    Generate a short joke about: {topic}

    Keep the joke under 2 lines with easy english.
    """
)
