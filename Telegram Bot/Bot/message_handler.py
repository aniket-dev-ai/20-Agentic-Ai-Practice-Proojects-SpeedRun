from typing import Optional

from telegram import Update
from telegram.ext import ContextTypes
 
from Data.session_store import (
    get_session,
    add_message,
    set_current_question,
    set_session_complete,
    increment_followup,
)
from Ai.analysis import analyze_response
from Ai.session_summary import send_session_summary

async def receive_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: Optional[str] = None
):
    """
    Flow:
    User Message (text or transcribed voice)
      -> Find User
      -> Find Session
      -> Append Message
      -> Run Conversation Logic
    """
    # 1. Find User
    # Guard against None for effective_user/message which can happen in some
    # update types. If missing, abort early.
    if update.effective_user is None:
        return
    user_id = update.effective_user.id

    user_text = (
        text
        if text is not None
        else ((update.message.text or "") if update.message else "")
    )

    # 2. Find Session (auto-creates if missing)
    session = get_session(user_id)

    print(f"User {user_id} sent a message: {user_text}")
    
    # 3. Append Message
    add_message(user_id, "user", user_text)

    print(f"Follow-up count for user {user_id}: {session.get('followup_count', 0)}")
    
    # 4. Run Conversation Logic
    reply = await run_conversation_logic(user_id, session, user_text)

    print(f"Replying to user {user_id} with: {reply}")
    
    # Save bot's reply too
    add_message(user_id, "bot", reply)

    # message; if none, do nothing.
    print(f"Sending reply to user {user_id}")
    reply_target = update.message or update.effective_message
    
    if reply_target:
        print(f"Replying to user {user_id} with: {reply}")
        await reply_target.reply_text(reply)

    if session.get("session_complete"):
        # Guard against missing chat information on some update types
        chat = update.effective_chat or (update.message.chat if update.message else None)
        if chat is None:
            # Nothing we can do without a chat id
            return
        await send_session_summary(
            user_id,
            get_session(user_id)["messages"],
            context.bot,
            chat.id,
        )

async def run_conversation_logic(user_id, session, user_text):
    """
    Step 10: Uses Gemini (via LangChain) to decide whether a follow-up
    is needed, what to ask, and whether the session is complete.
    """
    current_question = session.get("current_question", "")
    print(f"Current question for user {user_id}: {current_question}")
    messages = session.get("messages", [])
    print(f"Messages for user {user_id}: {messages}")
    result = analyze_response(current_question, messages, user_text)
    print(f"Analysis result for user {user_id}: {result}")
    if result["session_complete"]:
        print(f"Session for user {user_id} marked complete.")
        set_session_complete(user_id, True)
        return "Thanks! That wraps up today's check-in. 🎉"

    if result["need_followup"] and result["followup_question"]:
        increment_followup(user_id)
        print(f"Follow-up question for user {user_id}: {result['followup_question']}")
        set_current_question(user_id, result["followup_question"])
        return result["followup_question"]

    # No follow-up needed, but session not marked complete either
    return "Got it, thanks!"