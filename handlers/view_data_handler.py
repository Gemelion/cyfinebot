
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def view_data_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📄 Просмотр данных пока не реализован. Эта функция в разработке.")

def get_view_data_handler():
    return CommandHandler("view", view_data_handler)
