"""Choose tariff handlers."""

import time
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup
from tgbot.misc import UserStates
from tgbot.keyboards import weeks_keyboard, internet_keyboard, calls_keyboard,\
    yes_no_keyboard, create_price_keyboard
from tgbot.misc.constants import DEFAULT_BOT_TEXT, tariffs, RECOMMENDATION


async def give_recommendation(call: types.CallbackQuery, tariff):
    tariff.name = tariff.name.replace('_', '-')
    await call.message.answer(RECOMMENDATION.format(tariff.name.capitalize(), tariff.name))
    time.sleep(2)
    await call.message.answer_sticker(sticker="CAACAgIAAxkBAAETh25kjbjjzG-cT9mFsEon9q9wkbw0AwAC3QAD9wLID-pZL7ynakA8LwQ")
    time.sleep(2)
    await call.message.answer("Чи подобається вам тариф?", reply_markup=yes_no_keyboard)
    await UserStates.suitable.set()


def choosing_logic(want_internet, want_calls, i):
    if int(want_internet[1]) == 1000 and int(want_calls[1]) == 3000:
        if float(want_internet[1]) <= i.internet \
                and float(want_calls[1]) <= i.calls:
            return True

    if int(want_internet[1]) == 1000:
        if float(want_internet[1]) <= i.internet \
                and float(want_calls[0]) <= i.calls <= float(want_calls[1]):
            return True

    if int(want_calls[1]) == 3000:
        if float(want_internet[0]) <= i.internet <= float(want_internet[1]) \
                and float(want_calls[1]) <= i.calls:
            return True

    if float(want_internet[0]) <= i.internet <= float(want_internet[1])\
            and float(want_calls[0]) <= i.calls <= float(want_calls[1]):
        return True


async def start_choosing(message: types.Message, state: FSMContext):
    await UserStates.weeks.set()
    await message.answer("💳 За скільки тижнів вам зручно платити?", reply_markup=weeks_keyboard)


async def choose_weeks_quantity(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'weeks': call.data})
    if call.data == '12_weeks':
        for i in tariffs:
            if i.weeks == 12:
                await give_recommendation(call, i)
                break
        else:
            await state.finish()
            await call.message.answer("На жаль такі тарифи недоступні зараз.\nБудь ласка, спробуйте ще раз:  /choose")
    else:
        await UserStates.internet.set()
        await call.message.answer("Як багато часу ви викристовуєте інтернет?", reply_markup=internet_keyboard)
        await call.message.answer_sticker(sticker="CAACAgIAAxkBAAETh3lkjbqV4aEOeCJU3CeHMB-W0cl0OgAC3AAD9wLID1DYvAZ7vfB8LwQ")


async def end_of_choosing(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'yes':
        await call.message.answer("Дякуємо, що обрали Lifecell 🤩")
    elif call.data == 'no':
        await call.message.answer("😭 Нам шкода, що ми не змогли знайти вам тариф.\nБудь ласка, спробуйте ще раз /choose")
    await state.finish()


async def choose_internet_quantity(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'internet': call.data})
    await UserStates.calls.set()
    await call.message.answer("Як часто ви телефонуєте?", reply_markup=calls_keyboard)


def choosing_bests_tariffs(data):
    suitable_options = []
    want_internet = data['internet'].split("_")
    want_calls = data['calls'].split("_")
    for i in tariffs:
        if not i.internet:
            i.internet = 0
        if not i.calls:
            i.calls = 0
        if choosing_logic(want_internet, want_calls, i):
            suitable_options.append(i)
    return suitable_options


async def choose_calls_quantity(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'calls': call.data})
    desire_options = await state.get_data()
    suitable_options = choosing_bests_tariffs(desire_options)
    if suitable_options:
        await state.update_data({'data': suitable_options})
        await UserStates.price.set()
        list_of_buttons = create_price_keyboard(suitable_options)
        await call.message.answer_sticker(sticker='CAACAgIAAxkBAAETh4Vkjbtg9JpUYhXXFaZ6dwn7RVq38AAC6QAD9wLIDxlbsUWIj86LLwQ')
        time.sleep(1)
        await call.message.answer("Оберіть ціну", reply_markup=InlineKeyboardMarkup(inline_keyboard=list_of_buttons))
    else:
        await state.finish()
        await call.message.answer("На жаль такі тарифи недоступні зараз.\nБудь ласка, спробуйте ще раз:  /choose")


async def choose_price(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    for i in data['data']:
        if i.price == int(call.data):
            i.name = i.name.replace('_', '-')
            await call.message.answer(RECOMMENDATION.format(i.name.capitalize(), i.name))
            time.sleep(3)
            await call.message.answer("Чи підходить вам тариф?", reply_markup=yes_no_keyboard)
            await UserStates.suitable.set()


async def bot_echo(message: types.Message):
    await message.answer(DEFAULT_BOT_TEXT)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(start_choosing, commands=['choose'])
    dp.register_callback_query_handler(choose_weeks_quantity, state=UserStates.weeks,
                                       text=['4_weeks', '12_weeks'])
    dp.register_callback_query_handler(end_of_choosing, state=UserStates.suitable, text=['yes', 'no'])
    dp.register_callback_query_handler(choose_internet_quantity, state=UserStates.internet,
                                       text=['0_07', '07_30', '31_1000'])
    dp.register_callback_query_handler(choose_calls_quantity, state=UserStates.calls,
                                       text=['0_300', '301_1500', '1501_3000'])
    dp.register_callback_query_handler(choose_price, state=UserStates.price)
    dp.register_message_handler(bot_echo)
