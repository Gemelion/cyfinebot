
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Включаем логирование, чтобы видеть ошибки и информационные сообщения
logging.basicConfig(level=logging.INFO)

# Пример команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.

Чтобы начать, пожалуйста, подтвердите согласие на обработку ваших данных.")

# Обработчик согласия на обработку данных
@dp.message_handler(commands=['agree'])
async def cmd_agree(message: types.Message):
    await message.reply("Спасибо за согласие на обработку данных. Пожалуйста, введите ваш тип документа и номер автомобиля.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
