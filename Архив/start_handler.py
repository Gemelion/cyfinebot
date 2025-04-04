from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database import add_user, user_exists

start_handler = Router()

@start_handler.message(CommandStart())
async def start(message: types.Message):
    user_id = message.from_user.id
    if not user_exists(user_id):
        add_user(user_id)

    kb = InlineKeyboardBuilder()
    kb.button(text="🔎 Проверить штрафы", callback_data="check_fines")
    kb.adjust(1)

    await message.answer(
        "👋 Добро пожаловать в CyFineBot!",
        reply_markup=kb.as_markup()
    )
