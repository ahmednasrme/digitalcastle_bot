import telebot
import os
import datetime
from dotenv import load_dotenv, dotenv_values
from telebot import util

load_dotenv()

def send_message(file_path):
    bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
    file = open(file_path,'r',encoding='utf-8')
    text = file.read()
    bot.send_message(os.getenv('TGReciptor'),text,parse_mode="Markdown")
    file.close()
    return True

if __name__ == "__main__":
    file_path = f'data/message{datetime.datetime.date(datetime.datetime.now())}.md'
    send_message(file_path)
    print('message sent')