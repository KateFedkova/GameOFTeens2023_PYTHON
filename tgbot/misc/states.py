from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    weeks = State()
    internet = State()
    calls = State()
    price = State()
    suitable = State()
