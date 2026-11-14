import psycopg2
import dotenv

dotenv.load_dotenv()

con = psycopg2.connect(
    # dados de login no banco de dados como leitor:
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