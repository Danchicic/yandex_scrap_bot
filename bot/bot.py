import asyncio
import logging
from aiogram import Bot, Dispatcher
import handlers

token = '6639949950:AAHpARLzvHi2ifbZn54DyEzep2A_fYZPgns'
# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=token,
                   )

    dp: Dispatcher = Dispatcher()
    dp.include_router(handlers.router_main)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())