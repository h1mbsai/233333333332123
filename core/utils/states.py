from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    age = State()
    experience = State()
    about = State()
    discord = State()
    photo = State()