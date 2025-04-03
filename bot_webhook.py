import os
from fastapi import FastAPI
from bot import get_bot_application

app = FastAPI()
bot_app = get_bot_application(os.getenv("BOT_TOKEN"))

@app.on_event("startup")
async def on_startup():
    await bot_app.initialize()
    await bot_app.start()

@app.on_event("shutdown")
async def on_shutdown():
    await bot_app.stop()
