from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler, ConversationHandler, filters
)
from handlers import (
    start_handler, register_handler, view_data_handler,
    delete_data_handler, feedback_handler, gdpr_handler,
    menu_handler
)
from config import BOT_TOKEN

def get_bot_application() -> Application:
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(start_handler)
    app.add_handler(register_handler)
    app.add_handler(view_data_handler)
    app.add_handler(delete_data_handler)
    app.add_handler(feedback_handler)
    app.add_handler(gdpr_handler)
    app.add_handler(menu_handler)

    return app
