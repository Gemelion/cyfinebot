from telegram.ext import Application
from bot_config import BOT_TOKEN
from handlers import start_handler

application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(start_handler)

def get_bot_application():
    return application