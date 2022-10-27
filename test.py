import requests
from pprint import pprint

api_key = '92befc00c91f41cac7e0dd91aa4a144e'
#def test(city, API=api_key):
req = requests.get( f'http://api.openweathermap.org/geo/1.0/direct?q=rivne&limit=1&appid={api_key}')
pprint(req.json())
print('\U0001F600')
#test('london')