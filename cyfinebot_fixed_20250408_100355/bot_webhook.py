import os
from fastapi import FastAPI, Request
from aiogram.types import Update
from bot import bot, dp

app = FastAPI()

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    json_data = await request.json()
    update = Update(**json_data)
    await dp.feed_update(bot, update)
    return {"ok": True}
