# Библиотеки

from aiogram import Bot, Dispatcher, executor, types
import logging
logging.basicConfig(level=logging.INFO)
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

# Файлы

import config as cfg
from Podderzhka.db import Database
import Podderzhka.functions as fc
from key.kbs import kb_client1, kb_client2, kb_client3, kb_client4, kb_client5, kb_client6
from key.inline import txt_btn, txt_btn1, txt_btn2, txt_btn3, txt_btn4, txt_btn5, txt_btn6, txt_btn7, txt_btn8, txt_btn9
from base import db1_start, create_profile, edit

# Переменные

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database('Podderzhka/base.db')
txt = ''
channel = ''
group1_id = cfg.group1
group2_id = cfg.group2



# Классы

class Profile1(StatesGroup):
    Media = State()
    username = State()
    description = State()

class Profile2(StatesGroup):
    photo = State()
    username = State()
    description = State()

class chat(StatesGroup):
    text = State()

async def on_startup(_):
    await db1_start()


@classmethod
async def upload_photo(cls, sleep=None):
    
     await cls.do(cls.UPLOAD_PHOTO, sleep)





# Команды 

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "💬 Привет! Это шаблон моего бота, протестируйте его.\nНадеюсь, он вам понравится ;)\n \n📍 Могу сделать вам бота, пиши:\n@manager_in_telegram (Тиму₽)💤", reply_markup=kb_client1)
    
    await message.answer('💬 Инструкция по использованию бота:\n \n1️⃣ Для того, чтобы купить рекламу, нужно нажать на кнопку "Купить рекламу📈", затем выбрать прайс и заполнить анкету рекламодателя. Админ рассмотрит вашу заявку. После того, как админ принял вашу заявку, вам нужно оплатить прайс, который вы выбрали, реклама появится в Телеграм канале. \n \n2️⃣ Вы можете задать любой вопрос в поддержке, наш бот ответит вам:)\n \n3️⃣ Чтобы предложить новость, нужно нажать на кнопку "Предложить новость🚀" и, аналогично с рекламой заполнить анкету📒\n \n \n📍Чтобы снова открыть инструкцию снова, напиши:\n/инструкция 🔍')
    await create_profile(user_id=message.from_user.id)

@dp.message_handler(commands=['инструкция'])
async def start(message: types.Message):
    await message.answer('💬 Инструкция по использованию бота:\n \n1️⃣ Для того, чтобы купить рекламу, нужно нажать на кнопку "Купить рекламу📈", затем выбрать прайс и заполнить анкету рекламодателя. Админ рассмотрит вашу заявку. После того, как админ принял вашу заявку, вам нужно оплатить прайс, который вы выбрали, реклама появится в Телеграм канале. \n \n2️⃣ Вы можете задать любой вопрос в поддержке, наш бот ответит вам:)\n \n3️⃣ Чтобы предложить новость, нужно нажать на кнопку "Предложить новость🚀" и, аналогично с рекламой заполнить анкету📒\n \n \n📍Чтобы снова открыть инструкцию снова, напиши:\n/инструкция 🔍')

