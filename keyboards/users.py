from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


rkb3 = ReplyKeyboardMarkup(resize_keyboard=True, )
b3 = KeyboardButton('/МЕНЮ')
rkb3.add(b3)


ikb = InlineKeyboardMarkup(row_width=1)
ib1 = InlineKeyboardButton(text="ХОЧУ!", url="https://t.me/britva6")
ikb.add(ib1)


