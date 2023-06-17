"""All inline keyboards for bot."""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

weeks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("За 4 тижні", callback_data="4_weeks"),
            InlineKeyboardButton("Одразу за 12 тижнів", callback_data="12_weeks")
        ]
    ]
)


internet_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Майже не використовую", callback_data="0_07")],
        [InlineKeyboardButton("Майже постійно", callback_data="07_30")],
        [InlineKeyboardButton("Проводжу в інтернеті весь вільний час", callback_data="31_1000")]
    ]
)

calls_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("В основному використовую месенджери", callback_data="0_300")],
        [InlineKeyboardButton("Телефоную часто", callback_data="301_1500")],
        [InlineKeyboardButton("Цілими днями спілкуюсь з друзями", callback_data="1501_3000")]
    ],
)


yes_no_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Так", callback_data="yes"),
            InlineKeyboardButton("Ні", callback_data="no")
        ]
    ]
)


def create_price_keyboard(suitable_options):
    list_of_buttons = []
    for i in suitable_options:
        list_of_buttons.append([InlineKeyboardButton(f"{i.price}", callback_data=f"{i.price}")])
    return list_of_buttons
