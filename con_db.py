import pymysql
import dotenv
import os

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
        sql_query = """
            CREATE TABLE Pokemons (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(30),
                type_slot_1 VARCHAR(20),
                type_slot_2 VARCHAR(20),
                hp INT,
                attack INT,
                defense INT,
                speed INT
            )
        """

        cursor.execute(sql_query)
        con.commit()