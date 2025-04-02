from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 Меню:
/profile — Просмотр данных
/delete — Удалить данные")

def register_menu_handlers(app):
    app.add_handler(CommandHandler("menu", menu))
