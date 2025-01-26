from ..database import get_db
from src.pokemon.schemas import Pokemon

def add_pokemon_bulk(pokemons, db):
    cursor = db.cursor()
    insert_pokemon = ("INSERT INTO pokemon "
            "(name, type_1, type_2, pokedex_id, created_at, updated_at) "
            "VALUES (%(name)s, %(type_1)s, %(type_2)s, %(pokedex_id)s, %(created_at)s, %(updated_at)s)")
    cursor.executemany(insert_pokemon, pokemons)
    db.commit()
    cursor.close()
    

async def get_pokemon_data(db, query_params):
    pokemon = []
    params = []
    cursor = db.cursor()
    select_pokemon = "SELECT id, name, pokedex_id, type_1, type_2, created_at, updated_at FROM pokemon WHERE deleted_at IS NULL"
    if query_params["name"] != None:
        select_pokemon += " AND name LIKE %s"
        params.append("%" + query_params["name"] + "%")
    
    if query_params["type"] != None:
        select_pokemon += " AND (type_1 = %s OR type_2 = %s)"
        params.append(query_params["type"])
        params.append(query_params["type"])
    
    if query_params["limit"] != 0:
        select_pokemon += " LIMIT %s"
        params.append(query_params["limit"])
    
    if query_params["page"]:
        select_pokemon += " OFFSET %s"
        params.append(query_params["limit"] * (query_params["page"] - 1))

    cursor.execute(select_pokemon, params)
    for (id, name, pokedex_id, type_1, type_2, created_at, updated_at) in cursor:
        pokemon.append(Pokemon(id, name, type_1, type_2, pokedex_id, created_at, updated_at, None))
    
    return pokemon

async def get_pokemon_count(db, query_params):
    count: int = 0
    params = []
    cursor = db.cursor()
    select_pokemon = "SELECT COUNT(id) FROM pokemon WHERE deleted_at IS NULL"
    if query_params["name"] != None:
        select_pokemon += " AND name LIKE %s"
        params.append("%" + query_params["name"] + "%")
    
    if query_params["type"] != None:
        select_pokemon += " AND (type_1 = %s OR type_2 = %s)"
        params.append(query_params["type"])
        params.append(query_params["type"])


    cursor.execute(select_pokemon, params)
    for (row_count) in cursor:
        count = row_count[0]
    
    return count