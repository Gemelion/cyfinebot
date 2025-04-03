from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def feedback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напишите свой вопрос или отзыв, и мы свяжемся с вами.")

def get_feedback_handler():
    return CommandHandler("contact", feedback_handler)
