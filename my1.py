import os
import telebot
from flask import Flask, request
from telebot import types

TOKEN = "2122815268:AAHXEstUmm_bFxw8yiw0HHOYjnn4MdvZ2ek"
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

name = ''
age = 0


@bot.message_handler(commands=['start', 'help', 'погнале'])
def command_help(message):
    bot.reply_to(message, "Привмяу, че кого?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDYZBhpMKiuYTgWQSnfxq8gJVsUf3c2gAC3AsAAmbEWEtneEZg3zITKCIE")

    if message.text == 'хех':
        bot.reply_to(message, 'хых')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, 'Ты кто?')
        bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Скока лет?')
    bot.register_next_step_handler(message, reg_age)


def reg_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Ой, что-то не так... тебе нужно вводить возраст цифрами.")

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="ды", callback_data="yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="ноуп", callback_data="no")
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + " годиков. И ты " + name + "?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "норм, сохраню")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "а чё?")
        bot.send_message(call.message.chat.id, 'Ты кто?')
        bot.register_next_step_handler(call.message, reg_name)


bot.polling()
