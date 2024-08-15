from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainButtons = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Register", callback_data="register"),
        ],
        [
            InlineKeyboardButton(text="Login", callback_data="login"),
        ],
    ]
)