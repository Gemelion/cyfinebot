from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

ADMIN_ID = 123456789  # замените на ваш Telegram ID

async def delete_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Доступ запрещён.")
        return
    await update.message.reply_text("Пользовательские данные удалены (заглушка).")

def register_admin_handlers(app):
    app.add_handler(CommandHandler("admin_delete", delete_user))
