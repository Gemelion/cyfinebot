from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.

"
        "📍Что делает бот:
"
        "— Проверяет наличие штрафов по данным вашего ARC/ID (или другого документа) и номеру автомобиля.
"
        "— Проверяет штрафы на сайте раз в сутки и при появлении новых уведомляет вас
"
        "— Не собирает лишних данных и полностью соответствует требованиям GDPR

"
        "🛡️ Все данные хранятся только на сервере, в зашифрованном виде.

"
        "❗Перед началом работы необходимо ваше согласие на обработку данных."
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Согласен", callback_data="consent_given")],
        [InlineKeyboardButton(text="❌ Не согласен", callback_data="consent_denied")]
    ])
    await message.answer(text, reply_markup=keyboard)
