from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lexicon import lexicon_ru
from aiogram.filters import StateFilter
from keyboards.main_keyboards import Keyboard
from FSM import FSMUser
from config import config

course_router = Router()

course_router.message.filter(StateFilter(FSMUser.choose_course))


# choose the part of course
@course_router.message()
async def send_parts(message: Message, state: FSMContext):
    config.paths.course_path = config.paths.path_zero + message.text + '/'

    await state.set_state(FSMUser.choose_part)
    await message.answer(text=lexicon_ru['choose_part'],
                         reply_markup=Keyboard('directory').get_kb(config.paths.course_path),
                         )
