from aiogram.filters.state import State, StatesGroup


# user state model
class FSMUser(StatesGroup):
    choose_course = State()
    choose_part = State()
    choose_lesson = State()
    choose_page = State()
    chose_test = State()
    solve_test = State()
