from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ish joyi kerak'),KeyboardButton(text='Ustoz kerak')]
    ],resize_keyboard=True,one_time_keyboard=True
)