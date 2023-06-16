import json

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.services.interact_database import db_interaction
from tgbot.keyboards.reply import startup_markup, signup_markup


async def user_start(message: Message):
    if db_interaction.check_user_in_db(message.from_user.id):
        await message.answer("З поверненням! Аби обрати тариф, введи /choose.")
    else:
        await message.reply("Вітаю тебе! Давай розпочнемо роботу.", reply_markup=startup_markup)


async def signup_handler(message: Message):
    await message.answer(
        "Будь-ласка зареєструйся аби надалі користуватися моїми послугами!",
        reply_markup=signup_markup
    )


async def signup_user(message: Message):
    data = json.loads(message.web_app_data.data)
    db_interaction.add_user_to_db(message.from_user.id, data["name"], data["phone"])


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"])
    dp.register_message_handler(signup_handler, lambda msg: msg.text.lower() == 'почати роботу')
    dp.register_message_handler(signup_user, content_types={'web_app_data'})
