from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lexicon import lexicon_ru
from aiogram.filters import CommandStart, StateFilter
from keyboards.main_keyboards import Keyboard
from FSM import FSMUser

course_router = Router()

course_router.message.filter(StateFilter(FSMUser.choose_course))
path_zero = '/Users/danya/Desktop/курсы/'


@course_router.message()
async def send_parts(message: Message, state: FSMContext):
    await state.set_state(FSMUser.choose_part)
    await message.answer(text=lexicon_ru['choose_part'],
                         reply_markup=Keyboard('parts').get_kb(path_zero + message.text)
                         )
