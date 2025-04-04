from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Router, F
from aiogram.filters import CommandStart
from database import add_user
from aiogram.types import CallbackQuery

start_handler = Router()

@start_handler.message(CommandStart())
async def start_command_handler(message: Message):
    add_user(message.from_user.id)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Проверить штрафы", callback_data="check_fines")],
        [InlineKeyboardButton(text="GDPR & Контакт", callback_data="gdpr_contact")]
    ])

    await message.answer(
        text="👋 Добро пожаловать в CyFineBot!",
        reply_markup=keyboard
    )

@start_handler.callback_query(F.data == "check_fines")
async def check_fines_callback(callback_query: CallbackQuery):
    await callback_query.message.answer("Пожалуйста, введите ваш ARC/ID и номер автомобиля для проверки штрафов.")

@start_handler.callback_query(F.data == "gdpr_contact")
async def gdpr_contact_callback(callback_query: CallbackQuery):
    await callback_query.message.answer("Информация о GDPR и возможность связаться с администратором.")
