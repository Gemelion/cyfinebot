from aiogram import Router, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

WELCOME_TEXT = (
    "👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.\n\n"
    "📍Что делает бот:\n"
    "— Проверяет наличие штрафов по данным вашего ARC/ID (или другого документа) и номеру автомобиля.\n"
    "— Проверяет штрафы на сайте раз в сутки и при появлении новых штрафов уведомляет вас\n"
    "— Не собирает лишних данных и полностью соответствует требованиям GDPR\n\n"
    "🛡️ Все данные хранятся только на сервере, в зашифрованном виде.\n\n"
    "❗Перед началом работы необходимо ваше согласие на обработку данных."
)

@router.message(commands=["start"])
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Согласен", callback_data="consent_yes")],
        [InlineKeyboardButton(text="❌ Не согласен", callback_data="consent_no")]
    ])
    await message.answer(WELCOME_TEXT, reply_markup=keyboard)