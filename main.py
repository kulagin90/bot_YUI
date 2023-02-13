import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto
from setings import list_servis, bot_token, tech_chanel, list_answers, admins_chanel, admins_id
from keybord_func import services, user_help, service_order, mar_back, admin_servic, qw
from func import vall, delete_handler, delete_query_handler, admins_call, answer, keys, question, application


bot = telebot.TeleBot(bot_token)


def dt(s):
    s = s[1:]
    return s


def fs(st):
    return (st[0])


@bot.message_handler(commands=['start', 'help'])
def comands(message):
    if message.text == '/start':
        services(message.chat.id, list_servis, bot)
        delete_handler(message, bot)


    if message.text == '/help':

        user_help(message.chat.id, bot)
        delete_handler(message, bot)


@bot.message_handler(chat_types=['channels'], content_types=['text'])
def vvv(message):
    print(message)




@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, )
    id = call.message.chat.id
    flag = fs(call.data)
    data = dt(call.data)

    if flag == 'f': # флаг для FAQ
        data = data.split('!')
        msg = bot.send_message(id, 'Введите Ваш вопрос', reply_markup=mar_back)
        delete_query_handler(call.message, bot)
        bot.register_next_step_handler(msg, question)

        delete_query_handler(call.message, bot)



    elif flag == 't':# флаг тех-поддержки
        data = data.split('!')
        print(call.from_user)
        msg = bot.send_message(id, 'С Вами свяжется первый освободившийся специалист', reply_markup=mar_back)
        bot.register_next_step_handler(msg, admins_call)
        delete_query_handler(call.message, bot)

        admins_call(id, bot, tech_chanel,call)


    elif flag == 'q':#флаг выбота услуг
        data = data.split('!')
        text_keys = keys(list_servis, data[1])
        text_vall = vall(list_servis, data[1])
        bot.send_message(id, f'<b>{text_keys}:</b>\n<i>{text_vall}</i>', parse_mode='HTML')
        delete_query_handler(call.message, bot)
        service_order(id, bot, data[1])

        delete_query_handler(call.message, bot)

    elif flag =='b':#фла для возврата к списку услуг
        services(id, list_servis, bot)
        delete_query_handler(call.message, bot)

    elif flag == 's':#флаг расчета стоимости
        data = data.split('!')
        text = keys(list_servis, data[1])
        bot.send_message(tech_chanel, f'Расчитать стоимость:\n<b><i>{text}</i></b>\n{call.message.chat.username}', parse_mode='html')


    elif flag == 'e':#флаг для обратной связи администратора с пользователем
        data = data.split('!')
        msg = bot.send_message(admins_chanel, 'Ответ отправлен')
        bot.register_next_step_handler(msg, answer)

        bot.forward_message(chat_id=data[1], from_chat_id=admins_chanel, message_id=call.message.id+1)




    elif flag == 'h':#флаг для обратной связи тех-поддержки с пользователем
        data = data.split('!')




print("Ready")
bot.infinity_polling()