import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)

from handlers.start_handler import start_handler
from database import init_db

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def get_bot_application():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_handler))

    return application

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    init_db()
    app = get_bot_application()
    app.run_polling()
