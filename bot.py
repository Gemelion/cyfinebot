
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.start import start_handler
from handlers.help import help_handler
from handlers.feedback import feedback_handler

def get_bot_application(token: str) -> Dispatcher:
    bot = Bot(token=token, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_handler)
    dp.include_router(help_handler)
    dp.include_router(feedback_handler)

    return dp
