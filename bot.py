
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode  # Исправленный импорт для aiogram 3.x

from aiogram.utils import executor

TOKEN = "YOUR_BOT_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: Message):
    await message.reply("👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.", parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    executor.start_polling(dp)
    