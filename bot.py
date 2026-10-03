import os
from dotenv import load_dotenv
import telebot
import requests
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello! Commands:\n/time\n/weather Cairo")

@bot.message_handler(commands=["time"])
def time_cmd(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.reply_to(message, now)

@bot.message_handler(commands=["weather"])
def weather(message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.reply_to(message, "Usage: /weather Cairo")
        return
    city = parts[1]
    try:
        url = f"https://wttr.in/{city}?format=j1"
        now = requests.get(url, timeout=10).json()["current_condition"][0]
        text = f"{city}: {now['temp_C']} C, {now['weatherDesc'][0]['value']}"
        bot.reply_to(message, text)
    except Exception:
        bot.reply_to(message, "Could not get weather.")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "You said: " + message.text)

print("Bot is running...")
bot.infinity_polling()
