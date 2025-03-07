import telebot
import requests
import json
import os
from dotenv import load_dotenv, dotenv_values
from telebot import util

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(chat_types=['private'],commands=['start','about'])
def intro(message):
    bot.send_message(message.chat.id,
                     '''
                     مرحبا بك، أنا مساعد آلي\n
                       أدير قناة القلعة الرقمية، اجمع الأخبار التقنية، ومرتبط بمحرك ذكاء اصطناعي للمساعدة..يسعدني أن أقدم لك الدعم والمساعدة في مجالات حماية الخصوصية الرقمية وتعلّم موضوعات الأمن السيبراني
                     ''',
                     parse_mode="Markdown")

@bot.message_handler(func=lambda msg: True)
def sinkhole(message):
    print(message)
    
bot.infinity_polling()