from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3)# .row(b4, b5)

# kb_client.row(b1, b2, b3) кнопки в 1 строку
#kb_client.add(b1).add(b2).add(b3) кнопки в 1 столбец
#kb_client.add(b1).add(b2).insert(b3) кнопка 1 вверху и 2 внизу