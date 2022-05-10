from loader import dp
from states.state import Advert
from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=Advert.fullname)
async def name(message:types.Message,state: FSMContext):
    name=message.text
    await state.update_data(
        {'name':name}
    )
    await message.answer('''🕑 <b>Yosh</b>: 

Yoshingizni kiriting?
Masalan, 19''',parse_mode='html')
    await Advert.next()