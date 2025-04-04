from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler
from db import add_user, user_exists

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "Unknown"

    if not user_exists(user_id):
        add_user(user_id, username)

    keyboard = [
        [InlineKeyboardButton("Проверить штрафы", callback_data="check_fines")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Добро пожаловать в CyFineBot!

С помощью этого бота вы можете проверять наличие штрафов по вашему автомобилю.",
        reply_markup=reply_markup
    )

start_handler = CommandHandler("start", start)
