
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    # Fixed: closing the string literal properly
    await message.answer("👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
