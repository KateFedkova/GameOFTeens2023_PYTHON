from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

weeks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("4 тижні", callback_data=f"4 weeks"),
            InlineKeyboardButton("12 тижнів", callback_data=f"12 weeks")
        ]
    ]
)


internet_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("до 7 ГБ", callback_data=f"internet_7"),
            InlineKeyboardButton("від 7 до 30 ГБ", callback_data=f"internet_7_30"),
            InlineKeyboardButton("від 30 до Безліміту", callback_data=f"internet_30")
        ]
    ]
)

calls_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("до 300 хв", callback_data=f"calls_300"),
            InlineKeyboardButton("від 301 до 1500 хв", callback_data=f"calls_301"),
            InlineKeyboardButton("від 1501 до Безліміту", callback_data=f"calls_1501")
        ]
    ]
)
