from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application
from bot import bot  # Удалён get_bot_application

app = FastAPI()
bot_app = Application.builder().token(bot.token).build()


@app.post("/webhook/{token}")
async def telegram_webhook(request: Request, token: str):
    if token != bot.token:
        return {"error": "Invalid token"}
    update = Update.de_json(await request.json(), bot)
    await bot_app.initialize()
    await bot_app.process_update(update)
    return {"ok": True}