@dp.message_handler(commands=['панель'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Панель открыта♻️", reply_markup=kb_client1) 





# Обработка keyboard button

@dp.message_handler(lambda message: message.text == 'Купить рекламу📈', content_types=['text'])
async def ab2(message: types.Message):
    await message.answer('💬 Нажмите на кнопку "💸ПРАЙС💸", чтобы выбрать услугу🪙', reply_markup=kb_client2)

@dp.message_handler(lambda message: message.text == 'Закрыть панель🧩', content_types=['text'])
async def ab3(message: types.Message):
    await message.answer('💬 Панель закрыта♻️\n \n📍 Чтобы открыть панель напишите:\n/панель ℹ️', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == 'Информация🌐', content_types=['text'])
async def ab4(message: types.Message):
    await message.answer('ℹ️ Писать админам только в крайних случаях!', reply_markup=txt_btn2) 

@dp.message_handler(lambda message: message.text == 'Оплатить рекламу💸', content_types=['text'])
async def ab1(message: types.Message):
    await message.answer(text=txt, reply_markup=txt_btn7)





# pay

# keyboard *PAY*
@dp.message_handler(lambda message: message.text == '💸ПРАЙС💸', content_types=['text'])
async def a1(message: types.Message):
    await message.answer('💬 *ЭТО ПРИМЕР ПРАЙСА, СГЕНЕРИРОВАЛ В ЧАТ GPT!*\n \n🚨 Сначала выберите услугу:\n \n🌟 Увеличьте охват вашей аудитории с помощью рекламы в нашем телеграм канале! 🚀\n \n💼 Прайс-лист по размещению рекламы:\n \n🟢1 пост в канале: 300₽\n \n🟡1 пост в закрепе на 3 часа: 399₽\n \n🟠1 пост в закрепе на 5 часов: 499₽\n \n🔴1 пост в закрепе на 24 часа: 999₽\n \n🟣1 пост в закрепе на 3 дня: 2499₽\n \n⚫️Размещение поста в 3 каналах в закреп на 24 часа: 2999₽\n🔺 Другие услуги предлагайте в личку!\n \n🎯 Дополнительные опции:\n \nРазмещение в закрепленных постах: +50₽\nВключение ссылки в размещение: +50₽\nРазмещение в рассылке подписчикам: +100₽\n💰 Специальное предложение:\n \nЗакажи пакет из 5 постов и получи скидку 10%!\nЗакажи пакет из 10 постов и получи скидку 30%!\n📊 После размещения рекламы мы предоставляем отчёт о результатах!\n \n📍 Не упустите возможность привлечь новых клиентов и увеличить прибыль своего бизнеса с нашим телеграм каналом! 🌈✨', reply_markup=txt_btn1)


# state *PAY*
@dp.message_handler(lambda message: message.text == 'Заполнить анкету рекламодателя🤵🏼', content_types=['text'])
async def b1(message: types.Message) -> None:
    await message.answer('💬 Сначала пришлите фото🌇', reply_markup=kb_client4)
    
    await Profile1.Media.set()

@dp.message_handler(content_types=['video', 'photo'], state=Profile1.Media)
async def c1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Media'] = message.photo[0].file_id
    
    await message.reply('💬 А теперь отправьте свой username из Телеграма, например: @manager_in_telegram♻️')
    await Profile1.next()

@dp.message_handler(lambda message: not message.photo or not message.video, state=Profile1.Media)
async def b2(message: types.Message, state: FSMContext):
    if message.text == 'Отмена❌':
        await message.answer('Меню♻️', reply_markup=kb_client1)
        await state.finish()
    else:
        await message.reply('💬 Это не фото!')

@dp.message_handler(state=Profile1.username)
async def c2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text

    await message.reply('💬 Спасибо! Осталось совсем чуть-чуть, отправьте текст вашего поста♻️', reply_markup=types.ReplyKeyboardRemove())
    await Profile1.next()

@dp.message_handler(lambda message: not message.text.startswith('@'), state=Profile1.username)
async def c2(message: types.Message, state: FSMContext):
    if message.text == 'Отмена❌':
        await message.answer('Меню♻️', reply_markup=kb_client1)
        await state.finish()
    else:
        await message.reply('💬 Это не username!')

@dp.message_handler(state=Profile1.description)
async def c3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['Media'], caption=f"{data['username']}\n{data['description']}\n \n{txt}", reply_markup=txt_btn8)
        await bot.send_photo(chat_id=group1_id, photo=data['Media'], caption=f"{data['username']}\n{data['description']}\n \n{txt}", reply_markup=txt_btn9)
    await state.finish()


# callback *PAY*
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('pay'))
async def inline_pay(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'pay-2':
        await bot.send_message(chat_id=callback.from_user.id, text='💬 Заполни анкету заново♻️', reply_markup=kb_client2)
        await callback.message.delete()
    elif callback.data == 'pay-3':
        await bot.send_message(chat_id=callback.from_user.id, text='💬 Ваша анкета успешно создана. Ожидайте, администратор рассмотрит вашу заявку📝\n \n📍 Не отчищайте историю, админ ответит вам в боте!', reply_markup=kb_client1)
        await callback.message.delete()





# Предложить новость

@dp.message_handler(lambda message: message.text == 'Предложить новость🚀', content_types=['text'])
async def news1(message: types.Message) -> None:
    await message.reply('💬 Пришлите фото🌇', reply_markup=kb_client4)
    
    await Profile2.photo.set()

@dp.message_handler(lambda message: not message.photo, state=Profile2.photo)
async def news1(message: types.Message, state: FSMContext):
    if message.text == 'Отмена❌':
        await message.answer('Меню♻️', reply_markup=kb_client1)
        await state.finish()
    else:
        await message.reply('💬 Это не фотография!')

@dp.message_handler(content_types=['photo'], state=Profile2.photo)
async def news1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    
    await message.reply('💬 А теперь отправьте свой username из Телеграма, например: @manager_in_telegram\n \n📍Если хотите остаться анонимными, напишите: @anonymous🥷🏻')
    await Profile2.next()



@dp.message_handler(lambda message: not message.text.startswith('@'), state=Profile2.username)
async def news1(message: types.Message, state: FSMContext):
    if message.text == 'Отмена❌':
        await message.answer('Меню♻️', reply_markup=kb_client1)
        await state.finish()
    else:
        await message.reply('💬 Это не username!')

@dp.message_handler(state=Profile2.username)
async def news1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text

    await message.reply('💬 Осталось совсем чуть-чуть, отправьте текст(новость, информацию и тд.)♻️', reply_markup=types.ReplyKeyboardRemove())
    await Profile2.next()

@dp.message_handler(state=Profile2.description)
async def news1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'], caption=f"{data['username']}\n{data['description']}")
        await bot.send_message(chat_id=message.from_user.id, text='💬 Спасибо! Ваша новость успешно отправлена📝', reply_markup=kb_client1)
        global group2_id
        await bot.send_photo(chat_id=group2_id, photo=data['photo'], caption=f"{data['username']}\n{data['description']}")
    await state.finish()





# Поддержка

@dp.message_handler(lambda message: message.text == 'Поддержка⚙', content_types=['text'])
async def mess(message: types.Message):
    await message.answer('💬 Задайте любой вопрос, относящейся к боту, к оплате и тд., сразу ответим✏️', reply_markup=kb_client6)
    await chat.text.set()

@dp.message_handler(state=chat.text)
async def supp(message: types.Message, state: FSMContext):
    if message.text == 'Закончить диалог☎️':
        await bot.send_message(chat_id=message.from_user.id, text='💬 Диалог закончен❌', reply_markup=kb_client1)
        await state.finish()
    else:
        async with state.proxy() as data:
            data['text'] = message.text
    
        answer_id = fc.recognize_question(message.text, db.get_questions())
        await message.answer(db.get_answer(answer_id))
        await chat.text.set()

        



# Обработка callback (Inline keyboard)

@dp.callback_query_handler(text='a')
async def inline(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('💬 *ЭТО ПРИМЕР ПРАЙСА, СГЕНЕРИРОВАЛ В ЧАТ GPT!*\n \n🚨 Сначала выберите услугу:\n \n🌟 Увеличьте охват вашей аудитории с помощью рекламы в нашем телеграм канале! 🚀\n \n💼 Прайс-лист по размещению рекламы:\n \n🟢1 пост в канале: 300₽\n \n🟡1 пост в закрепе на 3 часа: 399₽\n \n🟠1 пост в закрепе на 5 часов: 499₽\n \n🔴1 пост в закрепе на 24 часа: 999₽\n \n🟣1 пост в закрепе на 3 дня: 2499₽\n \n⚫️Размещение поста в 3 каналах в закреп на 24 часа: 2999₽\n🔺 Другие услуги предлагайте в личку!\n \n🎯 Дополнительные опции:\n \nРазмещение в закрепленных постах: +50₽\nВключение ссылки в размещение: +50₽\nРазмещение в рассылке подписчикам: +100₽\n💰 Специальное предложение:\n \nЗакажи пакет из 5 постов и получи скидку 10%!\nЗакажи пакет из 10 постов и получи скидку 30%!\n📊 После размещения рекламы мы предоставляем отчёт о результатах!\n \n📍 Не упустите возможность привлечь новых клиентов и увеличить прибыль своего бизнеса с нашим телеграм каналом! 🌈✨', reply_markup=txt_btn1)

@dp.callback_query_handler(text='aa')
async def del_inline(callback: types.CallbackQuery) -> None:
    await callback.message.delete()
    await bot.send_message(chat_id=callback.from_user.id, text='💬 Для размещения вашей рекламы в Телеграм канале: "ТГК", нужно заполнить анкету💻\n \n🛎 Нажмите на кнопку "Заполнить анкету рекламодателя🤵🏼"', reply_markup=kb_client3)



@dp.callback_query_handler(lambda callback: callback.data.startswith('answer'))
async def pay_choice(callback: types.CallbackQuery):
    if callback.data == 'answer-1':
        await bot.send_message(chat_id=callback.from_user.id, text='💬 Админ принял вашу заявку! Для того чтобы ваш пост успешно был выложен в Телеграм канал: "ТГК", оплатите услугу🤝', reply_markup=kb_client5)
        await callback.message.edit_reply_markup(txt_btn)
        global group1_id
    elif callback.data == 'answer-2':
        await bot.send_message(chat_id=callback.from_user.id, text='💬 Извините, но админ отклонил вашу заявку. Наверное, контент вашего поста не подходит по тематике канала. Если произошла ошибка, напиши админу: @manager_in_telegram👔')
        await callback.message.delete()



@dp.callback_query_handler()
async def callback1(callback_quevery: types.CallbackQuery):
    if callback_quevery.data == '1':
        await bot.send_message(chat_id=callback_quevery.from_user.id, text='💬 Мы, небольшая компания программистов со специализацией на разработке телеграм ботов.\n \nℹ️ Владеем языками программирования: Python, JavaScript, HTML, Css и др. Занимаемся созданием как стандартных ботов, так и ботов с WEB приложением. Используем библиотеки Aiogram, pyTelegramBotAPI.\n \n📍 СДЕЛАЕМ УДОБНОГО ТЕЛЕГРАМ БОТА, КОТОРЫЙ УПРОСТИТ ВАМ ЖИЗНЬ!🪐')
    elif callback_quevery.data == '2':
        await bot.send_message(chat_id=callback_quevery.from_user.id, text='💬 Тут должна быть информация🛜')
    elif callback_quevery.data == '3':
        await bot.send_message(chat_id=callback_quevery.from_user.id, text='💬 Тут должна быть информация🛜')
    
    global txt    
    if callback_quevery.data == 'data-1':
        await callback_quevery.message.edit_text(text='🟢Услуга №1 - Реклама 1 пост в канале⚡️\nЦена - 300₽💵', reply_markup=txt_btn6)
        txt = '🟢Услуга №1 - Реклама 1 пост в канале⚡️\nЦена - 300₽💵'
    elif callback_quevery.data == 'data-2':
        await callback_quevery.message.edit_text(text='🟡Услуга №2 - Реклама 3 ч в ТОПЕ⚡️\nЦена - 399₽ 💵', reply_markup=txt_btn6)
        txt = '🟡Услуга №2 - Реклама 3 часа в ТОПЕ⚡️\nЦена - 399₽💵'
    elif callback_quevery.data == 'data-3':
        await callback_quevery.message.edit_text(text='🟠Услуга №3 - Реклама 5 ч в ТОПЕ⚡️\nЦена - 499₽ 💵', reply_markup=txt_btn6)
        txt = '🟠Услуга №3 - Реклама 5 часов в ТОПЕ⚡️\nЦена - 499₽💵'
    elif callback_quevery.data == 'data-4':
        await callback_quevery.message.edit_text(text='🔴Услуга №4 - Реклама 24 ч в ТОПЕ⚡️\nЦена - 999₽ 💵', reply_markup=txt_btn6)
        txt = '🔴Услуга №4 - Реклама 24 часа в ТОПЕ⚡️\nЦена - 999₽💵'
    elif callback_quevery.data == 'data-5':
        await callback_quevery.message.edit_text(text='🟣Услуга №5 - Реклама 3 дн в ТОПЕ⚡️\nЦена - 2499₽ 💵', reply_markup=txt_btn6)
        txt = '🟣Услуга №5 - Реклама 3 дня в ТОПЕ⚡️\nЦена - 2499₽💵'
    elif callback_quevery.data == 'data-6':
        await callback_quevery.message.edit_text(text='⚫️Услуга №6 - МЕГА-Реклама 24 часа в 3 каналах в ТОПЕ⚡️\nЦена - 2999₽💵', reply_markup=txt_btn6)
        txt = '⚫️Услуга №6 - МЕГА-Реклама 24 часа в 3 каналах в ТОПЕ⚡️\nЦена - 2999₽💵'
    




# Постоянная работа Бота

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)