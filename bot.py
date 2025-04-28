
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode, Message
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    await message.reply("👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
