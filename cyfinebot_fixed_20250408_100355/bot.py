from aiogram import Bot, Dispatcher
from bot_config import BOT_TOKEN, DEFAULT_PROPERTIES
from handlers.start_handler import router as start_router

bot = Bot(token=BOT_TOKEN, default=DEFAULT_PROPERTIES)
dp = Dispatcher()
dp.include_router(start_router)
