import psycopg2
import dotenv
import os
import requests

dotenv.load_dotenv()

con = psycopg2.connect(
    host='db.jttqcuxpvkppfglkbkce.supabase.co',
    user='leitor',
    password='123',
    database='postgres',
)

with con:
    with con.cursor() as cursor:
        sql = """
            SELECT * FROM pokemons
        """

        cursor.execute(sql)