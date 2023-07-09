__version__ = 'v1.2'

import os
import openai
import telebot

from openai.error import InvalidRequestError

from sessions import Session

openai.api_key = os.getenv("OPENAI_API_KEY")
bot_key = os.getenv("cmikh_openai_chat_bot")

bot = telebot.TeleBot(bot_key)


@bot.message_handler(commands=['info'])
def info(mess):
    models = [model.id for model in openai.Model.list().data]
    models_name = '\n'.join(model for model in models)
    bot.reply_to(
        mess, f"Версия {__version__}\n\nДоступные модели:\n{models_name}")


@bot.message_handler(commands=['tokens', 't', 'токены', 'т'])
def tokens(mess):

    from_user = mess.from_user.id

    if Session.sessions_list.get(from_user, False):
        session = Session.sessions_list[from_user]
        bot.reply_to(
            mess, f"Количество токенов в сессии: {session.total_tokens}\nМаксимум токенов в сессии: 4097")
    else:
        bot.reply_to(mess, f"Сессия не начата")


@bot.message_handler(commands=['clear', 'отчистить', 'очистить'])
def clear_session(mess):

    from_user = mess.from_user.id

    if Session.sessions_list.get(from_user, False):
        session = Session.sessions_list[from_user]
        session.clear_session()
        bot.reply_to(mess, f"Сессия сброшена")
    else:
        bot.reply_to(mess, f"Сессия не начата")


@bot.message_handler(func=lambda mess: True)
def message_handler(mess):

    message = mess.text
    from_user = mess.from_user.id

    if Session.sessions_list.get(from_user, False):
        session = Session.sessions_list[from_user]
        session.add_message_to_promt(role='user', message=message)
        # print(session)
    else:
        session = Session(from_user)
        session.add_message_to_promt(role='user', message=message)
        # print(session)

    try:
        chat = openai.ChatCompletion.create(
            model=session.model, messages=session.promt
        )
        reply = chat.choices[0].message.content
        session.add_message_to_promt(role="assistant", message=reply)
        bot.send_message(chat_id=from_user,
                         text=reply)
    except InvalidRequestError as e:
        bot.send_message(chat_id=from_user,
                         text=e)
        session.clear_session()
        bot.send_message(chat_id=from_user,
                         text=f"Сессия сброшена")

    except Exception as e:
        bot.send_message(chat_id=from_user,
                         text=e)


bot.polling()


# models = openai.Model.list()

# # print the first model's id
# print(models)
