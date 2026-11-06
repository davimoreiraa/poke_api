import requests

url = 'https://pokeapi.co/api/v2/pokemon-species/'

def get_amount_pokemons():
    response = requests.get(url).json()
    return response['count']