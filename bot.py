import telebot
import config


API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)

class MyClass:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __str__(self):
        return f"Данные экземпляра: Данные номер 1:{self.value1}, данные номер 2:{self.value2} "
        

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am UralsBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
@bot.message_handler(commands=['info'])
def send_inf(message):
    bot.reply_to(message, """\
I am UralsBot.
I am created by Ural developer\
""")
@bot.message_handler(commands=['create'])
def create_instance(message): 
        args = message.text.split()[1:]  
        if len(args) != 2:
            bot.reply_to(message, "Пожалуйста, введите два значения. Пример: /create значение1 значение2")
        value1 = args[0]
        value2 = args[1]
        instance = MyClass(value1, value2)
        bot.reply_to(message, f"Экземпляр создан: {instance}")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()