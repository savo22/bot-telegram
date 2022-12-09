import sqlite3 as sq
from create_bot import bot


async def sql_start():
    global base, cur
    with sq.connect('master_cool.db') as base:
        cur = base.cursor()
        if cur:
            print('Data base connect OK!')
        cur.execute("""CREATE TABLE IF NOT EXISTS menu(
            фото TEXT,
            название PRIMARY KEY,
            описание TEXT,
            цена TEXT)""")
        base.commit()


async def sql_add_command(state):  # функция для заполнения данных
    async with state.proxy() as data:
        cur.execute("INSERT INTO menu VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute("SELECT * FROM menu").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')


async def sql_read2():
    a = cur.execute("SELECT * FROM menu").fetchall()
    return a


async def sql_delete_command(data):
    cur.execute("DELETE FROM menu WHERE название == ?", (data,))
    base.commit()


# async def create_client(user_id):  # база для клиента
#     user = cur.execute("SELECT user_id, имя, телефон FROM client WHERE user_id == '{key}'"
#                        .format(key=user_id,)).fetchall()
#     if not user:
#         cur.execute("INSERT INTO client VALUES(?, ?, ?)", (user_id, '', ''))
#     base.commit()
#
#
# async def edit_client(state, user_id):
#     async with state.proxy() as data:
#         cur.execute("UPDATE client SET имя = '{}', телефон = '{}' WHERE user_id == '{}'"
#                     .format(data['имя'], data['телефон'], user_id))
#         base.commit()

