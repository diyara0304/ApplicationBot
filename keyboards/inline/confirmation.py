from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

confirmation=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Ha',callback_data='true'),InlineKeyboardButton(text='❌ Yo\'q',callback_data='false')]
    ]
)