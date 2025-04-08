
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher

async def cmd_start(message: types.Message):
    # Создаем кнопки
    button1 = KeyboardButton("Проверить штрафы")
    button2 = KeyboardButton("Мои данные")
    button3 = KeyboardButton("Удалить мои данные")

    # Создаем клавиатуру
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button1, button2, button3)

    # Отправляем сообщение с клавиатурой
    await message.answer("Привет! Чем я могу помочь?", reply_markup=keyboard)
