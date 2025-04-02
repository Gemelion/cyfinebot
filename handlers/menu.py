from telegram import Update
from telegram.ext import ContextTypes

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """📋 Меню:

Выберите действие:
- 📝 Регистрация
- 📷 Проверка штрафов
- ⚙️ Настройки
- ℹ️ GDPR и контакты"""
    )
