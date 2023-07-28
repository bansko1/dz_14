import os
import telebot
from parser import parce

TOKEN = '6205794405:AAEbD8e5Rp4kZqqdrcMp_1NmB_I3hxOdhZE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Телеграм бот - парсер новостей приветствует нового пользователя!")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Парсер читает новости сайта mos.ru. Мспользуются команды: /start, /help, /parser, /admin")


# @bot.message_handler(commands=['timer'])
# def timer(message):
#     for i in range(5):
#         time.sleep(1)
#         bot.send_message(message.chat.id, i + 1)


# @bot.message_handler(commands=['say'])
# def say(message):
#     text = ' '.join(message.text.split(' ')[1:])
#     bot.reply_to(message, f'{text.upper()}!')


@bot.message_handler(commands=['admin'], func=lambda message: message.from_user.id == 5076837299)
def admin(message):
    print(message)
    info = os.name
    bot.reply_to(message, info)


@bot.message_handler(commands=['parser'], func=lambda message: message.from_user.id == 5076837299)
def parser(message):
    # print(message)
    numb = parce()
    number_news = 1
    for it in numb:
        bot.send_message(message.chat.id, f'Новость {number_news}\n *** {it[0]} ***\n{it[1]}')
        number_news += 1


# @bot.message_handler(content_types='text')
# def reverse_text(message):
#     # print(message)
#     text = message.text[::-1]
#     bot.reply_to(message, text)


bot.polling()
