from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Добро пожаловать в CyFineBot!\n"
        "Этот бот помогает проверять штрафы по номеру ARC/ID и номеру автомобиля.\n\n"
        "Чтобы продолжить, введите свой ID (ARC/Alien Registration Certificate)."
    )

start_handler = CommandHandler("start", start)
