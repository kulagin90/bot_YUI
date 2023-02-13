import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
from setings import bot_token

# кнопка возврата к списку услуг
mar_back = InlineKeyboardMarkup()
mar_back1 = InlineKeyboardButton('Перейти к списку услуг', callback_data='b')
mar_back.add(mar_back1)

#клавиатура с кнопками услуг
def services(id_user, list_servis, bot):
    mar = InlineKeyboardMarkup()
    num = 0
    for x in range(len(list_servis)):
        for i in list_servis[num].keys():
            mar.add(InlineKeyboardButton(i, callback_data='q'+'!'+str(num) ))
        num += 1
    bot.send_message(id_user, 'Выберите услугу из списка', reply_markup= mar)

# клавиатура для помощи пользователю
def user_help (id_user, bot):
    mar_for_user = InlineKeyboardMarkup(row_width=2)
    mar_for_user2 = InlineKeyboardButton('FAQ', callback_data='f'+'!'+str(id_user))
    mar_for_user3 = InlineKeyboardButton('Тех-поддержка', callback_data='t'+'!'+str(id_user))
    mar_back = InlineKeyboardButton('Перейти к списку услуг', callback_data='b')
    mar_for_user.add(mar_for_user2, mar_for_user3, mar_back)
    bot.send_message(id_user, 'нужна помощь?', reply_markup=mar_for_user)


# клавиатура расчета стоимости
def service_order(id_user,bot, data):
    mar_order = InlineKeyboardMarkup(row_width=2)
    mar_order1= InlineKeyboardButton('Расчитать стоимость', callback_data='s'+'!'+str(data))
    mar_order2= InlineKeyboardButton('Вернуться к списку услуг', callback_data='b')
    mar_order.add(mar_order1,mar_order2)
    bot.send_message(id_user, '⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ', reply_markup= mar_order)


# кнопка для обратной связи с пользователем
def admin_servic(id, id_chanel, bot, text):
    mar_user_back = InlineKeyboardMarkup()
    mar_user_back.add(InlineKeyboardButton('Ответить на вопрос', callback_data='e'+'!'+str(id)))
    bot.send_message(id_chanel,text, reply_markup= mar_user_back)

# кнопка для обратной связи с пользователем
def technical(user, id):
    mar_tech = InlineKeyboardMarkup()
    mar_tech.add(InlineKeyboardButton(f'Связаться с {user}', callback_data='h'+'!'+str(id)))
    return mar_tech


def qw (id, bot,text_):
    mar = InlineKeyboardMarkup()
    mar.add(InlineKeyboardButton('Задать еще вопрос', callback_data='f'))
    bot.send_message(id,text_, reply_markup=mar)