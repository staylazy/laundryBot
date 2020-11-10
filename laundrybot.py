import telebot
import db 
bot = telebot.TeleBot('1480199090:AAGl4OdDzOH3cpyDGunLeQbVkCFHzK6Fw9s')

# все это счастье в класс чтобы было прикольно
# команды q aq dq 
# по команде dq сдвинуть базу и удалить человека из жизни 
# хачу кнопки
# q выдает всю очередь
# aq добавить себя после aq спрашивать да нет номер стиралки и тип стирки
# узнать время стирки для каждого типа 
a = [{'id': 1, 'user': 'Pidor baba', 'queue_date': 1, 'machine_num':1}, 
     {'id': 1, 'user': 'Pidor baba', 'queue_date': 1, 'machine_num':1} ]
def q():
    pass

@bot.message_handler(commands=['start','help'])
def start(message):
    if message.text == '/start':
        bot.reply_to(message,'Привет!') # напиши хелп чтобы узнать что я могу
    if message.text == '/help':
        bot.reply_to(message,'То - то ') # расписать команды бота 

@bot.message_handler(commands=['q', 'aq'])
def queue(message):
    if message.text == '/q':
        bot.reply_to(message,'Сейчас расскажу всё, что знаю!')
        q()



    


bot.polling()
