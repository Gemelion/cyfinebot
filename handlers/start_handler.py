
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для проверки штрафов.")

# Для регистрации через Application:
def get_start_handler():
    return CommandHandler("start", start_handler)
