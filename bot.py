import asyncio
import sys
import logging
from keyboard import keyboard_new
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart, Command
from weather_requests import TOKEN
from handlers import bot_functionality
from middleware import SomeMiddleWare


dp = Dispatcher()

dp.include_routers(bot_functionality.router)

dp.message.middleware(SomeMiddleWare())


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    logging.warning(message.from_user)
    await message.answer(f"Weather forecast. Select a city or write a city", reply_markup=keyboard_new)


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

