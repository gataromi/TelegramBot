import telebot
import random
from telebot import types
import datetime as dt
import requests
from bs4 import BeautifulSoup
from os import environ

# Parsing

URL = "https://time-in.ru/sun/perm"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

sunrise = soup.find("li", class_ = "sun-info-time-sunrise").text.strip()[6:]
sunset = soup.find("li", class_ = "sun-info-time-sunset").text.strip()[5:]

# BOT

token = environ["telegram_token"]
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Во сколько сегодня восход🌆")
    item2 = types.KeyboardButton("Во сколько сегодня закат🏙")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, который скажет когда восход или закат солнца в Перми".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup) 

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Во сколько сегодня восход🌆':
            bot.send_message(message.chat.id, 'Сегодня ' + str(dt.datetime.today())[:10] + ' восход в ' + str(sunrise))
        elif message.text == 'Во сколько сегодня закат🏙':
            bot.send_message(message.chat.id, 'Сегодня ' + str(dt.datetime.today())[:10] + ' закат в ' + str(sunset))
        else:
            bot.send_message(message.chat.id, 'Я даже не знаю что сказать')

# RUN
            
bot.polling(none_stop = True)
