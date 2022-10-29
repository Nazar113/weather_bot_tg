from weather_service import get_weather
from pprint import pprint


def get_weather_items(data_weather):
    def createWeatherItem(item):
      return {
        'time': item['dt_txt'],
        'temp': item['main']['temp'],
        'description': item['weather'][0]['description'],
        'visibility': item['visibility'],
        'pop': item['pop'],
        'wind_speed': item['wind']['speed']
      }
      
    return map(createWeatherItem, data_weather['list'])


def get_message(data_weather):
    main_info = {
        'country': data_weather['city']['country'],
        'city': data_weather['city']['name'],
        'population': data_weather['city']['population'],
    }
    
    txt = f'{main_info["country"]}, {main_info["city"]}, <b>Населення:</b> {main_info["population"]}\n\n' \
    
    weather_items = get_weather_items(city)
    for weatherItem in weather_items:
        txt += f"({weatherItem['time']}, {weatherItem['temp']},{weatherItem['description']}, {weatherItem['visibility']}, {weatherItem['pop']}, {weatherItem['wind_speed']})"
        txt += '\n\n'
    return txt
