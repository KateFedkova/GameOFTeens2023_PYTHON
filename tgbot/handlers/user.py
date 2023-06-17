"""Handlers for starting conversation with user."""

import json

from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from tgbot.services.interact_database import db_interaction
from tgbot.keyboards.reply import signup_markup
from tgbot.misc.constants import BOT_INFO


async def user_start(message: Message):
    """Start conversation with user and check if user is authorized."""
    if db_interaction.check_user_in_db(message.from_user.id):
        username = db_interaction.get_username(message.from_user.id)
        await message.answer(f"З поверненням, {username}! Аби обрати тариф, введи /choose.")
    else:
        await message.reply(BOT_INFO, reply_markup=signup_markup)


async def signup_user(message: Message):
    """Fetch data from login page and save it into database."""
    removed_keyboard = ReplyKeyboardRemove()
    data = json.loads(message.web_app_data.data)
    db_interaction.add_user_to_db(message.from_user.id, data["name"], data["phone"])
    await message.answer("Ви були успішно зареєтровані у систему!", reply_markup=removed_keyboard)


def register_user(dp: Dispatcher):
    """Register all handlers for interaction with user."""
    dp.register_message_handler(user_start, commands=["start"])
    dp.register_message_handler(signup_user, content_types={'web_app_data'})
