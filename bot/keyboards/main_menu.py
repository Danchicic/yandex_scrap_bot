from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='comps', description='Выбрать курс'),
        BotCommand(command='parts', description='Изменить ВУЗ'),

    ]
    await bot.set_my_commands(main_menu_commands)
