
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def gdpr_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 GDPR: Вы можете запросить доступ к данным, их удаление или исправление. "
        "Используйте команду /contact для связи."
    )

def get_gdpr_handler():
    return CommandHandler("gdpr", gdpr_handler)
