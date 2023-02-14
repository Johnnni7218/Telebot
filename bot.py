
import telebot
from config import *
from extensions import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def instruction(message: telebot.types.Message):
    text = 'Чтобы начать работу введите данные в следующем порядке: \n \
<название валюты> <валюту в которую перевести> <колличество переводимой валюты>\n' \
'Увидеть доступные валюты можно с помощью команды: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'ПРИМЕР ВВОДА: RUB USD 10\n\n' \
           'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        vvod = message.text.split()
        if len(vvod) != 3:
            raise ConvertionException('Неверное количество параметров!')
        base, quote, amount = vvod
        if base == quote:
            raise ConvertionException('Введена одинаковая валюта!')
        sum_price = Convertor.prices(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя - {e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка передачи информации - {e}')
    else:
        bot.reply_to(message, f'Цена {amount} {base} в {quote} = {sum_price}')


bot.polling()

