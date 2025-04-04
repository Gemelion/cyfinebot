import os
from telegram.ext import ApplicationBuilder
from handlers.start_handler import start_handler
from db import init_db


def get_bot_application():
    # Инициализация базы данных при запуске бота
    init_db()

    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(start_handler)
    application.initialize()  # Инициализация Application вручную
    return application
