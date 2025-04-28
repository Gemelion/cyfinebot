
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode  # Corrected import for ParseMode
import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("API_TOKEN")  # Make sure your API token is set in the environment variables

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

logging.basicConfig(level=logging.INFO)

# Command handler for /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.")

# Command handler for /help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Этот бот помогает проверять штрафы по номеру автомобиля.")

# Main entry point
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
