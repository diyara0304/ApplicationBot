from loader import dp
from aiogram import types
from states.state import Advert
from aiogram.types import ReplyKeyboardRemove 

@dp.message_handler(text='Ish joyi kerak')
async def job_start(message:types.Message):
    await message.answer('<b>Ish joyi topish uchun ariza berish</b>\n\nHozir sizga bir necha savollar beriladi. Har biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, "HA" tugmasini bosing va arizangiz Adminga yuboriladi.',parse_mode='html',reply_markup=ReplyKeyboardRemove())
    await message.answer('<b>Ism-familiyangizni</b> kiriting.',parse_mode='html')
    await Advert.fullname.set()