
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from handlers.start_handler import start_handler
from handlers.fine_check_handler import fine_check_handler
from handlers.gdpr_handler import gdpr_handler
from handlers.admin_handler import admin_handler
from handlers.register_handler import register_handler
from handlers.view_data_handler import view_data_handler
from handlers.delete_data_handler import delete_data_handler
from handlers.feedback_handler import feedback_handler


def get_bot_application(token: str):
    application = ApplicationBuilder().token(token).build()

    application.add_handler(start_handler)
    application.add_handler(register_handler)
    application.add_handler(fine_check_handler)
    application.add_handler(view_data_handler)
    application.add_handler(delete_data_handler)
    application.add_handler(feedback_handler)
    application.add_handler(gdpr_handler)
    application.add_handler(admin_handler)

    return application
