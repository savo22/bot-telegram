from aiogram import Bot, Dispatcher, executor
from create_bot import dp
from handlers import client, admin, tex
from data_base import sqlite_db


async def on_startup(_):
    await sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
