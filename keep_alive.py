# main.py
from flask import Flask
from threading import Thread
import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# === Веб-сервер для keep-alive ===
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive! 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# === Telegram bot ===
TOKEN = "8323998271:AAHWsHZ8Uq-CDC_dDxcdWVVxuGmVJKcc3Js"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я живой бот 🤖")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Ты написал: {text}")

if __name__ == '__main__':
    # Запускаем веб-сервер в отдельном потоке
    thread = Thread(target=run_flask)
    thread.start()

    # Создаём приложение Telegram
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Запускаем Telegram-бота...")
    application.run_polling()