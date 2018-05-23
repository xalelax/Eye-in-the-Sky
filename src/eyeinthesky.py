import sys
import time
import telepot
from telepot.loop import MessageLoop

"""
usage: $ python eyeinthesky.py <token> <ownerId>

This bot will reply only to a single owner.

"""


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if chat_id != ownerId:
        bot.sendMessage(chat_id, "Sorry, you can not control me.")
        return
    if command == "\temp":
        bot.sendMessage(chat_id, "Temperature = ")
    elif command == "\pic":
        bot.sendMessage(chat_id, "Sending picture")
    else:
        bot.sendMessage(chat_id, "Huh???")


try:
    token = sys.argv[1]
    ownerId = int(sys.argv[2])
except IndexError:
    print("Initialization error")
    sys.exit(0)

bot = telepot.Bot(token)
bot.getMe()

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
