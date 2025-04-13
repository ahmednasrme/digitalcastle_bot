import telebot
import requests
import json
import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, request

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Add your public webhook URL in the .env file

app = Flask(__name__)

@bot.message_handler(chat_types=['private'], commands=['start', 'about'])
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

@app.route('/' + os.getenv("BOT_TOKEN"), methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    # Set webhook
    bot.remove_webhook()
    print(f"Webhook url: {WEBHOOK_URL}/{os.getenv('BOT_TOKEN')}")
    bot.set_webhook(url=f"{WEBHOOK_URL}/{os.getenv('BOT_TOKEN')}")
    # Run Flask app
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))