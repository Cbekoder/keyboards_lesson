from aiogram.fsm.state import State, StatesGroup


class RegisterForm(StatesGroup):
    name = State()
    email = State()
    phone = State()
    address = State()