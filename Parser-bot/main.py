from aiogram import Bot, Dispatcher, F
from aiogram.types import Message


async def echo_handler(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, message.text)


