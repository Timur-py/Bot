from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_client1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client3 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client4 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client5 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client6 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client7 = ReplyKeyboardMarkup(resize_keyboard=True)

bt1 = KeyboardButton("Предложить новость🚀")
bt2 = KeyboardButton("Купить рекламу📈")
bt3 = KeyboardButton("Поддержка⚙")
bt4 = KeyboardButton("Закрыть панель🧩")
bt5 = KeyboardButton("Информация🌐")

kb_client1.row(bt3, bt5)
kb_client1.row(bt1,bt2)
kb_client1.row(bt4)


button1 = KeyboardButton("💸ПРАЙС💸")
kb_client2.add(button1)


button2 = KeyboardButton("Заполнить анкету рекламодателя🤵🏼")
kb_client3.add(button2)


button3 = KeyboardButton("Отмена❌")
kb_client4.add(button3)

button4 = KeyboardButton("Оплатить рекламу💸")
kb_client5.add(button4)

button5 = KeyboardButton('Закончить диалог☎️')
kb_client6.add(button5)
