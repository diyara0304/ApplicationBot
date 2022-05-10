from aiogram.dispatcher.filters.state import StatesGroup,State

class Advert(StatesGroup):
    fullname=State()
    age=State()
    skills=State()
    contact=State()
    address=State()
    price=State()
    profession=State()
    time=State()
    aim=State()
    confirm=State()


class Mentor(StatesGroup):
    fullname=State()
    age=State()
    skills=State()
    contact=State()
    address=State()
    price=State()
    profession=State()
    time=State()
    aim=State()
    confirm=State()


