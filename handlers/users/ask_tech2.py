from loader import dp
from aiogram import types
from states.state import Mentor
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=Mentor.age)
async def age(message:types.Message,state:FSMContext):
    try:
        age=int(message.text)
        if age>0 and age<150:
            await state.update_data(
                {'age':age}
            )
            await message.answer('''📚 <b>Texnologiya</b>:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#''',parse_mode='html')
            await Mentor.next()
        else:
            await message.answer('Yoshni to\'g\'ri kiriting')    
    except: 
        await message.answer("Yoshni to'g'ri kiriting") 
