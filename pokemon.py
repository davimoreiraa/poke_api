import requests

url = 'https://pokeapi.co/api/v2/pokemon/1/'

response = requests.get(url).json()

print(response['name'])
