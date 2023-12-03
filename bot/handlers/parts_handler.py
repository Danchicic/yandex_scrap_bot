from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lexicon import lexicon_ru
from keyboards.main_keyboards import Keyboard
from FSM import FSMUser

from config import config

parts_router: Router = Router()


# parts_router.message.filter(StateFilter(FSMUser.choose_part))


# file for lessons, to parts
@parts_router.message(F.text == '/part')
@parts_router.message(FSMUser.choose_part)
async def send_files(message: Message, state: FSMContext):
    if message.text != "/part":
        config.paths.part_path = config.paths.course_path + message.text + '/'

    # print(config.paths.part_path)

    await state.set_state(FSMUser.choose_lesson)
    await message.answer(text=lexicon_ru['choose_lesson'],
                         reply_markup=Keyboard('directory').get_kb(config.paths.part_path))
