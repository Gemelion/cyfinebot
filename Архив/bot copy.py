import asyncio
import logging
from telegram.ext import Application
from bot_config import BOT_TOKEN
from handlers.start_handler import start_handler
from database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_bot_application() -> Application:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(start_handler)
    return application

# При запуске файла создаем БД
if __name__ == "__main__":
    init_db()
    app = get_bot_application()
    app.run_polling()
