
# Пример исправленного кода

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.")

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
