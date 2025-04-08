
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import logging
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Stage 1 - Greeting and description
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    agree_button = KeyboardButton("✅ Согласен")
    disagree_button = KeyboardButton("❌ Не согласен")
    markup.add(agree_button, disagree_button)
    await message.answer(
        "👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.
"
        "📍Что делает бот:
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
        "Нажмите одну из кнопок ниже, чтобы продолжить.",
        reply_markup=markup)

# Stage 2 - User consent (GDPR)
@dp.message_handler(lambda message: message.text == "✅ Согласен")
async def user_agreement(message: types.Message):
    # Here, we would store user's consent in a database
    await message.answer("Ваше согласие получено! Пожалуйста, выберите тип документа для проверки штрафов.")
    # Redirect to the next stage (document input)
    await choose_document_type(message)

@dp.message_handler(lambda message: message.text == "❌ Не согласен")
async def no_agreement(message: types.Message):
    await message.answer("Без согласия на обработку данных бот не может работать. Вы можете вернуться к началу в любой момент.")
    await message.answer("Завершаем диалог.")
    await message.bot.close()

# Stage 3 - Request for document type and number
async def choose_document_type(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    document_buttons = [
        KeyboardButton("ARC Number"),
        KeyboardButton("Alien Book"),
        KeyboardButton("Passport"),
        KeyboardButton("Identity Card"),
        KeyboardButton("Cyprus Residence Permit")
    ]
    markup.add(*document_buttons)
    await message.answer("Пожалуйста, выберите тип документа.", reply_markup=markup)

# Start bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
