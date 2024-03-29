import sqlite3

from create_bot import bot

base = sqlite3.connect('pizza_cool.db')
cur = base.cursor()


def sql_start():
    if base:
        print('Data base connected OK!')
    base.execute('''
    CREATE TABLE IF NOT EXISTS menu(
        img TEXT,
        name TEXT PRIMARY KEY,
        description TEXT,
        price TEXT
        )
    ''')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute(
            '''INSERT INTO menu VALUES (?, ?, ?, ?)''',
            tuple(data.values())
        )
        base.commit()


async def sql_read(message):
    for ret in cur.execute('''SELECT * FROM menu''').fetchall():
        await bot.send_photo(
            message.from_user.id, ret[0],
            f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}'
        )


async def sql_read2():
    return cur.execute('''SELECT * FROM menu''').fetchall()


async def sql_delete_command(data):
    cur.execute('''DELETE FROM menu WHERE name == ?''', (data,))
    base.commit()
