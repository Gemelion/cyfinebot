
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

router = Router()

@router.message(F.command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Чем могу помочь?")
