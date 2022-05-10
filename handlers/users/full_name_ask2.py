from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=Mentor.fullname)
async def name2(message:types.Message,state: FSMContext):
    name=message.text
    await state.update_data(
        {'name':name}
    )
    await message.answer('''🕑 <b>Yosh</b>: 

Yoshingizni kiriting?
Masalan, 19''',parse_mode='html')
    await Mentor.next()
