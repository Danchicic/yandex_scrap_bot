from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lexicon import lexicon_ru
from keyboards.main_keyboards import Keyboard
from FSM import FSMUser
from config import config
from services.defs import read_tests, create_text_for_bot, dict_indexing

test_router = Router()
# test_router.message.filter(StateFilter(FSMUser.chose_test))
tests = read_tests()


@create_text_for_bot
def unpack_test(test, needed_test):  # -> tuple[str, tuple[str], list[bool]]
    print(needed_test)
    question, test = dict_indexing(test, needed_test - 1)
    answers, correct = list(test.items())[0]
    return question, answers, correct


@test_router.message(FSMUser.chose_test)
@test_router.message(F.text == '/test')
async def send_test(message: Message, state: FSMContext):
    if message.text != "/test":
        config.paths.test_path = config.paths.lesson_path + '/' + message.text
    test = tests[config.paths.test_path]
    text_for_bot, correct = unpack_test(test, config.db.page)

    if len(test) > 1:
        await message.answer(text=text_for_bot,
                             reply_markup=Keyboard.create_inline_answers_kb(
                                 correct, next_buttons=['backward', f"{config.db.page + 1}/{len(test)}", 'forward']),

                             )
    elif len(test) == 1:
        await message.answer(text=text_for_bot,
                             reply_markup=Keyboard.create_inline_answers_kb(correct),
                             )
    else:
        await message.answer(text=lexicon_ru['test_not_founded'])

    await state.set_state(FSMUser.solve_test)
