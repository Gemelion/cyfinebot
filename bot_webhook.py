from fastapi import FastAPI, Request
from bot import get_bot_application
from telegram import Update
import os

bot_app = get_bot_application()
app = FastAPI()

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    if token != os.getenv("BOT_TOKEN"):
        return {"status": "unauthorized"}
    update = Update.de_json(await request.json(), bot_app.bot)
    await bot_app.process_update(update)
    return {"status": "ok"}
