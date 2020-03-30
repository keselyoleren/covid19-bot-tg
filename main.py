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


response = requests.get("https://api.kawalcorona.com/indonesia/").json()

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'lihat update penyebaran virus corona di setiap daerah  /indonesa /bali /aceh /jambi /jatim /jateng /jabar /jakarta /jogja /papu /riau /sumbar /banten')

@bot.message_handler(commands=['indonesia'])
def indonesia_info(message):
    get_info_covid19 = requests.get("https://api.kawalcorona.com/indonesia").json()
    heder = "\033 Update covid19 \033 \n \n"
    for data in get_info_covid19:
        bot.reply_to(message, heder + " \n Wilayah :" + data['name'] + "\n positif : " + data['positif']  + "\n Sembuh : " + data['sembuh'] + "\n meninggal :" + data['meninggal'])


@bot.message_handler(commands=['jatim'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Jawa Timur":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                bot.reply_to(message, msg)

@bot.message_handler(commands=['jabar'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Jawa Barat":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                bot.reply_to(message, msg)

@bot.message_handler(commands=['jateng'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()
    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Jawa Tengah":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                bot.reply_to(message, msg)

@bot.message_handler(commands=['jakarta'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "DKI Jakarta":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)

@bot.message_handler(commands=['banten'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Banten":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)

@bot.message_handler(commands=['bali'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Bali":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)


@bot.message_handler(commands=['jogja'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Daerah Istimewa Yogyakarta":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)

@bot.message_handler(commands=['papua'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Papua":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)

@bot.message_handler(commands=['sumbar'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Sumatra Barat":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)

@bot.message_handler(commands=['lampung'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Lampung":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)

@bot.message_handler(commands=['aceh'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Aceh":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)


@bot.message_handler(commands=['riau'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Riau":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)




@bot.message_handler(commands=['jambi'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Jambi":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)

@bot.message_handler(commands=['maluku'])
def jatim_info(message):
    res = requests.get('https://api.kawalcorona.com/indonesia/provinsi').json()

    for a in res:
        for key, val in a.items():
            if val['Provinsi'] == "Maluku":
                msg = "  Update covid19  \n \n Wilayah: " + val['Provinsi']  + "\n positif: " + str(val['Kasus_Posi']) + "\n Sembuh : " + str(val['Kasus_Semb']) + "\n Meninggal : " + str(val['Kasus_Meni']) 
                
                bot.reply_to(message, msg)

























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