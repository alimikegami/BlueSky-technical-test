# BlueSky Back-end Engineer Technical Test
## Pokemon Data
The pokemon data is retrieved from <a href="https://pokemondb.net/">pokemondb.net</a>. The reasoning behind this is that the moderator in the site recently allows web scraping in moderation as stated in this <a href="https://pokemondb.net/pokebase/meta/82871/can-i-use-pokemons-data-of-this-website-for-my-school-project">reference</a>. Here are the Pokemon data fields stored in this project:
- Name
- Type 1
- Type 2
- Pokedex ID
## Running The Project
To run the project as a container, use the following command:
```
docker compose up -d
```
Once executed, the API will be accessible at `http://localhost:8001`
## Tech Stacks
The following technologies are used in this project:
- Python (BeautifulSoup4, FastAPI, MySQL connector, dotenv, pytest)
- MySQL
- Docker
## API Documentation
The API documentation can be accessed at `http://localhost:8001/docs`
<br>
![API docs screenshot](./screenshots/api_docs.png)
## How The Project Works
This project scrapes data from <a href="https://pokemondb.net/">pokemondb.net</a> using BeautifulSoup4. The scraping process serves as a database seeding mechanism for the API, which then serves Pokemon data from the local database.
## Tests
### Integration Tests
The integration test written for this project cant be found in `tests` directory. To run the test, use the following command:
```
pytest
```
<br>
![test screenshot](./screenshots/test.png)