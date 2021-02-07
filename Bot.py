import telebot
import User
import Expenditure

token = "1627587497:AAHhsD5XTu4m_A5ZQUdC6yXisUdyOfXrzfk"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Кулити")


bot.polling()
