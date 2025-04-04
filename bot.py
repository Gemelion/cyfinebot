import os
from telegram.ext import Application
from handlers.start_handler import start_handler
from db import init_db

def get_bot_application(token: str) -> Application:
    application = Application.builder().token(token).build()
    application.add_handler(start_handler)
    return application

# При импорте и запуске — инициализируем базу
init_db()
