
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database import add_user_if_not_exists

from aiogram.handlers import MessageHandler
from aiogram.fsm.context import FSMContext

start_handler = MessageHandler(
    lambda msg: msg.text == "/start",
    lambda message, state: handle_start(message, state),
)


async def handle_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username or ""

    # Добавляем пользователя в базу, если его нет
    add_user_if_not_exists(user_id, full_name, username)

    builder = InlineKeyboardBuilder()
    builder.button(text="🔎 Проверить штрафы", callback_data="check_fines")

    await message.answer(
        "👋 Добро пожаловать в CyFineBot!
Пожалуйста, нажмите кнопку ниже.",
        reply_markup=builder.as_markup()
    )
