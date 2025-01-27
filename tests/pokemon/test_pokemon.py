from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_pokemon():
    response = client.get("/pokemon?limit=10&page=1")
    records = response.json()['data']['records']
    total_records = response.json()['data']['_metadata']['total_records']
    assert total_records != 0
    assert len(records) != 0
    assert response.status_code == 200

def test_get_pokemon_invalid_type():
    response = client.get("/pokemon?limit=10&page=1&type=alim")
    records = response.json()['data']['records']
    total_records = response.json()['data']['_metadata']['total_records']
    assert total_records == 0
    assert len(records) == 0
    assert response.status_code == 200