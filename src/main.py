import csv
import time
from dotenv import load_dotenv
import os
# import time
from datetime import datetime
import json

import logging
from discord.ext import commands
from discord.abc import GuildChannel
from discord import File, Intents, Guild, Embed, Colour, Interaction, Emoji, TextChannel

from pymongo.collection import Collection
from discord.discorddatabase import DiscordDatabase

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
registry = json.load(open('./pokemon/registry_v2.json'))
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
async def testPagination(interaction: Interaction, poke_id: int):
    await interaction.response.send_message(embed=Embed(color=Colour.yellow(), title=f'Generating result for {poke_id}'))
    message = await interaction.original_response()
    
    pokeCollection: Collection = cache['mongodb']['pokemon']
    pokemon_response = PokeObject(pokeCollection.find_one({ "_id": poke_id})['data'])
    
    pokeselect = PokemonSelect(pokemon=pokemon_response, message=message, cache=cache)
    
    await pokeselect.send()

# @client.tree.command(name="get-random-pokemon", description="Searches for a pokemon")
# async def getRandomPokemon(interaction: Interaction):
#     fetch = FetchWild(os.environ['DATABASE_URL'], os.environ['DEFAULT_POKEMON_DATABASE'])
    
#     pokemon = fetch.getRandom()
    
#     pokemonMessage = f"Pokedex Number: {pokemon[0]}\n{pokemon[1][pokemon[1]['name']]}"
#     await interaction.response.send_message(pokemonMessage)

@client.tree.command(name="upload-sprites", description="Uploads sprites and images to both discord and cockroachdb")
@commands.check_any(commands.is_owner())
async def uploadSprites(interaction: Interaction):
    
    # ---------- Defines constant paths to both the json (where the pokemon info is stored) and sprites ----------
    SPRITES_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/'
    IMAGE_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/other/official-artwork/'
    
    # ---------- Guild number starts a one, and gradually increases as space runs out. ----------
    guild_num = [0]
        # ---------- Saves the channel from interaction to send a message for each emoji created. ----------
    channel = interaction.channel
    
    # ---------- Sends beginning message to avoid interaction not responded error ----------
    await interaction.response.send_message("Beginning upload.")

    sprite_versions: dict = {}
    # sprites_list: list = os.listdir(SPRITES_DIR)
    
    with open('extra_sprites.json', 'r') as extra_sprites:
        
        sprites_list = json.load(extra_sprites)
        
        
        
    
    for raw_sprite in sprites_list:
        
        for version in sprites_list[raw_sprite]:
            # sprite = raw_sprite.split('.')[0]
            
            sprite = '-'.join([raw_sprite, version])
            print(sprite)
            if len(sprite.split('-')) > 1:
                
                sprite_split = sprite.split('-')
                sprite_number = sprite_split[0]
                sprite_version_combined = '-'.join(sprite_split[1:])
                
                payload = await uploader(channel=channel, sprite_name=sprite, guild_num=guild_num, number=sprite_number, sprite_version="_".join(sprite_split[1:]))
                
                if sprite_number in sprite_versions.keys():
                    sprite_versions[sprite_number][sprite_version_combined] = {
                        'sprite': payload['emoji'],
                        'png': payload['png']
                    }
                    
                else:
                    sprite_versions[sprite_number] = {}
                    sprite_versions[sprite_number][sprite_version_combined] = {
                        'sprite': payload['emoji'],
                        'png': payload['png']
                    }
                    # await uploader(channel=channel)
                
                channel.send(f'{sprite_number} | {sprite_version_combined}')
                
            time.sleep(10)
        
    with open('extra_sprites_v2.json', 'w') as outfile:
        
        json.dump(sprite_versions, outfile, indent=4)
        

async def uploader(channel: TextChannel, sprite_name, guild_num, number, sprite_version) -> dict:
    
    SPRITES_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/'
    IMAGE_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/other/official-artwork/'

    # ---------- Changes DiscordDatabase enum into a list ----------
    discord_db = list(DiscordDatabase)

    payload = {
        'emoji': None,
        'png': None
    }
    guild: Guild | None = client.get_guild(discord_db[guild_num[0]].value)
    
    while len(guild.emojis) == 50:
        
        guild_num[0] += 1
        guild = client.get_guild(discord_db[guild_num[0]].value)
        
    with open(SPRITES_DIR + str(sprite_name) + ".png", "rb") as image:
        f = image.read()
        imageBytes = bytes(f)

    emoji: Emoji = await guild.create_custom_emoji(name=f"P{number}_{sprite_version}", image=imageBytes)
    try:
        message = await channel.send(file=File(IMAGE_DIR + str(sprite_name + ".png")))
    except Exception:
        print(f'{sprite_name}')
    
    image_url = message.attachments[0].url
    
    payload['emoji'] = f'<:P{number}_{sprite_version}:{emoji.id}>'
    payload['png'] = image_url
    
    return payload
        
        
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(os.environ['DISCORD_API_KEY'], log_handler=handler)
        
        


