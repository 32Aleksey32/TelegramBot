from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

"""Кнопки клавиатуры клиента."""
b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3)
