from telegram.ext import (
    Application,
    ApplicationBuilder,
)
from handlers.start_handler import start_handler
import os

def get_bot_application(token: str) -> Application:
    application = ApplicationBuilder().token(token).build()
    application.add_handler(start_handler)
    return application
