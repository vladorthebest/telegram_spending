import telebot
from config import TOKEN
from bd import Data_Base

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands='result')
def main(message):

    result = base.get_all_cost()
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands='add')
def set_expensive(message):
    bot.send_message(message.chat.id, "Сколько вы потратили?")
    bot.register_next_step_handler(message, add_to_bd)

def add_to_bd(message):
    base.add_in_bd(int(message.text))
    bot.send_message(message.chat.id, "Запись добавлена!")



base = Data_Base()
bot.polling(non_stop=True)