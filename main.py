import os
import telebot
from flask import Flask, request

TOKEN = "2122815268:AAERhoA2pXtSzVUkXPxmtlC7oEeJOWJWK5U"
APP_URL = f"https://raccoonmehbot.herokuapp.com/{TOKEN}"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

if __name__ == '__master__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


@bot.message_handler(commands=['start'])
def command_help(message):


    bot.reply_to(message, "Привмяу, че кого?")


@bot.message_handler(commands=['Когда', 'когда', 'Туса', 'туса', 'party'])
def command_help(message):
    bot.reply_to(message,
                 "Хз когда собираемся играть в монополию")


@bot.message_handler(commands=['jackbox', 'джекбокс', 'игра', 'game'])
def command_help(message):
    bot.reply_to(message, "https://jackbox.fun/")


@bot.message_handler(regexp="как дела?|Как дела?|делишки|Делишки")
def command_help(message):
    bot.reply_to(message, "У меня норм, а у тебя?")


@bot.message_handler(regexp="геншин|Геншин|Genshin|Genshin Impact")
def command_help(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDaNxhqnFSBq86S1PW4f3uAAFTJHDqzLgAAgkNAAKFgDhL4JDCM58wb7YiBA")


@bot.message_handler(regexp="Спокойной ночи|спокойной ночи|споки|Споки")
def command_help(message):
    bot.reply_to(message, "Спокойной ночи 🌚")


@bot.message_handler(regexp="бот")
def command_help(message):
    bot.reply_to(message, "Привет-привет")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDrDth3wk8UUsMqh1XFKp_gHJyOt1cqwACzwEAAj0N6ATqtWGyHHa6QSME")


bot.polling()
