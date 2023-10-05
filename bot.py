import asyncio
import logging
from keyboard import keyboard_new
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from weather_requests import city_weather, TOKEN

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):

    logging.warning(message.from_user)
    await message.answer(f"Weather forecast. Select a city or write a city", reply_markup=keyboard_new)



@dp.message(F.text)
async  def weather_of_the_city(message: types.Message):
    result = city_weather(message.text)
    await message.answer(result)


@dp.message(F.text == "Kyiv")
async def city_kyiv(message: types.Message):
    await message.answer(city_weather('Kyiv'))


@dp.message(F.text == "Dnepr")
async def city_dne(message: types.Message):
    await message.answer(city_weather('Dnepr'))


@dp.message(F.text == "Lviv")
async def city_lv(message: types.Message):
    await message.answer(city_weather('Lviv'))


@dp.message(F.text == "Kharkiv")
async def city_kh(message: types.Message):
    await message.answer(city_weather('Kharkiv'))


@dp.message(F.text == "Odessa")
async def city_od(message: types.Message):
    await message.answer(city_weather('Odessa'))


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

