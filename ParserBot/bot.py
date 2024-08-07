import asyncio
import logging

from aiogram import Bot, Dispatcher
import betterlogging as bl

from handlers.first_handler import start_router


async def main():
    bl.basic_colorized_config(level=logging.INFO)

    bot = Bot('6602615450:AAGHJbfktLzyxNII5NrMV3m4HQJFkbTEvH0')
    dp = Dispatcher()

    dp.include_routers(start_router)

    await dp.start_polling(bot)
    await bot.session.close()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    logging.info('Bot Stop')
