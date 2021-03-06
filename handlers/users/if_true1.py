from loader import dp,bot
from states.state import Advert
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu1 import menu

@dp.callback_query_handler(text='true',state=Advert.confirm)
async def send_admin(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer('Adminga jo\'natildi',reply_markup=menu)
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
    t_name=data.get('username')
    await bot.send_message('1451606931',f'''Ish joyi kerak:

π¨βπΌ Xodim: <b>{ism}</b>
π Yosh: {yosh}
π Texnologiya: <b>{texnologiya}</b> 
πΊπΏ Telegram: @{t_name} 
π Aloqa: {raqam} 
π Hudud: <b>{manzil}</b> 
π° Narxi: {narx} 
π¨π»βπ» Kasbi: {kasb} 
π° Murojaat qilish vaqti: {vaqt} 
π Maqsad: {maqsad} 

#xodim''',parse_mode='html')
    await state.finish()
