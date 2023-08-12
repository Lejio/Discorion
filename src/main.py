from dotenv import load_dotenv
import os
# import time
from datetime import datetime
import json

import logging
from discord.ext import commands
from discord import Intents, Guild, Embed, Colour, Interaction, errors, File

from pymongo.collection import Collection

from utils.supabase import supabase_loader
from utils.pymongo import load_mongodb
from poketools.pokemon.pokecalc import *
from poketools.pokegenerator.pokedatabase import FetchWild
from poketranslator import *
from pokemon.pokeobject import PokeObject
from poketools.pokequery import PokeQuery
from pokeembed import *

from testembed import *


load_dotenv()
cogs: list = ["pokestyles", "catch"]
registry = json.load(open('./pokemon/registry.json'))
catch_registry = json.load(open('./pokemon/catch_registry.json'))
cache: dict = {'supabase': supabase_loader(), 'mongodb': load_mongodb()['pokemon_templates']}

class Discorion(commands.Bot):
    
    def __init__(self, command_prefix="!p", description: str | None = None, intents=Intents.all()) -> None:
        super().__init__(command_prefix, description=description, intents=intents)
        
    
    async def on_ready(self):
        
        """
        Client event. Runs when the bot is ready and has successfully logged in.
        """
        
        self.registry = registry
        self.cache = cache
        self.catch_registry = catch_registry
        
        print("Cache successfully loaded.")
        
        print(f"\n{datetime.utcnow()}: Logged in successfully as: " + str(client.user) + "\n")

        try:
        
            for cog in cogs:  # Loads each config into the client.

                await client.load_extension(cog)
                print(f"Loaded cog {cog}")

            print("Successfully loaded all Cogs\n")
        
        except commands.ExtensionAlreadyLoaded:
        
            print("Extension already loaded")
            
        a = await self.tree.sync()
        print(f"{len(a)} Synced")

        
    
    async def on_guild_join(self, guild: Guild):
        
        guild_id = guild.name.replace(" ", "_")
        
        print(f"{guild_id} = {guild.id}")
        
client = Discorion()


@client.tree.command(name='search-pokemon', description='Searches for a pokemon via pokedex number or name.')
async def searchPokemon(interaction: Interaction, name: str):

    message = None
    
    try:
        int(name)
        query_type = 'number_based'
    except ValueError:
        query_type = 'name_based'
    
    queryEngine = PokeQuery(pokemon_object=registry[query_type])
    result_list = queryEngine.query(user_input=name)
    
    if result_list is None:
        await interaction.response.send_message(embed=Embed(colour=Colour.red(), title='404 Error: Pokemon Not Found'))
        return
    else:
        await interaction.response.send_message(embed=Embed(color=Colour.yellow(), title=f'Generating result for {result_list[0]}'))
        message = await interaction.original_response()
        
    pokeCollection: Collection = cache['mongodb']['pokemon']
    pokemon_response = PokeObject(pokeCollection.find_one({ "_id": int(result_list[1])})['data'])
    
    pokepage = [PokeInfo(pokemon=pokemon_response), PokeStats(pokemon=pokemon_response), PokePokedex(pokemon=pokemon_response)]
    
    testview = TestPrag(pokepage)
    await testview.send(message=message)
    
    
@client.tree.command(name="test-select", description="Testing select pagination.")
async def testPagination(interaction: Interaction):
    
    message = interaction.message
    
    pokeCollection: Collection = cache['mongodb']['pokemon']
    pokemon_response = PokeObject(pokeCollection.find_one({ "_id": 6})['data'])
    
    pokeselect = PokemonSelect(pokemon=pokemon_response, message=message)
    
    view = View()
    view.add_item(pokeselect)
    
    await interaction.response.send_message(embed=Embed(color=Colour.yellow(), title=f'Generating result for {6}'))

# @client.tree.command(name="get-random-pokemon", description="Searches for a pokemon")
# async def getRandomPokemon(interaction: Interaction):
#     fetch = FetchWild(os.environ['DATABASE_URL'], os.environ['DEFAULT_POKEMON_DATABASE'])
    
#     pokemon = fetch.getRandom()
    
#     pokemonMessage = f"Pokedex Number: {pokemon[0]}\n{pokemon[1][pokemon[1]['name']]}"
#     await interaction.response.send_message(pokemonMessage)
    
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(os.environ['DISCORD_API_KEY'], log_handler=handler)
        
        


