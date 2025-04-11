
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Загрузка токена из переменной окружения
API_TOKEN = os.getenv("API_TOKEN")

if API_TOKEN is None:
    raise ValueError("API_TOKEN is not set in the environment variables!")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('✅ Согласен')
    button2 = KeyboardButton('❌ Не согласен')
    keyboard.add(button1, button2)
    
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
        "❗Перед началом работы необходимо ваше согласие на обработку данных.",
        reply_markup=keyboard
    )

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
