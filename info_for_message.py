from weather_service import get_weather
from pprint import pprint


def get_info(city):
    data_weather = get_weather(city)
    pprint(data_weather)

    #txt = data_weather['city']['name'] + data_weather['city']['country'] + 'Населення: ' data_weather['city']['population']'\n\n'
    #
    # for i in range(6):
    #     txt+= data_weather['list'][i]['dt_txt']'\n'        #time
    #     txt+= data_weather['list'][i]['weather'][0]['description'] + 'Температура: 'data_weather['list'][i]['main']['temp']'°C\n'
    #     txt+= 'Середня видимість: 'data_weather['list'][i]['visibility']'\n' #Середня видимість
    #     txt+= 'Імовірність опадів: 'data_weather['list'][i]['pop']'\n'           #Імовірність опадів
    #     txt+= 'Швидкість вітру: 'data_weather['list'][i]['wind']['speed'])


    data_message = {
        'country': data_weather['city']['country'],
        'city': data_weather['city']['name'],
        'population': data_weather['city']['population'],
        'description': [],
        'time': [],
        'temp': [],
        'visibility': [],       #середня видимість
        'pop': [],         #Імовірність опадів
        'wind_speed': []
    }

    for i in range(6):
        data_message['time'].append(data_weather['list'][i]['dt_txt'])
        data_message['temp'].append(data_weather['list'][i]['main']['temp'])
        data_message['description'].append(data_weather['list'][i]['weather'][0]['description'])
        data_message['visibility'].append(data_weather['list'][i]['visibility']) #Середня видимість
        data_message['pop'].append(data_weather['list'][i]['pop'])               #Імовірність опадів
        data_message['wind_speed'].append(data_weather['list'][i]['wind']['speed'])

    return data_message


def get_message(city):
    data_message = get_info(city)

    txt = f'{data_message["country"]}, {data_message["city"]}, <b>Населення:</b> {data_message["population"]}\n\n' \

    for i in range(6):
        txt += f"({data_message['time'][i]}, {data_message['temp'][i]},{data_message['description'][i]}, {data_message['visibility'][i]}, {data_message['pop'][i]}, {data_message['wind_speed'][i]})\n\n"
    return txt