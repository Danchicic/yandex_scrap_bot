from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lexicon import lexicon_ru
from aiogram.filters import CommandStart, StateFilter
from keyboards.main_keyboards import Keyboard
from FSM import FSMUser
from aiogram import F

parts_router: Router = Router()
parts_router.message.filter(StateFilter(FSMUser.choose_part))


@parts_router.message()
async def send_files(message: Message, state: FSMContext):
    await  state.set_state(FSMUser.choose_lesson)
    await message.reply(text=lexicon_ru['choose_lesson'],
                        reply_markup=Keyboard(''))
