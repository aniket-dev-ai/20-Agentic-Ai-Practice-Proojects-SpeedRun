from langchain_core.prompts import ChatPromptTemplate


summary_prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant.

    Generate a concise summary of the following text:

    {text}

    Keep the summary under 2-3 lines.
    """
)
