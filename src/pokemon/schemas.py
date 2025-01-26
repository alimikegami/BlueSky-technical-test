from dataclasses import dataclass

class Pokemon:
    id: int
    name: str
    type_1: str
    type_2: str
    pokedex_id: str
    created_at: int
    updated_at: int
    deleted_at: int
    
    def __init__(self, id, name, type_1, type_2, pokedex_id, created_at, updated_at, deleted_at):
        self.id = id
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.pokedex_id = pokedex_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at