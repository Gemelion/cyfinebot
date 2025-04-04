from fastapi import FastAPI, Request
from telegram import Update
from bot import get_bot_application
import os

app = FastAPI()

bot_app = get_bot_application(os.getenv("BOT_TOKEN"))

@app.on_event("startup")
async def startup_event():
    await bot_app.initialize()

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    data = await request.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"ok": True}
