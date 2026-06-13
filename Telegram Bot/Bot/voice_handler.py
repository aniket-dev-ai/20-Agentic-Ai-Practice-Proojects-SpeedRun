import os
from telegram import Update
from telegram.ext import ContextTypes

from message_handler import receive_message
from faster_whisper import WhisperModel

# Model ek baar load karo — module level pe (efficient hai)
# model size options: "tiny", "base", "small", "medium", "large-v3"
# CPU pe: compute_type="int8", GPU pe: compute_type="float16"
_whisper_model = WhisperModel("turbo", device="cuda", compute_type="float16")


async def receive_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Flow:
    Voice Note -> Download -> Transcribe -> Text -> Same Pipeline
    """
    if not update.message:
        return

    voice = update.message.voice or update.message.audio
    if voice is None:
        await update.message.reply_text("Couldn't read that voice note.")
        return

    # 1. Download
    file = await context.bot.get_file(voice.file_id)
    if not update.effective_user:
        return
    file_path = f"voice_{update.effective_user.id}.ogg"
    await file.download_to_drive(file_path)

    # 2. Transcribe
    try:
        text = transcribe_audio(file_path)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    if not text:
        await update.message.reply_text("Sorry, I couldn't understand that audio.")
        return

    # 3. Text -> Same Pipeline
    await receive_message(update, context, text=text)


def transcribe_audio(file_path: str) -> str:
    """
    Faster-Whisper se audio transcribe karta hai.
    Returns the transcribed text as a single string.
    """
    segments, _info = _whisper_model.transcribe(file_path, beam_size=5)
    # segments ek generator hai — join karke full text banao
    full_text = " ".join(segment.text.strip() for segment in segments)
    return full_text.strip()