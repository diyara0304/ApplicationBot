from loader import dp
from aiogram import types
from states.state import Advert
from aiogram.dispatcher import FSMContext
from keyboards.inline.confirmation import confirmation


@dp.message_handler(state=Advert.aim)
async def aim(message:types.Message,state:FSMContext):
    username=message.from_user.username
    await state.update_data(
        {'username':username}
    )
    aim=message.text

    await state.update_data(
        {'aim':aim}
    ) 
    data=await state.get_data()
    ism=data.get('name')
    yosh=data.get('age')
    texnologiya=data.get('skill')
    raqam=data.get('phone')
    manzil=data.get('address')
    narx=data.get('price')
    kasb=data.get('profession')
    vaqt=data.get('time')
    maqsad=data.get('aim')
    await message.answer(f'''Ish joyi kerak:

👨‍💼 Xodim: <b>{ism}</b>
🕑 Yosh: {yosh}
📚 Texnologiya: <b>{texnologiya}</b> 
🇺🇿 Telegram: @{username} 
📞 Aloqa: {raqam} 
🌐 Hudud: <b>{manzil}</b> 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb} 
🕰 Murojaat qilish vaqti: {vaqt} 
🔎 Maqsad: {maqsad} 

#xodim''',parse_mode='html')
    await message.answer('Ma\'lumotlarni tasdiqlaysizmi?',reply_markup=confirmation)    
    await Advert.next()