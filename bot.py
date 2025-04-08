
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from bot_config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton("Option 1")
    button_2 = KeyboardButton("Option 2")
    keyboard.add(button_1, button_2)

    await message.answer("Привет! Чем я могу помочь?", reply_markup=keyboard)

if __name__ == "__main__":
    from aiogram import executor
    asyncio.run(dp.start_polling())
