from aiogram import types, Dispatcher
from create_bot import bot, dp
from data_base import sqlite_db
from keyboards.users import rkb3, ikb
from handlers.tex import sc1, sc2, sc3


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    send_mess = f"Привет {message.from_user.first_name}! {sc3}"
    await bot.send_message(message.from_user.id, send_mess, reply_markup=rkb3)


@dp.message_handler(commands=['МЕНЮ'])
async def menu_command(message: types.Message):
    read = await sqlite_db.sql_read2()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
        await bot.send_message(message.from_user.id, text='Направить тебя к мастеру?', reply_markup=ikb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(menu_command, commands=['МЕНЮ'])






