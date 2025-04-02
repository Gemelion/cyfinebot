import os
import logging
import asyncio
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Инициализация логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получение токена и вебхука из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_PATH = f"/webhook/{TOKEN}"
FULL_WEBHOOK_URL = WEBHOOK_URL + WEBHOOK_PATH

# Инициализация Telegram и FastAPI
bot_app = Application.builder().token(TOKEN).build()
app = FastAPI()

# Вебхук FastAPI
@app.post(WEBHOOK_PATH)
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"ok": True}

@app.on_event("startup")
async def on_startup():
    await bot_app.bot.set_webhook(FULL_WEBHOOK_URL)
    logger.info("🚀 Вебхук установлен и бот запущен!")

# Команды Telegram
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я бот для проверки штрафов на Кипре. "
        "Данные шифруются и обрабатываются по правилам GDPR. "
        "Нажми /info для подробностей."
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """📄 *GDPR и защита данных*

Я собираю только:
- Тип документа
- Номер удостоверения
- Номер автомобиля

Все данные хранятся в зашифрованном виде.

Ты можешь:
• Просмотреть — /view
• Удалить — /delete
• Запросить удаление — /contact

🔐 С нами можно связаться через /contact""",
        parse_mode="Markdown"
    )

# Регистрируем команды
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("info", info))