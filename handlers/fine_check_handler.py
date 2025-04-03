
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

async def fine_check_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Эта функция пока в разработке. Введите ваш номер ARC/ID и номер автомобиля.")

def get_fine_check_handler():
    return MessageHandler(filters.TEXT & (~filters.COMMAND), fine_check_handler)
