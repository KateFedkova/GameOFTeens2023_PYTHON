import json

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.types import KeyboardButton, WebAppInfo, ReplyKeyboardMarkup

from tgbot.services.interact_database import db_interaction


async def user_start(message: Message):
    if db_interaction.check_user_in_db(message.from_user.id):
        await message.answer("All is okay.")
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        signup_btn = KeyboardButton(text="Sign up!")
        markup.add(signup_btn)
        await message.reply("Hello, user!", reply_markup=markup)


async def signup_handler(message: Message):
    web_site_btn = KeyboardButton(text="Click here to complete registration!", web_app=WebAppInfo(
            url="https://pavloshutz.github.io/signup-page/"))
    markup = ReplyKeyboardMarkup(keyboard=[[web_site_btn]], resize_keyboard=True, one_time_keyboard=True)
    await message.answer("Please complete registration in order to communicate with me!", reply_markup=markup)


async def signup_user(message: Message):
    data = json.loads(message.web_app_data.data)
    db_interaction.add_user_to_db(message.from_user.id, data["name"], data["phone"])


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"])
    dp.register_message_handler(signup_handler, lambda msg: msg.text.lower() == 'sign up!')
    dp.register_message_handler(signup_user, content_types={'web_app_data'})
