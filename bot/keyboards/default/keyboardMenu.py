from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Kategoriyalar"),
            KeyboardButton(text="Kinolar")
        ],
        [
            KeyboardButton(text="Joylashuv", request_location=True),
        ]
    ]
)