import time
import schedule
import requests


def telegram_bot_sendtext(bot_message):
    print(bot_message)
    
    bot_token = '1126681710:AAGmM11NBljhLcER_WoM_q_70m6Vehy1Mr4'
    bot_chatID = '1126681710'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    print(send_text)

    response = requests.get(send_text)
    print(response.json())

    return response.json()


def report():
    my_balance = 10   ## Replace this number with an API call to fetch your account balance
    my_message = "Current balance is: {}".format(my_balance)   ## Customize your message
    telegram_bot_sendtext(my_message)


    
# schedule.every().day.at("19:00").do(report)
report()
# while True:
#     schedule.run_pending()
#     time.sleep(1)