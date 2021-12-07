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


@bot.message_handler(commands=['start', 'help', 'погнале'])
def command_help(message):
    bot.reply_to(message, "Привмяу, че кого?")


@bot.message_handler(commands=['Когда', 'когда', 'Туса', 'туса', 'party'])
def command_help(message):
    bot.reply_to(message, "Все собираемся у Лешрака 11 декабря в районе 7–8 часиков на слойки.\n\nПашар, возьми шурик.\n\nКатяра, напиши, что надо на слойки.")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDZithqEibdkEMdfQwFqCihlP_XzwZmQACYQEAAixg9RwjJ4QiDIzt8CIE")


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


@bot.message_handler(commands=['Санта', 'санта', 'santa', 'Santa'])
def command_help(message):
    bot.reply_to(message, "Тайный Санта 🎅\n\nНас будет 6 человек: Лёшар, Юля, Даша, Пашап, Пашар и Катяра\n\nЯ напишу бумажки, где будут имена каждого, каждый будет в тайной комнате тянуть бумажку и смотреть кто там. Если ты сам, то бери другую.\n\nБумажку брать с собой и никому не рассказывать кто там. Цена подарка примерно в районе 1000–1500₽. Если ты испытываешь теплые чувства к этому человеку, то можно больше.\n\nПодарки будем дарить на тусе в НГ или где-то после НГ, как получится.")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDbZZhrz6w6JhcgaXimrq0SiofCB168wACOgADobYRCBvFr5Ov1gHjIgQ")

bot.polling()
