from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

txt_btn = InlineKeyboardMarkup(row_width=2)
txt_btn1 = InlineKeyboardMarkup(row_width=2)
txt_btn2 = InlineKeyboardMarkup(row_width=2)
txt_btn3 = InlineKeyboardMarkup(row_width=2)
txt_btn4 = InlineKeyboardMarkup(row_width=2)
txt_btn5 = InlineKeyboardMarkup(row_width=2)
txt_btn6 = InlineKeyboardMarkup(row_width=2)
txt_btn7 = InlineKeyboardMarkup(row_width=2)
txt_btn8 = InlineKeyboardMarkup(row_width=2)
txt_btn9 = InlineKeyboardMarkup(row_width=2)



b1 = InlineKeyboardButton('🟢', callback_data='data-1')
b2 = InlineKeyboardButton('🟡', callback_data='data-2')
b3 = InlineKeyboardButton('🟠', callback_data='data-3')
b4 = InlineKeyboardButton('🔴', callback_data='data-4')
b5 = InlineKeyboardButton('🟣', callback_data='data-5')
b6 = InlineKeyboardButton('⚫️', callback_data='data-6')
txt_btn1.row(b1,b2,b3)
txt_btn1.row(b4, b5, b6)


btn1 = InlineKeyboardButton('О нас🦄', callback_data='1')
btn2 = InlineKeyboardButton('Ячейка №2', callback_data='2')
btn3 = InlineKeyboardButton('Ячейка №3', callback_data='3')
btn4 = InlineKeyboardButton('Админ/Менеджер👔', url='https://t.me/manager_in_telegram')
btn5 = InlineKeyboardButton('Владелец тгк👑', url='https://t.me/manager_in_telegram')
txt_btn2.row(btn1, btn2, btn3)
txt_btn2.row(btn4, btn5)


button1 = InlineKeyboardButton('*ссылка*', url='t.me/newspredlozhka')
txt_btn3.row(button1)


bn1 = InlineKeyboardButton('Закончить диалог☎️', callback_data='dialog')
txt_btn4.row(bn1)


bn2 = InlineKeyboardButton('', callback_data='')
txt_btn5.row(bn2)


r1 = InlineKeyboardButton('<< Назад', callback_data='a')
r2 = InlineKeyboardButton('Подтвердить❤️', callback_data='aa')
txt_btn6.row(r1, r2)


pay_btn1 = InlineKeyboardButton('💰ОПЛАТИТЬ💰', url='https://online.sberbank.ru/')
txt_btn7.add(pay_btn1)


pay_btn2 = InlineKeyboardButton('🔴Неверно', callback_data='pay-2')
pay_btn3 = InlineKeyboardButton('🟢Верно', callback_data='pay-3')
txt_btn8.row(pay_btn2, pay_btn3)


yes = InlineKeyboardButton('🟢Да', callback_data='answer-1')
no = InlineKeyboardButton('🔴Нет', callback_data='answer-2')
txt_btn9.row(yes, no)