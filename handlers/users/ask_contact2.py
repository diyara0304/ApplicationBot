from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext
from keyboards.default.ask_contact import contact_b

@dp.message_handler(state=Mentor.skills)
async def ask_skill(message:types.Message,state:FSMContext):
    skill=message.text
    await state.update_data(
        {'skill':skill}
    )
    await message.answer('''📞 <b>Aloqa</b>: 

Bog`lanish uchun raqamingizni jo'nating.''',parse_mode='html',reply_markup=contact_b)