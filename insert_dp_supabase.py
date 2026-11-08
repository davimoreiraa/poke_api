import dotenv
import psycopg2
import os
import requests

dotenv.load_dotenv()


con = psycopg2.connect(
    dbname= os.environ['SUPABASE_DATABASE'],
    user= os.environ['SUPABASE_USER'],
    password= os.environ['SUPABASE_PASWWORD'],
    host= os.environ['SUPABASE_HOST'],
    port= os.environ['SUPABASE_PORT']
)

with con.cursor() as cursor:
    url = "https://pokeapi.co/api/v2/pokemon?limit=10"    
    response = requests.get(url).json()

    for pokemon in response['results']:
        url_pokemon = pokemon['url']
        dados_pokemon = requests.get(url_pokemon).json()

        #collection basic datas:
        pokemon_name = dados_pokemon['name']
        pokemon_height = dados_pokemon['height']
        pokemon_weight = dados_pokemon['weight']

        #coletando statics:
        for stat in dados_pokemon["stats"]:
            nome_stat = stat["stat"]["name"]
            valor = stat["base_stat"]

            if nome_stat == "hp":
                pokemon_hp = valor
            if nome_stat == "attack":
                pokemon_attack = valor
            elif nome_stat == "defense":
                pokemon_defense = valor
            elif nome_stat == "speed":
                pokemon_speed = valor

        # collection generation:
        url_generation = dados_pokemon['species']['url']
        species_response = requests.get(url_generation).json()
        pokemon_gen = species_response['generation']['name']

        # collection types:
        type_1 = dados_pokemon['types'][0]['type']['name']
        if len(dados_pokemon['types']) > 1:
            type_2 = dados_pokemon['types'][1]['type']['name']
            sql = """
                INSERT INTO pokemons (name, type_1, type_2, gen, hp, attack, defense, speed, height, weight) VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(sql, [pokemon_name, type_1, type_2, pokemon_gen, pokemon_hp, pokemon_attack, pokemon_defense, pokemon_speed, pokemon_height, pokemon_weight])
        else:
            sql = """
                INSERT INTO pokemons (name, type_1, gen, hp, attack, defense, speed, height, weight) VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s)

            """
            cursor.execute(sql, [pokemon_name, type_1, pokemon_gen, pokemon_hp, pokemon_attack, pokemon_defense, pokemon_speed, pokemon_height, pokemon_weight])

    con.commit()