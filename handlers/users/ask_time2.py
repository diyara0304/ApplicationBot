from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=Mentor.profession)
async def prof(message:types.Message,state:FSMContext):
    profession=message.text
    await state.update_data(
        {'profession':profession}
    )
    await message.answer('''🕰 <b>Murojaat qilish vaqti</b>: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00''',parse_mode='html')
    await Mentor.next()
