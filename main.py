import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):

 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Random")
    item2 = types.KeyboardButton("How are you?")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Welcome, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Как дела?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично, а ты?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'I don`t know what to say ')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Супер ')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'С кем не бывает')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Как дела?",
                reply_markup=None)
 

    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)