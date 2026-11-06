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
        url = "https://pokeapi.co/api/v2/pokemon?limit=1026"    
        response = requests.get(url).json()

        for pokemon in response['results']:
            url_pokemon = pokemon['url']
            dados_pokemon = requests.get(url_pokemon).json()
            pokemon_name = dados_pokemon['name']
            pokemon_height = dados_pokemon['height']
            pokemon_weight = dados_pokemon['weight']
            
            url_generation = dados_pokemon['species']['url']
            species_response = requests.get(url_generation).json()
            pokemon_gen = species_response['generation']['name']
            
            sql = """
                UPDATE pokemons
                SET gen = %s,
                height = %s,
                weight = %s
                WHERE name = %s
            """

            cursor.execute(sql, [pokemon_gen, pokemon_height, pokemon_weight, pokemon_name])
        con.commit()

        # pronto para executar