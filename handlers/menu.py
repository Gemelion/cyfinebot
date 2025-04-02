from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Меню:\n\n"
        "/start - Перезапустить бота\n"
        "/register - Регистрация\n"
        "/status - Проверить статус\n"
        "/gdpr - Информация о GDPR\n"
        "/delete - Удалить мои данные"
    )

def register_menu_handlers(application):
    application.add_handler(CommandHandler("menu", menu_command))
