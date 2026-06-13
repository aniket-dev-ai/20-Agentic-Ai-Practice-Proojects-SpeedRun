import sqlite3
from telegram import Update
from telegram.ext import ContextTypes

DB_FILE = "users.db"

# Conversation states
ASK_NAME, ASK_EMAIL, ASK_PHONE = range(3)


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT
        )
    """)
    conn.commit()
    conn.close()


def is_registered(user_id: int) -> bool:
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    conn.close()
    return result is not None


def save_user(user_id: int, name: str, email: str, phone: str):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (user_id, name, email, phone) VALUES (?, ?, ?, ?)",
        (user_id, name, email, phone)
    )
    conn.commit()
    conn.close()


async def check_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Call this when a user interacts with the bot.
    If already registered -> does nothing (pass).
    If not registered -> starts asking for name, email, phone.
    Returns True if registered (so calling code can continue),
    False if registration flow was started (calling code should stop).
    """
    if update.effective_user is None or update.message is None:
        return False

    user_id = update.effective_user.id
    user_data = context.user_data
    if user_data is None:
        return False

    if is_registered(user_id):
        return True  # already registered, just pass

    # Not registered -> start registration flow
    user_data["registering"] = True
    user_data["reg_step"] = ASK_NAME
    await update.message.reply_text("Welcome! You're not registered yet. What's your name?")
    return False


async def handle_registration_step(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Call this on every message while registration is in progress.
    Walks through name -> email -> phone, then saves the user.
    """
    if update.effective_user is None or update.message is None:
        return

    user_id = update.effective_user.id
    text = update.message.text.strip() if update.message.text else ""
    user_data = context.user_data
    if user_data is None:
        return

    step = user_data.get("reg_step")

    if step == ASK_NAME:
        user_data["reg_name"] = text
        user_data["reg_step"] = ASK_EMAIL
        await update.message.reply_text("Great. What's your email address?")

    elif step == ASK_EMAIL:
        user_data["reg_email"] = text
        user_data["reg_step"] = ASK_PHONE
        await update.message.reply_text("Got it. What's your phone number?")

    elif step == ASK_PHONE:
        user_data["reg_phone"] = text

        save_user(
            user_id,
            user_data["reg_name"],
            user_data["reg_email"],
            user_data["reg_phone"]
        )

        user_data["registering"] = False
        user_data.pop("reg_step", None)
        await update.message.reply_text("You're registered! You can now chat normally.")


# Initialize DB on import
init_db()