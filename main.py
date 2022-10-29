
import telebot
from info_for_message import get_message

import weather_service
from config import bot_id

import weather_service
bot = telebot.TeleBot(bot_id)


@bot.message_handler(commands=['start'])
def start(message):
    mess = 'Привіт! \n<b>Звідки показати погоду?</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


smiles_dict = {
    'sun_cloud': '\U0001F324',
    'sad_smile': '\U0001F61E',
    'smile_face': '\U0001F600'
}


@bot.message_handler(content_types=['text'])
def message_handler(message):

    city = message.text
    try:
        weather_data = weather_service.get_weather(city)
    except weather_service.NotFoundCity:
        bot.send_message(message.chat.id, 'Не можу знайти координати ', smiles_dict['sad_smile'],'\n''Перевірте точність введення назви ', smiles_dict['smile_face'], parse_mode='html')

    bot.send_message(message.chat.id, smiles_dict['sun_cloud'], parse_mode='html')
    bot.send_message(message.chat.id, get_message(weather_data), parse_mode='html')

    #
    #
    # mess =f'{city_country}, {city_name}, <b>Населення:</b> {city_pop}\n\n' \
    #       f'*{time[0]}\nТемпература повітря: <b>{temp[0]}\U000000B0C</b>\n\n' \
    #       f'*{time[1]}\nТемпература повітря: <b>{temp[1]}\U000000B0C</b>\n\n' \
    #       f'*{time[2]}\nТемпература повітря: <b>{temp[2]}\U000000B0C</b>\n\n' \
    #       f'*{time[3]}\nТемпература повітря: <b>{temp[3]}\U000000B0C</b>\n\n' \
    #       f'*{time[4]}\nТемпература повітря: <b>{temp[4]}\U000000B0C</b>\n\n' \
    #       f'*{time[5]}\nТемпература повітря: <b>{temp[5]}\U000000B0C</b>\n\n' \
    #
    # pprint(data_weather)
    # bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)



