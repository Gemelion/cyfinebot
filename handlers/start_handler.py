
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router(name="start")

# Приветствие и согласие на обработку данных
@router.message(F.text == "/start")
async def start_handler(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Согласен", callback_data="consent_yes")
    builder.button(text="❌ Не согласен", callback_data="consent_no")
    await message.answer(
        "👋 Добро пожаловать в CyFineBot!

"
        "Я помогу вам проверить наличие штрафов по дорожному движению на Кипре. "
        "Для этого мне потребуется номер ARC/ID и номер автомобиля.

"
        "⚠️ Важно: мы соблюдаем GDPR. Все ваши данные будут зашифрованы и удалены по вашему запросу.

"
        "Вы даёте согласие на обработку персональных данных?",
        reply_markup=builder.as_markup()
    )

@router.callback_query(F.data == "consent_yes")
async def consent_yes(callback: CallbackQuery):
    await callback.message.edit_text(
        "✅ Спасибо за согласие!

"
        "Теперь отправьте ваш ID (ARC/ID) и номер автомобиля в формате:

"
        "`ID: X123456`\n`Car: KAA123`

"
        "Например:
`ID: A234567`\n`Car: ABC456`

"
        "Как только вы это сделаете, я начну отслеживать ваши штрафы.",
        parse_mode="Markdown"
    )

@router.callback_query(F.data == "consent_no")
async def consent_no(callback: CallbackQuery):
    await callback.message.edit_text("❌ Без согласия на обработку данных бот не может работать. Всего доброго!")
