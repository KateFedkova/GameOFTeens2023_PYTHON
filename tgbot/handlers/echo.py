from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.misc import UserStates


async def start_choosing(message: types.Message, state: FSMContext):
    await UserStates.weeks.set()
    await message.answer("Choose weeks")


async def choose_weeks_quantity(message: types.Message, state: FSMContext):
    await state.finish()
    await UserStates.internet.set()
    await message.answer("Choose internet quantity")


async def choose_internet_quantity(message: types.Message, state: FSMContext):
    await state.finish()
    await UserStates.calls.set()
    await message.answer("Choose calls quantity")


async def choose_calls_quantity(message: types.Message, state: FSMContext):
    await state.finish()
    await UserStates.price.set()
    await message.answer("Choose price")


async def choose_price(message: types.Message, state: FSMContext):
    await state.finish()


async def bot_echo(message: types.Message):
    text = [
        "Эхо без состояния.",
        "Сообщение:",
        message.text
    ]

    await message.answer('\n'.join(text))


async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f'Эхо в состоянии {hcode(state_name)}',
        'Содержание сообщения:',
        hcode(message.text)
    ]
    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(start_choosing, commands=['choose'])
    dp.register_message_handler(choose_weeks_quantity, state=UserStates.weeks)
    dp.register_message_handler(choose_internet_quantity, state=UserStates.internet)
    dp.register_message_handler(choose_calls_quantity, state=UserStates.calls)
    dp.register_message_handler(choose_price, state=UserStates.price)
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
