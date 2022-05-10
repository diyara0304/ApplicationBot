from loader import dp
from states.state import Mentor
from aiogram import types
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(text='Ustoz kerak')
async def job_start2(message:types.Message):
    await message.answer('<b>Ustoz topish uchun ariza berish</b>\n\nHozir sizga bir necha savollar beriladi. Har biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, "HA" tugmasini bosing va arizangiz Adminga yuboriladi.',parse_mode='html',reply_markup=ReplyKeyboardRemove())
    await message.answer('<b>Ism-familiyangizni</b> kiriting.',parse_mode='html')
    await Mentor.fullname.set()
