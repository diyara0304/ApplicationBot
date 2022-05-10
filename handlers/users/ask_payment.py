from loader import dp
from states.state import Advert
from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=Advert.address)    
async def location(message:types.Message,state:FSMContext):
    location=message.text
    await message.answer('''💰 <b>Narxi</b>:

To'lov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?''',parse_mode='html')
    await state.update_data(
        {'address':location}
    )
    await Advert.next()