from bot import telegram_chatbot
import gizoogle
import requests

bot = telegram_chatbot("config.cfg")
# print(bot)
# bot.send_message('reply,')


def make_reply(msg):
    reply = None
    if msg is not None:
        reply = gizoogle.text(msg)
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["description"]
    print(updates)
    if updates:
        for item in updates:
            print(item)
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)