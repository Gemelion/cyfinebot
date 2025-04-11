from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Токен бота
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply(
        "👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.\n\n"
        "📍Что делает бот:\n"
        "— Проверяет наличие штрафов по данным вашего ARC/ID (или другого документа) и номеру автомобиля.\n"
        "— Проверяет штрафы на сайте раз в сутки и при появлении новых штрафов уведомляет вас.\n"
        "— Не собирает лишних данных и полностью соответствует требованиям GDPR.\n\n"
        "🛡️ Все данные хранятся только на сервере, в зашифрованном виде.\n\n"
        "❗Перед началом работы необходимо ваше согласие на обработку данных.\n\n"
        "👉 Ниже отображаются inline-кнопки:\n"
        "• ✅ Согласен\n"
        "• ❌ Не согласен"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
