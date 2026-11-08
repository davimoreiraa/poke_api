import pymysql
import dotenv
import os
import requests

dotenv.load_dotenv()

con = pymysql.connect(
    host=os.environ['HOST'],
    user=os.environ['USER'],
    password=os.environ['PASSWORD'],
    database=os.environ['DATABASE'],
    cursorclass=pymysql.cursors.DictCursor
)

with con:
    with con.cursor() as cursor:
        url = "https://pokeapi.co/api/v2/pokemon?limit=1"    
        response = requests.get(url).json()

        for pokemon in response['results']:
            url_pokemon = pokemon['url']
            dados_pokemon = requests.get(url_pokemon).json()
            print(dados_pokemon['stats'])
            
        # pronto para executar