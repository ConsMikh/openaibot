__version__ = 'v1.0'

import os
import openai
import telebot

openai.api_key = os.getenv("OPENAI_API_KEY")
bot_key = os.getenv("cmikh_openai_chat_bot")

bot = telebot.TeleBot(bot_key)

messages = [{"role": "system", "content":
             "You are a intelligent assistant."}]


@bot.message_handler(func=lambda _: True)
def message_handler(mess):

    message = mess.text
    from_user = mess.from_user.id
    try:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        bot.send_message(chat_id=mess.from_user.id,
                         text=chat.choices[0].message.content)
    except Exception as e:
        bot.send_message(chat_id=from_user,
                         text=e)


bot.polling()


# models = openai.Model.list()

# # print the first model's id
# print(models)
