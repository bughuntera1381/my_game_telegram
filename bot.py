import telebot
import os
from flask import Flask
import time

BOT_TOKEN ='9177653819:AAGM6Qiu2nORwcntM3BSbNNyv27uYlgkaus'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['play'])
def send_game(message):
    bot.send_game(chat_id=message.chat.id, game_short_name='my_game')

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.game_short_name == 'my_game':
        bot.answer_callback_query(callback_query_id=call.id, url='https://bughuntera1381.github.io/game/')

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=20)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5) # اگر خطایی داد، ۵ ثانیه صبر میکنه و دوباره تلاش میکنه

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))