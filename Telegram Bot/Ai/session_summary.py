import os
import sqlite3
from datetime import datetime

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from Data.user_registeration import DB_FILE

# Reuse same LLM setup style as analysis.py
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3,
)

SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You are an accountability coach bot. Summarize today's check-in "
     "conversation in a short, friendly way (3-5 sentences). "
     "Highlight what the user committed to, any blockers mentioned, "
     "and an encouraging note for tomorrow."),
    ("human", "Conversation:\n{history}")
])

summary_chain = SUMMARY_PROMPT | llm | StrOutputParser()

SUMMARY_DIR = "session_summaries"


def format_history(messages):
    lines = []
    for msg in messages:
        role = "User" if msg["role"] == "user" else "Bot"
        lines.append(f"{role}: {msg['content']}")
    return "\n".join(lines)


def get_user_name(user_id: int) -> str:
    """Fetch the registered name for a user from the registration DB."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT name FROM users WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    if row and row[0]:
        return row[0]
    return f"user_{user_id}"


def generate_summary(messages: list) -> str:
    """Generate a short summary of the session using Gemini."""
    history_text = format_history(messages)

    if not history_text.strip():
        return "No conversation took place in this session."

    try:
        return summary_chain.invoke({"history": history_text}).strip()
    except Exception as e:
        print(f"Summary generation error: {e}")
        return "Could not generate a summary for this session, but it has been logged."


def save_summary_to_file(user_id: int, summary: str, messages: list) -> str:
    """
    Save the summary + transcript to a file inside SUMMARY_DIR,
    named with the user's registered name and current date/time.
    Returns the file path.
    """
    os.makedirs(SUMMARY_DIR, exist_ok=True)

    name = get_user_name(user_id)
    safe_name = "".join(c for c in name if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"{safe_name}_{timestamp}.txt"
    filepath = os.path.join(SUMMARY_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Session Summary for {name} (user_id: {user_id})\n")
        f.write(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")
        f.write("SUMMARY:\n")
        f.write(summary + "\n\n")
        f.write("=" * 50 + "\n\n")
        f.write("FULL CONVERSATION:\n")
        f.write(format_history(messages) + "\n")

    return filepath


async def send_session_summary(user_id: int, messages: list, bot, chat_id):
    """
    Full flow:
    1. Generate summary via LLM
    2. Save summary + transcript to file (named by registered user + date/time)
    3. Send summary back to the user on Telegram
    """
    summary = generate_summary(messages)
    filepath = save_summary_to_file(user_id, summary, messages)

    print(f"Saved session summary to: {filepath}")

    await bot.send_message(
        chat_id=chat_id,
        text=f"📋 Here's a summary of today's check-in:\n\n{summary}"
    )