
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from bot_config import BOT_TOKEN
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram import types


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Сообщение приветствия
@dp.message_handler(commands=["start"])
async def cmd_start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("✅ Согласен")
    button2 = KeyboardButton("❌ Не согласен")
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
        "❗Перед началом работы необходимо ваше согласие на обработку данных.

"
        "👉 Ниже отображаются inline-кнопки:",
        reply_markup=keyboard
    )

# Ожидаем команды
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
