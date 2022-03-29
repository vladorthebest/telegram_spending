import telebot
from config import TOKEN
from bd import Data_Base

bot = telebot.TeleBot(TOKEN)

#keyboard
menu_keyboard = telebot.types.ReplyKeyboardMarkup(False, False)
menu_keyboard.row('Продукты')
menu_keyboard.row('Подарок')
menu_keyboard.row('Путешествие')

@bot.message_handler(commands='start')
def main(message):
    bot.send_message(message.chat.id,
    """Я бот капиталист\n
Посчитаю твои убытки, а может заработки\n
Хотя зная тебя я буду считать рассходы)))""",
    reply_markup=menu_keyboard
    )


@bot.message_handler(commands="result")
def ask(message):
    bot.send_message(message.chat.id, "Какой счет интересует?", reply_markup=menu_keyboard)
    bot.register_next_step_handler(message, get_bd)

def get_bd(message):
    all_spending = base.get_all_cost(message.text)
    bot.send_message(message.chat.id, f"{message.text} : {all_spending}")


@bot.message_handler(content_types=['text'])
def ask(message):
    typ = message.text
    bot.register_next_step_handler(message, plus, typ)

def plus(message, typ):
    try:
        lost = float(message.text)
        print(typ, lost)
        base.add_in_bd(lost, typ)
        bot.send_message(message.chat.id, f"Запись добавлена!\n{typ}:{lost}")

    except:
        bot.send_message(message.chat.id, "Цифры вводить нужно!")
        bot.register_next_step_handler(message, typ, plus, typ)
     
   

base = Data_Base()
bot.polling(non_stop=True)