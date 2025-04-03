
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

start_handler = CommandHandler("start", lambda update, context: update.message.reply_text(
    "👋 Добро пожаловать в CyFineBot!

"
    "🔍 Чтобы проверить штрафы, введите ваш идентификатор (ARC/ID) и номер автомобиля.
"
    "📘 Мы обрабатываем ваши данные в соответствии с GDPR.
"
    "✅ Продолжая, вы даёте согласие на обработку данных для проверки штрафов."
))
