import sqlite3
import os
from cryptography.fernet import Fernet
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, ContextTypes, filters

# Этапы диалога
TYPE, ID, PLATE = range(3)

# Ключ шифрования
FERNET_KEY = os.getenv("FERNET_KEY").encode()
fernet = Fernet(FERNET_KEY)

# Подключение к базе
DB_FILE = "users.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    document_type TEXT,
    document_id TEXT,
    plate_number TEXT
)
""")
conn.commit()

# Команда /register
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ID Card", "Passport"]]
    await update.message.reply_text(
        "Выберите тип документа:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return TYPE

async def receive_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["doc_type"] = update.message.text
    await update.message.reply_text("Введите номер документа:", reply_markup=ReplyKeyboardRemove())
    return ID

async def receive_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["doc_id"] = update.message.text
    await update.message.reply_text("Введите номер автомобиля:")
    return PLATE

async def receive_plate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    doc_type = context.user_data["doc_type"]
    doc_id = fernet.encrypt(context.user_data["doc_id"].encode()).decode()
    plate = fernet.encrypt(update.message.text.encode()).decode()

    cur.execute("REPLACE INTO users (user_id, document_type, document_id, plate_number) VALUES (?, ?, ?, ?)",
                (user_id, doc_type, doc_id, plate))
    conn.commit()

    await update.message.reply_text("✅ Данные сохранены.")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Регистрация отменена.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def register_handlers(app):
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("register", register)],
        states={
            TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_type)],
            ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_id)],
            PLATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_plate)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)