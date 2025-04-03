from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

start_text = (
    "👋 Добро пожаловать в CyFineBot!\n\n"
    "🔍 С помощью этого бота вы можете проверять наличие штрафов по номеру автомобиля и ARC/ID.\n\n"
    "💬 Для начала, пожалуйста, согласитесь на обработку персональных данных.\n"
    "Это необходимо согласно требованиям GDPR.\n\n"
    "Если вы согласны, введите: /agree\n"
    "Если хотите узнать больше, введите: /gdpr\n\n"
    "После согласия вам будет предложено ввести номер ARC/ID и номер автомобиля."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(start_text)

start_handler = CommandHandler("start", start)
