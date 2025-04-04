from fastapi import FastAPI, Request
from aiogram.types import Update
from bot import get_bot_application, bot

app = FastAPI()
dp = get_bot_application()

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    if token != bot.token:
        return {"status": "unauthorized"}
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"status": "ok"}
