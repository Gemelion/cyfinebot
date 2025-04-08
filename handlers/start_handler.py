
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Function to handle the command start
async def cmd_start(message: types.Message):
    # Send greeting and ask for GDPR consent
    await send_welcome(message)
