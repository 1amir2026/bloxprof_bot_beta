from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔗 لینک رفرال")],
        [KeyboardButton(text="👤 مشخصات من")]
    ],
    resize_keyboard=True
)