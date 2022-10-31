#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import psycopg2
from flask import Flask, request

API_KEY = '5603401902:AAFLpdln-_Y0EHdrGDHiKl2mO1UjOkaGZY8'
bot = telebot.TeleBot(API_KEY)
manager = 357214910
Group = -885134397
Flag = False
server = Flask(__name__)


# API function

@bot.message_handler(commands=['start'])
def start_command(message):
    start(message)


@bot.message_handler(commands=['help'])
def help_command(message):
    start(message)


@bot.message_handler(commands=['send'])
def support_command(message):
    send(message)


@bot.message_handler(content_types=['text'])
def mmm(message):
    print(message)


# requirement function


def send(message):
    msg = bot.send_message(message.chat.id, 'لطفا پیام خود را ارسال کنید ')
    bot.register_next_step_handler(msg, send_message)


def send_message(message):
    text = message.text
    bot.send_message(Group, text)
    manager_text = str(message.from_user.id) + '\n' + text+ '\n' + message.from_user.username
    bot.send_message(manager, manager_text)
    


def delete(message):
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


# typical function

def start(message):
    bot.send_message(message.chat.id, 'برای ارسال پیام در گروه دستور /send را ارسال کنید')
    print(message)


# server's function

@server.route('/' + API_KEY, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://aut-tutoring.herokuapp.com/' + API_KEY)
    return "!", 200


def main():
    print('running')
    bot.infinity_polling()
    # server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


if __name__ == '__main__':
    main()
