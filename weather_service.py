import requests
from config import api_key

geocoder_api = 'http://api.openweathermap.org/geo/1.0/direct'
weather_api = 'http://api.openweathermap.org/data/2.5/forecast'


class NotFoundCity(Exception):
    pass


def get_weather(city):
    req_coordinates = requests.get(geocoder_api, params={'q': city, 'appid': api_key})
    data = req_coordinates.json()
    if data == [] or data[0]['lat'] == '' or data[0]['lon'] == '':
        raise NotFoundCity

    req_weather_params = {
        'lat': data[0]['lat'],
        'lon':  data[0]['lon'],
        'units': 'metric',
        'lang': 'ua',
        'appid': api_key
    }

    req_weather = requests.get(weather_api, params=req_weather_params)
    return req_weather.json()
