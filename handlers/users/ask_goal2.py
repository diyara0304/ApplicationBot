from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=Mentor.time)
async def time(message:types.Message,state:FSMContext):
    time=message.text
    await state.update_data(
        {'time':time}
    )    
    await message.answer('''🔎 <b>Maqsad</b>: 

Maqsadingizni qisqacha yozib bering.''',parse_mode='html')
    await Mentor.next()