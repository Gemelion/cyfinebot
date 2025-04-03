
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 Панель администратора. Здесь будет управление пользователями.")

def get_admin_handler():
    return CommandHandler("admin", admin_handler)
