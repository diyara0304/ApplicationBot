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

👨‍💼 Xodim: <b>{ism}</b>
🕑 Yosh: {yosh}
📚 Texnologiya: <b>{texnologiya}</b> 
🇺🇿 Telegram: @{t_name} 
📞 Aloqa: {raqam} 
🌐 Hudud: <b>{manzil}</b> 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb} 
🕰 Murojaat qilish vaqti: {vaqt} 
🔎 Maqsad: {maqsad} 

#xodim''',parse_mode='html')
    await state.finish()
