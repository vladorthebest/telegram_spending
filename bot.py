import telebot
from config import TOKEN
from bd import Data_Base

bot = telebot.TeleBot(TOKEN)

#keyboard
menu_keyboard = telebot.types.ReplyKeyboardMarkup(False, False)
menu_keyboard.row('Продукты')
menu_keyboard.row('Подарок')
menu_keyboard.row('Путешествие')

#start bot
@bot.message_handler(commands='start')
def main(message):
    bot.send_message(message.chat.id,
    """Я бот капиталист\n
Посчитаю твои убытки, а может заработки\n
Хотя зная тебя я буду считать рассходы)))""",
    reply_markup=menu_keyboard  #add keyboard
    )


#command 'result' - sends value your bank account category
@bot.message_handler(commands="result")
def ask(message):
    bot.send_message(message.chat.id, "Какой счет интересует?", reply_markup=menu_keyboard) #input category
    bot.register_next_step_handler(message, get_bd) #next step

def get_bd(message):
    all_spending = base.get_all_cost(message.text, message.chat.id) #get value in the DataBase
    bot.send_message(message.chat.id, f"{message.text} : {all_spending}") #send value in the user


#text - add new record in the DataBase
@bot.message_handler(content_types=['text'])
def ask(message):
    message_typ = message #input category record
    bot.register_next_step_handler(message, plus, message_typ)
    

def plus(message, message_typ):
    try:
        lost = float(message.text) #user result
        
        base.add_in_bd(lost, message_typ.text, message.chat.id) #add record in the DataBase
        bot.send_message(message.chat.id, f"Запись добавлена!\n{message_typ.text}:{lost}") #send alert about add record for user 


    #if user result doesn`t float/int
    except:
        bot.send_message(message.chat.id, "Цифры вводить нужно!") 
        bot.register_next_step_handler(message, plus, message_typ) #again start this function
     
   

base = Data_Base()
bot.polling(non_stop=True)