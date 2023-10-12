from aiogram import types, F, Router
from weather_requests import city_weather


router = Router()


@router.message(F.text)
async  def weather_of_the_city(message: types.Message):
    result = city_weather(message.text)
    await message.answer(result)


@router.message(F.text == "Kyiv")
async def city_kyiv(message: types.Message):
    await message.answer(city_weather('Kyiv'))


@router.message(F.text == "Dnepr")
async def city_dnepr(message: types.Message):
    await message.answer(city_weather('Dnepr'))


@router.message(F.text == "Lviv")
async def city_lviv(message: types.Message):
    await message.answer(city_weather('Lviv'))


@router.message(F.text == "Kharkiv")
async def city_kha(message: types.Message):
    await message.answer(city_weather('Kharkiv'))


@router.message(F.text == "Odessa")
async def city_ode(message: types.Message):
    await message.answer(city_weather('Odessa'))