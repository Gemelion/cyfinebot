import os
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEFAULT_PROPERTIES = DefaultBotProperties(parse_mode=ParseMode.HTML)
