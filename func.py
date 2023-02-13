import json
import telebot
from setings import bot_token, tech_chanel, admins_chanel, list_answers
from keybord_func import admin_servic, technical, qw


bot = telebot.TeleBot(bot_token)

#функция возвращае values из list_servic
def vall(list_, data):
    for i in list_[int(data)].values():
        return i
#функция возвращае keys из list_servic
def keys (list_, data):
    for i in list_[int(data)].keys():
        return i

#функия удаляет сообщения
def delete_handler(message, bot):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id - 2)
        
    except:
        pass

#функия удаляет сообщения
def delete_query_handler(message, bot):
    try:
       bot.delete_message(message.chat.id, message.id)
       bot.delete_message(message.chat.id, message.id-1)
       bot.delete_message(message.chat.id, message_id - 2)
    except:
        pass

#функция отправляет в канал вызов администратора
def admins_call(id, bot, chanel_id ,message):

    card_user_buf = []
    if message.from_user.username != None:
        card_user_buf.append(message.from_user.username)
    else:
        pass
    if message.from_user.first_name != None:
        card_user_buf.append(message.from_user.first_name)
    else:
        pass
    if message.from_user.last_name != None:
        card_user_buf.append(message.from_user.last_name)
    else:
        pass
    if message.from_user.id != None:
        card_user_buf.append(message.from_user.id)
    else:
        pass

    bot.send_message(chanel_id, f'Необходима помощь пользователю :{card_user_buf[0]}', reply_markup = technical(card_user_buf[0],id))



#функция для ответов пользователю
def question(message):
    text_ = message.text
    card_user_buf = []
    for list in list_answers:
        for key, val in list.items():
            if key == text_:
                qw(message.chat.id, bot, val)
    if text_ not in list_answers:

        if message.from_user.username != None:
            card_user_buf.append(message.from_user.username)
        else:
            pass
        if message.from_user.first_name != None:
            card_user_buf.append(message.from_user.first_name)
        else:
            pass
        if message.from_user.last_name != None:
            card_user_buf.append(message.from_user.last_name)
        else:
            pass
        if message.from_user.id != None:
            card_user_buf.append(message.from_user.id)
        else:
            pass
        if text_ != '':
            admin_servic(message.chat.id, admins_chanel, bot,f'пользователь: {card_user_buf[0]}\nвопрос: {text_}' )


def answer(message):
    print(message)

def application(message):
    print(message)
    bot.send_message(message.chat.id)

def calculation():
    pass