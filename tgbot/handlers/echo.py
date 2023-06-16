from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.misc import UserStates
from tgbot.keyboards import weeks_keyboard, internet_keyboard, calls_keyboard


async def start_choosing(message: types.Message, state: FSMContext):
    await UserStates.weeks.set()
    await message.answer("Choose weeks", reply_markup=weeks_keyboard)


async def choose_weeks_quantity(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await UserStates.internet.set()
    await call.message.answer("Choose internet quantity", reply_markup=internet_keyboard)


async def choose_internet_quantity(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await UserStates.calls.set()
    await call.message.answer("Choose calls quantity", reply_markup=calls_keyboard)


async def choose_calls_quantity(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await UserStates.price.set()
    await call.message.answer("Choose price")


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
    dp.register_callback_query_handler(choose_weeks_quantity, state=UserStates.weeks, text=['4weeks', '12weeks'])
    dp.register_callback_query_handler(choose_internet_quantity, state=UserStates.internet, text=['internet_7', 'internet_7_30', 'internet_30'])
    dp.register_callback_query_handler(choose_calls_quantity, state=UserStates.calls, text=['calls_300', 'calls_301', 'calls_1501'])
    dp.register_callback_query_handler(choose_price, state=UserStates.price)
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
