import telebot
import time
import json
import requests

bot_token = '1126681710:AAGmM11NBljhLcER_WoM_q_70m6Vehy1Mr4'
bot = telebot.TeleBot(token=bot_token)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

# def info_covod19():
response = requests.get("https://api.kawalcorona.com/indonesia/").json()
# for data in response:
    # print(data['name'])
# a = response.json()
# print(response)






@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'lihat update penyebaran virus corona dengan cara kirkm @namawilayah contoh @indonesa')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)
    if at_text[1:] == 'indonesia':
        get_info_covid19 = requests.get("https://api.kawalcorona.com/{}".format(at_text[1:])).json()
        heder = "\033 Update covid19 \033 \n \n"
        for data in get_info_covid19:
            bot.reply_to(message, heder + " \n Wilayah :" + data['name'] + "\n positif : " + data['positif']  + "\n Sembuh : " + data['sembuh'] + "\n meninggal :" + data['meninggal'])
    else:
        bot.reply_to(message, 'wilayah tidak di ketahui')
# while True:
#     try:
#         bot.polling()
#     except Exception:
#         time.sleep(15)

bot.polling()