from aiogram import Router, F, Bot
from aiogram.types import Message

start_router = Router()


@start_router.message(F.text)
async def echo_handler(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, message.text)
