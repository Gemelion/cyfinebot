from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Проверить штрафы", callback_data="check_fines")],
        [InlineKeyboardButton("Мои данные", callback_data="my_data")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Добро пожаловать в CyFineBot!

"
        "Здесь вы можете проверить штрафы по номеру автомобиля и ARC.

"
        "Выберите действие ниже:",
        reply_markup=reply_markup
    )

start_handler = CommandHandler("start", start)