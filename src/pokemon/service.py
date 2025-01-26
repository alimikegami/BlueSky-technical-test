from http.client import HTTPException
import requests
from bs4 import BeautifulSoup
from src.pokemon.repository import add_pokemon_bulk, get_pokemon_data, get_pokemon_count
from datetime import datetime

def scrape_pokemon_data(db):
    url = "https://pokemondb.net"
    response = requests.get(url=url + "/pokedex/all", timeout=10)
    
    pokemons = []
    
    # handle the same pokemon from being inserted into the database multiple times, as the site also contains mega variant with the same pokedex ID   
    hash_map = {}

    
    # define the limit of pokemon we are trying to import to the database
    count = 0
    limit = 15
    
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        pokedex = soup.find(id="pokedex").find("tbody")
        for row in pokedex.find_all("tr"):
            if count == limit:
                break
            
            name = row.find("a", class_="ent-name")
            types = row.find_all("a", class_="type-icon")
            pokedex_id = row.find(class_="infocard-cell-data")
            
            # only the first variant found (which usually is the regular variant) are inserted to the DB
            if pokedex_id in hash_map:
                continue
            
            if name:
                pokemon = {
                    "name": name.get_text(),
                    "pokedex_id": pokedex_id.get_text(),
                    "created_at": datetime.now().timestamp(),
                    "updated_at": datetime.now().timestamp()
                }
                
                if len(types) > 1:
                    pokemon["type_1"] = types[0].get_text()
                    pokemon["type_2"] = types[1].get_text()
                elif len(types) == 1:
                    pokemon["type_1"] = types[0].get_text()
                    pokemon["type_2"] = ""
                
                pokemons.append(pokemon)
            
            hash_map[pokedex_id] = 1
            count += 1
    else:
        raise Exception("unable to access pokemondb.net")
    
    add_pokemon_bulk(pokemons=pokemons, db=db)
    
async def get_pokemon(db, query_params):
    pokemon = await get_pokemon_data(db, query_params)
    pokemon_count = await get_pokemon_count(db, query_params)
    return {"records": pokemon, "_metadata": {"total_records": pokemon_count, "page": query_params["page"], "limit": query_params["limit"]}}