import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import errorcode

load_dotenv()

def get_db():
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT'))
    )
    
    try:
        yield db
    finally:
        db.close()
        
def migrate_tables(db):
    cursor = db.cursor()
    pokemon = (
    "CREATE TABLE `pokemon` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(50) NOT NULL,"
    "  `type_1` varchar(30) NOT NULL,"
    "  `type_2` varchar(30) NOT NULL,"
    "  `pokedex_id` VARCHAR(10) NOT NULL,"
    "  `created_at` int(11) NOT NULL,"
    "  `updated_at` int(11) NOT NULL,"
    "  `deleted_at` int(11) NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
    try:
        print("creating pokemon table")
        cursor.execute(pokemon)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("pokemon table already exists")
        else:
            print(err.msg)
    else:
        print("pokemon table created")