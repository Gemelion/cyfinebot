from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database import add_user, user_exists


async def start_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    if not user_exists(user_id):
        add_user(user_id, first_name)

    builder = InlineKeyboardBuilder()
    builder.button(text="🔎 Проверить штрафы", callback_data="check_fines")

    await message.answer(
        "👋 Добро пожаловать в CyFineBot!

"
        "Этот бот поможет вам проверить наличие штрафов по вашему автомобилю. "
        "Нажмите кнопку ниже, чтобы начать:",
        reply_markup=builder.as_markup()
    )
