import telebot

bot = telebot.TeleBot('YOUR_TOKEN')

@bot.message_handler(commands=['start','help'])
def start(message):
    if message.text == '/start':
        bot.reply_to(message,'Привет!')
    if message.text == '/help':
        bot.reply_to(message,'То - то ')

bot.polling()
