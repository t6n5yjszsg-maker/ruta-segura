import telebot
import os
from flask import Flask, request
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! 👋 Soy RutaSegura Niño 🚨, escribe tu provincia: Cajamarca, Cutervo, Chota, Jaén, San Miguel")

@bot.message_handler(func=lambda message: True)
def responder_usuario(message):
    texto = message.text.lower()
    if "cutervo" in texto or "chiple" in texto:
        bot.reply_to(message, "🔴 ALERTA ROJA: Deslizamiento Cutervo-Chiple. Evita laderas. Ruta segura: Kuntur Wasi")
        bot.send_location(message.chat.id, -6.381400, -78.818900)
    elif "los ajos" in texto or "san miguel" in texto:
        bot.reply_to(message, "🔴 Derrumbe Los Ajos. Dirígete a zonas altas San Miguel")
        bot.send_location(message.chat.id, -6.997200, -78.865800)
    elif "chota" in texto:
        bot.reply_to(message, "⚠️ Lluvias Chota. Evita puentes con alto caudal")
        bot.send_location(message.chat.id, -6.557400, -78.653600)
    elif "jaen" in texto or "jaén" in texto:
        bot.reply_to(message, "⚠️ Riesgo aniegos Jaén. Desconecta llaves térmicas")
        bot.send_location(message.chat.id, -5.708900, -78.807500)
    elif "cajamarca" in texto:
        bot.reply_to(message, "🟢 Monitoreo Cajamarca. Punto seguro:")
        bot.send_location(message.chat.id, -7.163780, -78.500270)
    else:
        bot.reply_to(message, "Escribe: Cutervo, Chota, Jaén, San Miguel o Cajamarca")

@app.route('/', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200

@app.route('/')
def index():
    return "RutaSegura Niño activo"