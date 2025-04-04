from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers.start_handler import start_handler, consent_callback_handler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

dp.message.register(start_handler, commands=["start"])
dp.callback_query.register(consent_callback_handler, lambda c: c.data.startswith("consent"))

def get_bot_application():
    return dp
