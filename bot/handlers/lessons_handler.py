from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.main_keyboards import Keyboard
from FSM import FSMUser
from config import config

from scrapper.work_with_html import get_files

lesson_router = Router()


# lesson_router.message.filter(StateFilter(FSMUser.choose_lesson))


@lesson_router.message(FSMUser.choose_lesson)
@lesson_router.message(F.text == '/lesson')
async def send_lesson_files(message: Message, state: FSMContext):
    if message.text != "/lesson":
        config.paths.lesson_path = config.paths.part_path + message.text

    files = get_files(config.paths.lesson_path)
    # print('files', files)
    await message.answer(text='Выбери файл', reply_markup=Keyboard.create_kb_from_list(files))

    # files_path, tasks_path = get_files(path=config.paths.lesson_path)

    await state.set_state(FSMUser.chose_test)
