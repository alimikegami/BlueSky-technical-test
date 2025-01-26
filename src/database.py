import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db():
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    
    try:
        yield db
    finally:
        db.close()