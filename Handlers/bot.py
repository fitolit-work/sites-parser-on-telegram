import asyncio
from aiogram import Bot, Dispatcher


async def main():
    bot = Bot('')
    dp = Dispatcher()

    await dp.start_polling(bot)
    await bot.session.close()


asyncio.run(main())
