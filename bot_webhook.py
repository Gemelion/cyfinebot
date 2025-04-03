from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application
from bot import get_bot_application
import os

app = FastAPI()
bot_app: Application = get_bot_application(os.getenv("BOT_TOKEN"))

@app.post("/webhook/{token}")
async def telegram_webhook(request: Request, token: str):
    if token != os.getenv("BOT_TOKEN"):
        return {"error": "Unauthorized"}

    data = await request.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"ok": True}