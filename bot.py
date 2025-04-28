from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode  # Подтверждаем использование корректного импорта для ParseMode
import logging
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# Хэндлер для команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.")

# Хэндлер для команды /help
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Используйте команду /start для начала работы с ботом.")

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
