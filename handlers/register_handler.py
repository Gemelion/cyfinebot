
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Регистрация пока не реализована. Функция в разработке.")

def get_register_handler():
    return CommandHandler("register", register_handler)
