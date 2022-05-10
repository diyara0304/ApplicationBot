from loader import dp
from aiogram import types
from states.state import Advert
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=Advert.price)
async def price(message:types.Message,state:FSMContext):
    price=message.text.split()
    if price[0].isnumeric() or price[0].lower()=="tekin":
        await state.update_data(
            {'price':message.text}
        )
        await message.answer('''👨🏻‍💻 <b>Kasbi</b>: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba''',parse_mode='html')
        await Advert.next()
    else:
        await message.answer('Narxni to\'g\'ri kiriting')