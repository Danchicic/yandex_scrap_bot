from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from lexicon import lexicon_ru
from aiogram.filters import StateFilter
from keyboards.main_keyboards import Keyboard
from FSM import FSMUser
from config import config

from scrapper.work_with_html import get_files, delete_answers

lesson_router = Router()
lesson_router.message.filter(StateFilter(FSMUser.choose_lesson))


@lesson_router.message()
async def send_lesson_files(message: Message, state: FSMContext):
    """
    send quiz file
    set state task if tasks == 1

    :param message:
    :param state:
    :return:
    """

    config.paths.lesson_path = config.paths.part_path + message.text
    print(config.paths.lesson_path)
    files_path, tasks_path = get_files(path=config.paths.lesson_path)
    delete_answers(files_path)
    for pages_path in files_path:
        await message.reply_document(FSInputFile(pages_path))

    if tasks_path:
        pass
    # send htmls files
    # await message.answer()
    pass
