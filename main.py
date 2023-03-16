import telebot


API_TOKEN = '5427501008:AAGkjCYNVzTDkUNLYKxqeaJ2p6cX2a0cCEA'  # @youtube_scraping_bot
id_my = 5124962240

bot = telebot.TeleBot(API_TOKEN)
print('Start')

@bot.message_handler(commands=['start'])
def start(message):
    bot.forward_message(id_my, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Запрос в обработке, пожалуйста ожидайте')
@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    bot.forward_message(id_my, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Запрос в обработке, пожалуйста ожидайте')


bot.polling()
