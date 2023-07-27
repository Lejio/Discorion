from pokemon.pokemon import Pokemon
from poketools.pokequery import PokeQuery
from poketools.pokegenerator.pokedatabase import FetchWild

from dotenv import load_dotenv

import json
import os

load_dotenv()

registry = json.load(open('./pokemon/registry.json'))
query_pokemon = input('Enter a pokemon: ')

try:
    int(query_pokemon)
    query_type = 'number_based'
except ValueError:
    query_type = 'name_based'

queryEngine = PokeQuery(pokemon_object=registry[query_type])
result_list = queryEngine.query(user_input=query_pokemon)

fetch = FetchWild(os.environ['DATABASE_URL'], os.environ['DEFAULT_POKEMON_DATABASE'])
response = fetch.getPokemon(int(result_list[1]))

print(result_list)

# print(response[1])
# data = None

# with open('./pokemon/25.json') as raw:
#     data = json.load(raw)

pokemon = Pokemon(response[1])

print(pokemon.versions[0].national_number)
print(pokemon.versions[0].type)

