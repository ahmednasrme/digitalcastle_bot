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
    bot.send_message(int(os.getenv('TGReciptor')),text,parse_mode="Markdown")
    return True