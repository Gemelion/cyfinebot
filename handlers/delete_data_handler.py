
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def delete_data_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🗑 Запрос на удаление данных получен. Эта функция в разработке.")

def get_delete_data_handler():
    return CommandHandler("delete", delete_data_handler)
