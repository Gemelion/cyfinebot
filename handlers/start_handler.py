
from aiogram import Bot, types
from aiogram.fsm import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram import Dispatcher  # Нужно заменить этот импорт

from bot_config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

# Новый импорт
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher import AiogramDispatcher

# Настройка диспетчера для 3.x
dp = AiogramDispatcher(bot)

# Далее идет код для работы с командами
