from fastapi import FastAPI, Request
from telegram import Update
from bot import get_bot_application

app = FastAPI()
bot_app = get_bot_application()

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    update_data = await request.json()
    update = Update.de_json(update_data, bot_app.bot)
    await bot_app.initialize()
    await bot_app.process_update(update)
    return {"ok": True}