
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Bot token and other settings (example)
API_TOKEN = 'your-bot-token'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_start(message: Message):
    await message.answer("👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.")

# Here the string literal was terminated properly
