from fastapi import FastAPI, Request
from aiogram.types import Update
from bot import bot, dp

app = FastAPI()

@app.post("/webhook/{token}")
async def webhook(token: str, request: Request):
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"ok": True}
