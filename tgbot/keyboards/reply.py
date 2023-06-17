from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from tgbot.misc.constants import SIGNUP_PAGE

web_site_btn = KeyboardButton(
    text="Тисни сюди аби зареєструватись!",
    web_app=WebAppInfo(url=SIGNUP_PAGE)
)
signup_markup = ReplyKeyboardMarkup(keyboard=[[web_site_btn]], resize_keyboard=True, one_time_keyboard=True)
