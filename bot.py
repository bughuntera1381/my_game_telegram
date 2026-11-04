import telebot
import os
from flask import Flask

# توکن ربات جدیدت (mmd2gameoldbot) رو اینجا بذار
BOT_TOKEN = '9177653819:AAGM6Qiu2nORwcntM3BSbNNyv27uYlgkaus'
bot = telebot.TeleBot(BOT_TOKEN)

# یه دستور ساده برای تست
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام داداش! من به سرور وصل هستم.")

# بخشی که Render لازم داره تا ربات رو خاموش نکنه
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: bot.polling(none_stop=True), daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
