from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user, user_exists
from datetime import datetime

welcome_text = (
    "👋 Добро пожаловать в CyFineBot — ваш помощник по проверке автомобильных штрафов с камер на Кипре.\n\n"
    "📍Что делает бот:\n"
    "— Проверяет наличие штрафов по данным вашего ARC/ID (или другого документа) и номеру автомобиля.\n"
    "— Проверяет штрафы на сайте раз в сутки и при появлении новых уведомляет вас\n"
    "— Не собирает лишних данных и полностью соответствует требованиям GDPR\n\n"
    "🛡️ Все данные хранятся только на сервере, в зашифрованном виде.\n\n"
    "❗Перед началом работы необходимо ваше согласие на обработку данных."
)

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Согласен", callback_data="consent_yes")],
    [InlineKeyboardButton(text="❌ Не согласен", callback_data="consent_no")]
])

async def start_handler(message: types.Message, state: FSMContext):
    if await user_exists(message.from_user.id):
        await message.answer("Вы уже дали согласие. Для проверки штрафов нажмите /check.")
        return
    await message.answer(welcome_text, reply_markup=keyboard)

async def consent_callback_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "consent_yes":
        await add_user(
            user_id=callback.from_user.id,
            username=callback.from_user.username,
            first_name=callback.from_user.first_name,
            consent_date=datetime.utcnow()
        )
        await callback.message.edit_text("✅ Спасибо! Теперь можете ввести свои данные для проверки штрафов. Нажмите /check.")
    elif callback.data == "consent_no":
        await callback.message.edit_text("❌ Без согласия бот не может работать. До свидания.")
