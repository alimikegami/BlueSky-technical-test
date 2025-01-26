from fastapi import APIRouter, Depends
from database import get_db
from typing import Optional
from pokemon.service import get_pokemon

router = APIRouter()

async def query_parameters(name: Optional[str] = None, page: int = 1, limit: int = 10, type: Optional[str]=None):
    return {"name": name, "page": page, "limit": limit, "type": type}

@router.get("/pokemon",
    responses={
        200: {
            "description": "Retrieved Pokemon data",
            "content": {
                "application/json": {
                    "example": {"status": "success", "data": {"_metadata": {"total_records": 1, "limit": 10, "page": 1}, "records": [{"id": 1, "name": "Charizard", "type_1": "fire", "type_2": "Dragon", "pokedex_id": "0006", "created_at": 1737904525, "updated_at": 1737904525, "deleted_at": 0}]}}
                }
            },
        },
    },
    tags=["pokemon"])
async def get_pokemon_route(db=Depends(get_db), query_params=Depends(query_parameters)):
    pokemon = await get_pokemon(db, query_params)
    return {"status": "success", "data": pokemon}