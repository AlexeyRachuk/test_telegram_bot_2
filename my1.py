import os
import time
from multiprocessing.context import Process
import schedule
import telebot
from flask import Flask, request

TOKEN = "2122815268:AAHXEstUmm_bFxw8yiw0HHOYjnn4MdvZ2ek"
APP_URL = f"https://raccoonmehbot.herokuapp.com/{TOKEN}"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


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


#@bot.message_handler(commands=['start', 'help', 'погнале'])
#def command_help(message):
#   bot.reply_to(message, "Привмяу, че кого?")


@bot.message_handler(commands=['Когда', 'когда', 'Туса', 'туса', 'party'])
def command_help(message):
    bot.reply_to(message,
                 "Собираемся 5 числа, по времени определимся чуть позже.\n\nПредлагаю ничего не готовить, а заказать еду, а я думаю чём-нибудь покрепче 🤔")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDhK5hv1RjaHAO6rxMiXu6mHRpmfUpoQACMRgAAihWUEmMynP2r9sKQyME")


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
    bot.reply_to(message,
                 "Тайный Санта 🎅\n\nПокупаем подарочки 🌚\n\nЦена в районе 1000–1500₽, но если хотите, можно и больше.\n\nДарим скорее всего 5 января.\n\nКста я уже купил подарок х)")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDhLBhv1SJUPiz53vkKnWh5my78uKlvwACIBMAAm7LuEnGA10qj48M_CME")

@bot.message_handler(regexp="НГ|нг|новым годом|")
def command_help(message):
    bot.reply_to(message, "С новым годом! ✨")

if __name__ == '__master__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


bot.polling(none_stop=True, interval=0)
