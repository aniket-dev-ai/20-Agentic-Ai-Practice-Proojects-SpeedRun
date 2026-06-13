from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
load_dotenv()
import os
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent))  # add parent dir to path to import state.user_registeration
from Data.user_registeration import check_registration , handle_registration_step
from Data.session_store import (
    get_session,
    create_session,
    end_session,
    add_message,
    get_messages,
    increment_followup,
    set_current_question,
    get_current_question,
)

from Ai.question_agent import start_session
from message_handler import receive_message
from voice_handler import receive_voice


BOT_TOKEN = os.getenv("telegram_bot_api")  # get this from @BotFather on Telegram
if not BOT_TOKEN:
    raise RuntimeError("telegram_bot_api environment variable is not set")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received /start command")
    if update.effective_user is None or update.message is None or update.effective_chat is None:
        return
    print(f"User: {update.effective_user.id}, Chat: {update.effective_chat.id}")
    user_id = update.effective_user.id 
    await check_registration(update, context)
    print(f"Starting session for user {user_id}")
    create_session(user_id)
    print(f"Session created for user {user_id}")
    await start_session(user_id, context.bot, update.effective_chat.id)



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ = context
    if update.message is None:
        return
    await update.message.reply_text("Just type anything and I'll respond. Use /start to begin.")



async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received chat message")
    if update.effective_user is None or update.message is None:
        return
    print(f"User: {update.effective_user.id}, Message: {update.message.text}")
    user_id = update.effective_user.id
    print(f"User {user_id} sent a message: {update.message.text}")
    if (context.user_data or {}).get("registering"):
        await handle_registration_step(update, context)
        return
    
    print(f"Processing message for user {user_id}")
    # Check registration status first
    registered = await check_registration(update, context)
    print(f"User {user_id} registration status: {registered}")
    if not registered:
        return  # registration flow just started, wait for next message
    print(f"User {user_id} is registered, proceeding with session handling")
    user_text = update.message.text or ""
    
    print(f"Retrieving session for user {user_id}")
    get_session(user_id)
    
    print(f"Adding message for user {user_id}")
    add_message(user_id, "user", user_text)
    count = increment_followup(user_id)

    print(f"Follow-up count for user {user_id}: {count}")
    if not get_current_question(user_id):
        set_current_question(user_id, user_text)
    
    print(f"Current question for user {user_id}: {get_current_question(user_id)}")
    reply = (
        f"You said: {user_text}\n"
        f"Follow-up count: {count}\n"
        f"Current question: {get_current_question(user_id)}\n"
        f"Messages so far: {len(get_messages(user_id))}"
    )
    
    print(f"Replying to user {user_id} with: {reply}")
    
    add_message(user_id, "bot", reply)
    
    print(f"Sending reply to user {user_id}")
    await receive_message(update, context)

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _ = context
    if update.effective_user is None or update.message is None:
        return
    user_id = update.effective_user.id
    end_session(user_id)
    await update.message.reply_text("Session ended.")
    



if __name__ == "__main__":
    print("Starting bot...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    print("Adding handlers...")
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, receive_voice))

    print("Bot is running...")
    app.run_polling()