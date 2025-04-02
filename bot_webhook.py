import os
import logging
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, ApplicationBuilder
from bot_register import register_handlers

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
register_handlers(bot_app)

# Инициализация FastAPI
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await bot_app.initialize()
    webhook_url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/webhook/{BOT_TOKEN}"
    await bot_app.bot.set_webhook(url=webhook_url)
    logging.info("🚀 Вебхук установлен и бот запущен!")

@app.post("/webhook/{token}")
async def telegram_webhook(request: Request, token: str):
    if token != BOT_TOKEN:
        return {"error": "Invalid token"}
    data = await request.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"status": "ok"}