from aiogram import types, Dispatcher
import json, string
from create_bot import dp

'''Удаляем маты.'''
#@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('mat_delete/cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
