from aiogram import Bot, Dispatcher, types
import logging
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_TOKEN = os.getenv("API_TOKEN")  # Getting the API token from environment variables

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# Command /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("✅ Согласен")
    button2 = types.KeyboardButton("❌ Не согласен")
    keyboard.add(button, button2)
    await message.answer(
        "👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.
"
        "📍 Что делает бот:
"
        "— Проверяет наличие штрафов по данным вашего ARC/ID (или другого документа) и номеру автомобиля.
"
        "— Проверяет штрафы на сайте раз в сутки и при появлении новых штрафов уведомляет вас.
"
        "— Не собирает лишних данных и полностью соответствует требованиям GDPR.
"
        "🛡️ Все данные хранятся только на сервере, в зашифрованном виде.

"
        "❗Перед началом работы необходимо ваше согласие на обработку данных.

"
        "👉 Ниже отображаются inline-кнопки:
"
        "• ✅ Согласен
"
        "• ❌ Не согласен",
        reply_markup=keyboard,
    )