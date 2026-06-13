import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Requires: pip install langchain-google-genai
# Set GOOGLE_API_KEY env var (or pass google_api_key="...")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3,
)

ANALYSIS_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You are an accountability coach bot analyzing a user's response.\n"
     "Decide whether a follow-up question is needed to get a clearer, "
     "more complete answer, or whether the session is done.\n\n"
     "Respond ONLY with valid JSON in this exact format, no extra text:\n"
     "{{\n"
     '  "need_followup": true or false,\n'
     '  "followup_question": "string (empty if not needed)",\n'
     '  "session_complete": true or false\n'
     "}}"),
    ("human",
     "Current Question: {current_question}\n\n"
     "Conversation History:\n{history}\n\n"
     "Latest User Message: {latest_message}")
])

parser = JsonOutputParser()

analysis_chain = ANALYSIS_PROMPT | llm | parser


def format_history(messages):
    """Convert message list into a readable transcript string."""
    lines = []
    for msg in messages:
        role = "User" if msg["role"] == "user" else "Bot"
        lines.append(f"{role}: {msg['content']}")
    return "\n".join(lines)


def analyze_response(current_question: str, messages: list, latest_message: str) -> dict:
    """
    Input:
      - current_question: the question currently being asked
      - messages: full conversation history (list of {"role": ..., "content": ...})
      - latest_message: the user's most recent message

    Output (dict):
      {
        "need_followup": bool,
        "followup_question": str,
        "session_complete": bool
      }
    """
    print(f"Analyzing response for current question: {current_question}")
    history_text = format_history(messages)
    print(f"Conversation history:\n{history_text}")
    try:
        print(f"Invoking analysis chain with latest message: {latest_message}")
        result = analysis_chain.invoke({
            "current_question": current_question,
            "history": history_text,
            "latest_message": latest_message
        })
        print(f"Analysis result: {result}")
    except Exception as e:
        # Fallback if LLM call/parsing fails
        print(f"Analysis error: {e}")
        result = {
            "need_followup": False,
            "followup_question": "",
            "session_complete": True
        }

    # Ensure all expected keys exist with correct types
    print(f"Validating analysis result keys and types")
    return {
        "need_followup": bool(result.get("need_followup", False)),
        "followup_question": str(result.get("followup_question", "")),
        "session_complete": bool(result.get("session_complete", False))
    }