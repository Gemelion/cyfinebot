from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

GDPR_INFO = """
📄 *GDPR и защита данных*

Мы обрабатываем ваши следующие данные:
• Имя пользователя Telegram
• Telegram ID
• Данные для проверки штрафов на сайте cycamerasystem.com.cy (тип документа, ID)

Данные шифруются и хранятся на сервере. Вы можете:
• 📄 Получить копию данных (/profile)
• ❌ Удалить все данные (/delete)
• 📬 Отправить запрос на реализацию прав через /contact

Контакт для запросов: @iv_van
"""

async def privacy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(GDPR_INFO)

def register_privacy_handlers(app):
    app.add_handler(CommandHandler("gdpr", privacy))
