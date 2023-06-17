"""All default commands for bot."""

from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустити бота"),
        types.BotCommand("help", "Вивести довідку"),
        types.BotCommand("choose", "Обрання тарифу"),
    ])
