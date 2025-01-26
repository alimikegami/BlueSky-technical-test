from fastapi import FastAPI
from pokemon.service import scrape_pokemon_data
app = FastAPI()
from database import get_db

# populate database data via web scraping
for db in get_db():
    try:
        scrape_pokemon_data(db)
    except Exception as err:
        print("error on scraping pokemon data: ", err)
    
@app.get("/")
async def root():
    return {"message": "Hello World"}