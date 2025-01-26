from fastapi import FastAPI, Depends
from pokemon.service import scrape_pokemon_data, get_pokemon
from database import get_db
from pokemon.route import router as pokemon_router

app = FastAPI()
app.include_router(pokemon_router)


# populate database data via web scraping
@app.on_event("startup")
async def startup_event():
    for db in get_db():
        try:
            query_params = {
                "name": None,
                "type": None,
                "limit": 10,
                "page": 1
            }
            pokemon = await get_pokemon(db, query_params)
            if len(pokemon) == 0:
                scrape_pokemon_data(db)
                print("pokemon data has been scraped")
            else:
                print("pokemon data exists")    
        except Exception as err:
            print("error on scraping pokemon data: ", err)

@app.get("/")
async def root():
    return {"message": "Hello World"}