from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application
from bot import get_bot_application
import json
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

bot_app: Application = get_bot_application()

@app.on_event("startup")
async def startup_event():
    await bot_app.initialize()
    webhook_url = f"https://{bot_app.token}.onrender.com/webhook/{bot_app.token}"
    await bot_app.bot.set_webhook(url=webhook_url)
    logging.info("🚀 Вебхук установлен и бот запущен!")

@app.post("/webhook/{token}")
async def telegram_webhook(request: Request, token: str):
    if token != bot_app.token:
        return {"status": "unauthorized"}
    try:
        data = await request.body()
        json_data = json.loads(data.decode("utf-8"))
        update = Update.de_json(json_data, bot_app.bot)
        await bot_app.process_update(update)
    except Exception as e:
        logging.exception("❌ Ошибка при обработке вебхука: %s", e)
        return {"status": "error", "detail": str(e)}
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "CyFineBot is live"}
