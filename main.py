import telebot

TOKEN = '976466335:AAHOa7DtAhim0NImttQye5xLQf7c0_bPevg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Бот создан Кадыровым Бексултаном!')

bot.polling()