from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=Mentor.address)    
async def location(message:types.Message,state:FSMContext):
    location=message.text
    await message.answer('''💰 <b>Narxi</b>:

To'lov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?''',parse_mode='html')
    await state.update_data(
        {'address':location}
    )
    await Mentor.next()
