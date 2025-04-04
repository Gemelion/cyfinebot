from database import init_db
from telegram.ext import ApplicationBuilder

from handlers.start_handler import start_handler

def get_bot_application():
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(start_handler)
    init_db()
    return application