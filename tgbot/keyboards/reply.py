from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from tgbot.misc.constants import WEB_APP_URL

begin_btn = KeyboardButton(text="Почати роботу")
startup_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [begin_btn]
    ]
)

web_site_btn = KeyboardButton(
    text="Тисни сюди аби зареєструватись!",
    web_app=WebAppInfo(url=WEB_APP_URL)
)
signup_markup = ReplyKeyboardMarkup(keyboard=[[web_site_btn]], resize_keyboard=True, one_time_keyboard=True)
