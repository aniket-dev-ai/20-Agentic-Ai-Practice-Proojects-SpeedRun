from Data.session_store import create_session, set_current_question


def generate_daily_question():
    """
    Returns the daily accountability question.
    Hardcoded for now - can later be randomized or AI-generated.
    """
    return "What will you complete today?"


async def start_session(user_id, bot, chat_id):
    """
    Initiates the daily accountability conversation:
    1. Create a fresh session
    2. Generate the daily question
    3. Save it as the current question
    4. Send it to the user
    """
    # 1. Create session
    create_session(user_id)

    # 2. Generate question
    question = generate_daily_question()

    # 3. Save question
    set_current_question(user_id, question)

    # 4. Send question
    await bot.send_message(chat_id=chat_id, text=question)