
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(filters.Command("start"))
async def start(message: Message):
    await message.answer("Привет! Как я могу помочь?")
