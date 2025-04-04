from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.ext import ApplicationBuilder

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Добро пожаловать в CyFineBot!")

start_handler = CommandHandler("start", start)
