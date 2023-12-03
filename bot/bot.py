import asyncio
import logging
from aiogram import Bot, Dispatcher
import handlers
from config import config
from keyboards.main_menu import set_main_menu

# main file of bot


# CONFIG!!!
token = config.tg_bot.token

# logger initializing
logger = logging.getLogger(__name__)


# configuration and turn on bot
async def main():
    # configurate logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=token,
                   parse_mode='HTML'
                   )

    dp: Dispatcher = Dispatcher()
    dp.include_router(handlers.router_main)
    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
