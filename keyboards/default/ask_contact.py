from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

contact_b=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telefon raqamni jo\'natish',request_contact=True)]        
    ],resize_keyboard=True,
)
