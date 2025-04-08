
from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram import F

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    # Создаем клавиатуру с одной кнопкой
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Нажми меня")
    keyboard.add(button)

    # Отправляем сообщение с кнопкой
    await message.answer("Привет! Чем могу помочь?", reply_markup=keyboard)
