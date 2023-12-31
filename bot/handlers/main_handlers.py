from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lexicon import lexicon_ru
from keyboards.main_keyboards import Keyboard
from FSM import FSMUser
from aiogram import F

command_router: Router = Router()


# commands router file

@command_router.message(F.text == '/start')
async def hello_world(message: Message, state: FSMContext):
    await state.set_state(FSMUser.choose_course)
    await message.reply(text=lexicon_ru['hello'], reply_markup=Keyboard('courses').get_kb())


