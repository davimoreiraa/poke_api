import dotenv
import psycopg2
import os

dotenv.load_dotenv()

con = psycopg2.connect(
    dbname= os.environ['SUPABASE_DATABASE'],
    user= os.environ['SUPABASE_USER'],
    password= os.environ['SUPABASE_PASWWORD'],
    host= os.environ['SUPABASE_HOST'],
    port= os.environ['SUPABASE_PORT']
)

with con.cursor() as cursor:
    sql_create_table = """
        CREATE TABLE Pokemons (
            id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name VARCHAR(60),
            type_1 VARCHAR(30),
            type_2 VARCHAR(30),
            gen VARCHAR(35),
            hp INT,
            attack INT,
            defense INT,
            speed INT,
            height INT,
            weight INT
        )
    """

    cursor.execute(sql_create_table)
    con.commit()