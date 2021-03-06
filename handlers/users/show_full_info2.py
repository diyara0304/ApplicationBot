from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext
from keyboards.inline.confirmation import confirmation


@dp.message_handler(state=Mentor.aim)
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
    await message.answer(f'''Ustoz kerak:

π¨βπΌ Shogird: <b>{ism}</b>
π Yosh: {yosh}
π Texnologiya: <b>{texnologiya}</b> 
πΊπΏ Telegram: @{username} 
π Aloqa: {raqam} 
π Hudud: <b>{manzil}</b> 
π° Narxi: {narx} 
π¨π»βπ» Kasbi: {kasb} 
π° Murojaat qilish vaqti: {vaqt} 
π Maqsad: {maqsad} 

#shogird''',parse_mode='html')
    await message.answer('Ma\'lumotlarni tasdiqlaysizmi?',reply_markup=confirmation)    
    await Mentor.next()
