from database import get_db
from fastapi import Depends


def add_pokemon_bulk(pokemons, db):
    cursor = db.cursor()
    insert_pokemon = ("INSERT INTO pokemon "
            "(name, type_1, type_2, pokedex_id) "
            "VALUES (%(name)s, %(type_1)s, %(type_2)s, %(pokedex_id)s)")
    cursor.executemany(insert_pokemon, pokemons)
    db.commit()
    cursor.close()