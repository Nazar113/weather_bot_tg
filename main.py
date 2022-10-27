import requests
import telebot
from pprint import pprint
import json

bot = telebot.TeleBot('5709491583:AAESmBOsGDBu6lSECnsU1BeMGMjquBCkyoo')
api_key = '92befc00c91f41cac7e0dd91aa4a144e'

@bot.message_handler(commands=['start'])
def start(message):
    mess = 'Привіт! \n<b>Звідки показати погоду?</b>'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')



@bot.message_handler(content_types=['text'])
def get_user_text(message):

    city = message.text
    req = requests.get( f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}')
    data = req.json()


    bot.send_message(message.chat.id, '\U0001F324', parse_mode = 'html')
    try:
        lat = data[0]['lat']
        lon = data[0]['lon']
    except IndexError:
        bot.send_message(message.chat.id,
                         'Не можу знайти координати \U0001F61E\nПеревірте точність введення назви \U0001F600',
                         parse_mode='html')
        bot.polling(none_stop=True)

    req_weather = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&units=metric&lon={lon}&appid={api_key}')
    data_weather = req_weather.json()

    city_country = data_weather['city']['country']
    city_name = data_weather['city']['name']
    city_pop = data_weather['city']['population']

    time0 = data_weather['list'][0]['dt_txt']
    temp0 = data_weather['list'][0]['main']['temp']

    time1 = data_weather['list'][1]['dt_txt']
    temp1 = data_weather['list'][1]['main']['temp']

    time2 = data_weather['list'][2]['dt_txt']
    temp2 = data_weather['list'][2]['main']['temp']

    time3 = data_weather['list'][3]['dt_txt']
    temp3 = data_weather['list'][3]['main']['temp']
    time4 = data_weather['list'][4]['dt_txt']
    temp4 = data_weather['list'][4]['main']['temp']
    time5 = data_weather['list'][5]['dt_txt']
    temp5 = data_weather['list'][5]['main']['temp']

    mess =f'{city_country}, {city_name}, <b>Населення:</b> {city_pop}\n\n' \
          f'*{time0}\nТемпература повітря: <b>{temp0}\U000000B0C</b>\n\n' \
          f'*{time1}\nТемпература повітря: <b>{temp1}\U000000B0C</b>\n\n' \
          f'*{time2}\nТемпература повітря: <b>{temp2}\U000000B0C</b>\n\n' \
          f'*{time3}\nТемпература повітря: <b>{temp3}\U000000B0C</b>\n\n' \
          f'*{time4}\nТемпература повітря: <b>{temp4}\U000000B0C</b>\n\n' \
          f'*{time5}\nТемпература повітря: <b>{temp5}\U000000B0C</b>\n\n' \

    pprint(data_weather)
    bot.send_message(message.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)



