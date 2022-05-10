from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove 

@dp.message_handler(content_types=['contact'],state=Mentor.skills)    
async def get_contact(message:types.Message,state:FSMContext):
    number=message.contact['phone_number']
    await state.update_data(
        {'phone':number}
    )
    await message.answer('''🌐 <b>Hudud</b>: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.''',parse_mode='html',reply_markup=ReplyKeyboardRemove())
    await Mentor.address.set()