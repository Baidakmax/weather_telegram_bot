from aiogram import types

kb = [
    [
        types.KeyboardButton(text="Kyiv"),
        types.KeyboardButton(text="Dnepr"),
        types.KeyboardButton(text="Lviv"),
        types.KeyboardButton(text="Kharkiv"),
        types.KeyboardButton(text="Odessa"),
    ],
]
keyboard_new = types.ReplyKeyboardMarkup(
    keyboard= kb,
    resize_keyboard=True,
    input_field_placeholder="Choose a city"
)