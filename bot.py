
import logging
import sqlite3
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters, ConversationHandler
from encryption import encrypt, decrypt
from fines import check_fines
import os
import asyncio
import sys

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = "db.sqlite3"

DOC_TYPE, ID_NUMBER, CAR_NUMBER = range(3)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

DOCUMENT_TYPES = ["ID Card", "Passport", "ARC", "Driving Licence"]

MAIN_MENU = ReplyKeyboardMarkup([
    ["/check"],
    ["/view", "/delete"]
], resize_keyboard=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            doc_type TEXT,
            encrypted_id TEXT,
            encrypted_car TEXT,
            consent_given INTEGER,
            had_fines INTEGER DEFAULT 0
        )""")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я бот, который поможет тебе отслеживать штрафы с камер на Кипре.\n\n"
        "🔐 Все данные хранятся в зашифрованном виде и обрабатываются в строгом соответствии с GDPR.\n\n"
        "Нажми /consent, чтобы дать согласие на обработку персональных данных.\n"
        "Нажми /delete, чтобы удалить свои данные.",
        reply_markup=MAIN_MENU
    )

async def consent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT OR REPLACE INTO users (user_id, consent_given) VALUES (?, 1)", (user_id,))
    await update.message.reply_text("✅ Спасибо! Теперь введите команду /register, чтобы добавить свои данные.", reply_markup=MAIN_MENU)

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton(t)] for t in DOCUMENT_TYPES]
    await update.message.reply_text(
        "🪪 Пожалуйста, выберите тип документа:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return DOC_TYPE

async def doc_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['doc_type'] = update.message.text.strip()
    await update.message.reply_text("✏️ Введите номер документа:")
    return ID_NUMBER

async def id_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['id_number'] = update.message.text.strip()
    await update.message.reply_text("🚗 Теперь введите номер автомобиля:")
    return CAR_NUMBER

async def car_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    car = update.message.text.strip()
    id_number = context.user_data['id_number']
    doc_type = context.user_data['doc_type']

    encrypted_id = encrypt(id_number)
    encrypted_car = encrypt(car)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("UPDATE users SET doc_type=?, encrypted_id=?, encrypted_car=? WHERE user_id=?",
                     (doc_type, encrypted_id, encrypted_car, user_id))

    await update.message.reply_text("✅ Данные сохранены! Используйте /check чтобы проверить наличие штрафов.", reply_markup=MAIN_MENU)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Действие отменено.", reply_markup=MAIN_MENU)
    return ConversationHandler.END

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT doc_type, encrypted_id, encrypted_car FROM users WHERE user_id=?", (user_id,))
        row = cursor.fetchone()
        if not row:
            await update.message.reply_text("⚠️ Данные не найдены. Пожалуйста, сначала зарегистрируйтесь с помощью /register.", reply_markup=MAIN_MENU)
            return
        doc_type = row[0]
        decrypted_id = decrypt(row[1])
        decrypted_car = decrypt(row[2])

    fines = check_fines(decrypted_id, decrypted_car, doc_type)
    if fines:
        await update.message.reply_text(f"🚨 Обнаружено {len(fines)} штрафов! Перейдите на сайт для подробностей.", reply_markup=MAIN_MENU)
    else:
        await update.message.reply_text("✅ Штрафов не найдено.", reply_markup=MAIN_MENU)

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM users WHERE user_id=?", (user_id,))
    await update.message.reply_text("🗑️ Ваши данные удалены. Вы всегда можете начать заново с /start.", reply_markup=MAIN_MENU)

async def view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT doc_type, encrypted_id, encrypted_car FROM users WHERE user_id=?", (user_id,))
        row = cursor.fetchone()
        if not row:
            await update.message.reply_text("⚠️ Данные не найдены. Пожалуйста, сначала зарегистрируйтесь.", reply_markup=MAIN_MENU)
            return
    doc_type = row[0]
    decrypted_id = decrypt(row[1])
    decrypted_car = decrypt(row[2])

    await update.message.reply_text(
        f"📄 Ваши данные:\nТип документа: {doc_type}\nНомер документа: {decrypted_id}\nНомер авто: {decrypted_car}",
        reply_markup=MAIN_MENU
    )

async def daily_check(app):
    while True:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT user_id, doc_type, encrypted_id, encrypted_car, had_fines FROM users WHERE consent_given=1")
            rows = cursor.fetchall()

        for user_id, doc_type, encrypted_id, encrypted_car, had_fines in rows:
            id_number = decrypt(encrypted_id)
            car_number = decrypt(encrypted_car)

            fines = check_fines(id_number, car_number, doc_type)
            has_now = 1 if fines else 0

            if has_now and not had_fines:
                try:
                    await app.bot.send_message(
                        chat_id=user_id,
                        text="🚨 Обнаружен новый штраф! Перейдите на https://cycamerasystem.com.cy/Login для проверки."
                    )
                except Exception as e:
                    logger.error(f"Ошибка отправки сообщения пользователю {user_id}: {e}")

            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("UPDATE users SET had_fines=? WHERE user_id=?", (has_now, user_id))

        await asyncio.sleep(86400)

if __name__ == '__main__':
    if os.environ.get("BOT_RUNNING") == "1":
        logger.error("❌ Уже запущен другой экземпляр бота. Завершаем работу.")
        sys.exit(1)

    os.environ["BOT_RUNNING"] = "1"
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("register", register)],
        states={
            DOC_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, doc_type)],
            ID_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, id_number)],
            CAR_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, car_number)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("consent", consent))
    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("check", check))
    app.add_handler(CommandHandler("delete", delete))
    app.add_handler(CommandHandler("view", view))

    app.job_queue.run_once(lambda ctx: asyncio.create_task(daily_check(app)), when=5)
    app.run_polling()
