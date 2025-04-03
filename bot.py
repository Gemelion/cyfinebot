from telegram.ext import Application, CommandHandler
from handlers.start_handler import start_handler


def get_bot_application(token: str) -> Application:
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start_handler))
    return application
