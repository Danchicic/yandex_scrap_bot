from aiogram import Router, F
from aiogram.types import CallbackQuery
from lexicon import lexicon_ru
from aiogram.filters import StateFilter
from keyboards.main_keyboards import Keyboard
from FSM import FSMUser
from config import config
from services.defs import read_tests

from .test_handler import unpack_test
from scrapper.work_with_html import get_files

quiz_router = Router()
quiz_router.message.filter(StateFilter(FSMUser.solve_test))

test = read_tests()


@quiz_router.callback_query(F.data == 'forward')
async def send_next_test(callback: CallbackQuery):
    my_test: list = test[config.paths.test_path]
    if config.db.page < len(my_test) - 1:
        config.db.page += 1
        text_for_bot, correct = unpack_test(my_test, config.db.page)

        await callback.message.edit_text(text=text_for_bot,
                                         reply_markup=Keyboard.create_inline_answers_kb(
                                             correct=correct,
                                             next_buttons=['backward',
                                                           f"{config.db.page + 1}/{len(my_test)}",
                                                           'forward']),

                                         )
    else:
        await callback.answer(text=lexicon_ru['all_tests'])
    # print("test number: ", config.db.page)


@quiz_router.callback_query(F.data == 'backward')
async def send_prev_test(callback: CallbackQuery):
    my_test: list = test[config.paths.test_path]

    if config.db.page > 0:
        config.db.page -= 1
        text_for_bot, correct = unpack_test(my_test, config.db.page)
        await callback.message.edit_text(text=text_for_bot,
                                         reply_markup=Keyboard.create_inline_answers_kb(
                                             correct=correct,
                                             next_buttons=['backward',
                                                           f"{config.db.page + 1}/{len(my_test)}",
                                                           'forward']),
                                         )

    else:
        await callback.answer(text="Вы в своём уме?")


@quiz_router.callback_query(F.data == 'True')
async def give_notification_true(callback: CallbackQuery):
    await callback.answer(text='Верно!')
    # give true notification


@quiz_router.callback_query(F.data == 'False')
async def give_notification_false(callback: CallbackQuery):
    await callback.answer(text='Неверно( 😔')
    # give false notification
