from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

async def start_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("🔐 Начать регистрацию")]]
    await update.message.reply_text(
        "Добро пожаловать! Нажмите кнопку ниже, чтобы начать регистрацию.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

def register_registration_handlers(app):
    app.add_handler(CommandHandler("start", start_registration))
