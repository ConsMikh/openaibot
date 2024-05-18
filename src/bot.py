__version__ = 'v1.4.2'

import os
import json

import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# from telebot import apihelper # Использовать для подключения прокси

from sessions import Session, SessionException


bot_key = os.getenv("OPENAI_CHAT_BOT")

bot = telebot.TeleBot(bot_key)


def choise_context():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Сбрасывать контекст",
                                    callback_data="{\"command\":\"context\",\"param\":\"fin\"}"),
               InlineKeyboardButton("Накапливать контекст",
                                    callback_data="{\"command\":\"context\",\"param\":\"inf\"}"),
               )
    return markup


def choise_model():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("gpt-3.5-turbo",
                                    callback_data="{\"command\":\"model\",\"param\":\"gpt-3.5-turbo\"}"),
               InlineKeyboardButton("gpt-3.5-turbo-16k",
                                    callback_data="{\"command\":\"model\",\"param\":\"gpt-3.5-turbo-16k\"}"),
               InlineKeyboardButton("gpt-4",
                                    callback_data="{\"command\":\"model\",\"param\":\"gpt-4\"}"),
               InlineKeyboardButton("gpt-4-0613",
                                    callback_data="{\"command\":\"model\",\"param\":\"gpt-4-0613\"}"),
               InlineKeyboardButton("gpt-4o",
                                    callback_data="{\"command\":\"model\",\"param\":\"gpt-4o\"}"),
               InlineKeyboardButton("gpt-4-turbo",
                                    callback_data="{\"command\":\"model\",\"param\":\"gpt-4-turbo\"}"),
               ),
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    message = json.loads(call.data)
    from_user = call.from_user.id
    bot.answer_callback_query(call.id, show_alert=False)
    if Session.sessions_list.get(from_user, False):
        session = Session.sessions_list[from_user]
    else:
        session = Session(from_user)

    if message['command'] == 'model':
        session.model = message['param']
        bot.send_message(chat_id=from_user,
                         text='Moдель установлена')
    if message['command'] == 'context':
        session.ses_type = message['param']
        bot.send_message(chat_id=from_user,
                         text=f"Режим установлен")


@bot.message_handler(commands=['model'])
def model(mess):
    bot.send_message(mess.chat.id, "Выберите модель из списка",
                     reply_markup=choise_model())


@bot.message_handler(commands=['info'])
def info(mess):
    from_user = mess.from_user.id

    session_info = Session.sessions_list[from_user].__repr__(
    ) if Session.sessions_list.get(from_user, False) else 'Сессия не создана'

    bot.send_message(chat_id=from_user,
                     text=f"Версия {__version__}\n\nДоступные команды:\n"
                     "/clear - очистить сессию (остается только системный промт)\n"
                     "/model - выбрать модель для сессии\n"
                     "/context - выбрать режим работы с контекстом\n"
                     "/system [текст] - поменять системный промт на [текст] (сессия будет очищена)\n"
                     "/session - вывести информацию о сессии\n"
                     f"/t, /т, /tokens - вывести количество токенов в сессии\n\n{session_info}")


@bot.message_handler(commands=['sessions'])
def sessions(mess):
    from_user = mess.from_user.id
    text = '\n'.join([ses.__repr__()
                     for ses in Session.sessions_list.values()])
    bot.send_message(chat_id=from_user,
                     text=text if len(text) > 0 else 'Нет активных сессий')


@bot.message_handler(commands=['session'])
def sessions(mess):
    from_user = mess.from_user.id
    text = ""
    if Session.sessions_list.get(from_user, False):
        text = Session.sessions_list[from_user].__repr__()

    bot.send_message(chat_id=from_user,
                     text=text if len(text) > 0 else 'Нет активных сессий')


@bot.message_handler(commands=['system'])
def system(mess):

    from_user = mess.from_user.id
    system_promt = ' '.join(mess.text.split(' ')[1:])
    if len(system_promt) > 0:
        if Session.sessions_list.get(from_user, False):
            session = Session.sessions_list[from_user]
            session.system_promt = system_promt
            session.promt = [{"role": "system", "content": f"{system_promt}"}]

        else:
            session = Session(from_user, system_promt=system_promt)
        bot.send_message(chat_id=from_user,
                         text='Системный промт установлен')
    else:
        bot.send_message(chat_id=from_user,
                         text='Системный промт не задан')


@bot.message_handler(commands=['tokens', 't', 'токены', 'т'])
def tokens(mess):

    from_user = mess.from_user.id

    if Session.sessions_list.get(from_user, False):
        session = Session.sessions_list[from_user]
        bot.send_message(
            chat_id=from_user,  text=f"Количество токенов в сессии: {session.total_tokens}")
    else:
        bot.reply_to(mess, f"Сессия не начата")


@bot.message_handler(commands=['clear', 'отчистить', 'очистить'])
def clear_session(mess):

    from_user = mess.from_user.id

    if Session.sessions_list.get(from_user, False):
        session = Session.sessions_list[from_user]
        session.clear_session()
        bot.send_message(chat_id=from_user,  text=f"Сессия сброшена")
    else:
        bot.send_message(chat_id=from_user,  text=f"Сессия не начата")


@bot.message_handler(commands=['context'])
def set_sesion_mode(mess):
    bot.send_message(mess.chat.id, "Выберите режим работы с контекстом",
                     reply_markup=choise_context())


@bot.message_handler(func=lambda mess: True)
def message_handler(mess):

    message = mess.text
    from_user = mess.from_user.id

    if Session.sessions_list.get(from_user, False):
        session = Session.sessions_list[from_user]
        session.add_message_to_promt(role='user', message=message)

    else:
        session = Session(from_user)
        session.add_message_to_promt(role='user', message=message)

    try:
        reply = session.send_promt()
    except SessionException as e:
        reply = f"Ошибка OpenAI API: {repr(e)[:150]}\n\nСессия очищена"
    except Exception as e:
        reply = f"Ошибка выполения: {repr(e)[:150]}"
    finally:
        bot.send_message(chat_id=from_user,
                         text=reply)


bot.infinity_polling()
