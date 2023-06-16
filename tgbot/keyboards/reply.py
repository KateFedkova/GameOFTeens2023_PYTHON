from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

signup_btn = KeyboardButton(text="Sign up!")

signup_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [signup_btn]
    ]
)

web_site_btn = KeyboardButton(text="Click here to complete registration!", web_app=WebAppInfo(
            url="https://pavloshutz.github.io/signup-page/"))
signup_page = ReplyKeyboardMarkup(keyboard=[[web_site_btn]], resize_keyboard=True, one_time_keyboard=True)
