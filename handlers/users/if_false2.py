from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext
from keyboards.default.menu1 import menu


@dp.callback_query_handler(state=Mentor.confirm,text='false')
async def delete_text(call:types.callback_query,state:FSMContext):
    await call.answer('Bekor qilindi!')
    await call.message.delete()
    await call.message.answer('Asosiy menyudasiz',reply_markup=menu)
    await state.finish()