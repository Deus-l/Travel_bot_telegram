import telebot
from telebot import types
from yan import get_local
from main import data_base
from telebot import types

token = "1637447083:AAEAqVQ1C0S0caxJYYrm5u9mNr-4FYQV-_o"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.row(button_geo,'/info')
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и отправь мне свое местоположение", reply_markup=keyboard)


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        #print(message.location)
        bot.send_message(message.chat.id,"Теперь напиши сколько у тебя есть времени в минутах")
        #print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude)
        #bot.send_location(message.from_user.id, 59.938924, 30.315311)

        #start time_for_drive
        k = bot.register_next_step_handler(message, time_for_drive)
        global user_addres
        user_addres = (get_local(message.location.latitude, message.location.longitude))

       # print(user_addres)

@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.chat.id,"Отправь мне свое место положение, напиши сколько у тебя есть времени и я найду интересные для тебя места.")

def time_for_drive(message):
    #считывание времени пользователя
    try:
        user_time = int(message.text)
        information = data_base(user_addres, user_time)
        bot.send_message(message.chat.id,information[1])
        bot.send_location(message.from_user.id, information[2], information[3])
    except:
        bot.send_message(message.chat.id, 'не удалось определить время поездки.')

bot.polling()