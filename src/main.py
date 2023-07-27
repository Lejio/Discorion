from dotenv import load_dotenv
import os
# import time
from datetime import datetime
import json

import logging
from discord.ext import commands
from discord import Intents, Guild, Embed, Colour, Interaction, errors, File

from poketools.pokemon.pokecalc import *
from poketools.pokegenerator.pokedatabase import FetchWild
from poketranslator import *
from pokemon.pokemon import Pokemon
from poketools.pokequery import PokeQuery
from pokeembed import *


load_dotenv()
cogs: list = ["pokestyles"]
registry = json.load(open('./pokemon/registry.json'))

class Discorion(commands.Bot):
    
    def __init__(self, command_prefix="!p", description: str | None = None, intents=Intents.all()) -> None:
        super().__init__(command_prefix, description=description, intents=intents)
        
    
    async def on_ready(self):
        
        """
        Client event. Runs when the bot is ready and has successfully logged in.
        """
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

@client.tree.command(name="pikachu", description="Displays example pikachu pokemon.")
@commands.check_any(commands.is_owner())
async def pikachu(interaction: Interaction):
            
        embed = Embed(colour=Colour.yellow(), title=f"{interaction.user.display_name}'s", description=f"{translateText(text_style=Style('electric')[0], text='Pikachu')}")
        # embed.set_image(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938114247016548/pikachu-removebg-preview.png")
        # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938978797916180/Electric_icon_SwSh.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938114247016548/pikachu-removebg-preview.png")
        
        embed.add_field(name="Level", value=f"5", inline=False)
        
        style = Style('electric')[0]
        
        embed.add_field(name=f"{translateText(text_style=style, text='HP')} [100/180]", value=f"{createBar(calcBar(100, 180), style)}", inline=False)
        embed.add_field(name=f"{translateText(text_style=style, text='Attack')} [55/103]", value=f"{createBar(calcBar(55, 103), style)}", inline=False)
        embed.add_field(name=f"{translateText(text_style=style, text='Defense')} [40/79]", value=f"{createBar(calcBar(40, 79), style)}", inline=False)
        embed.add_field(name=f"{translateText(text_style=style, text='Sp Atk')} [50/94]", value=f"{createBar(calcBar(50, 94), style)}", inline=False)
        embed.add_field(name=f"{translateText(text_style=style, text='Sp Def')} [50/94]", value=f"{createBar(calcBar(50, 94), style)}", inline=False)
        embed.add_field(name=f"{translateText(text_style=style, text='Speed')} [90/166]", value=f"{createBar(calcBar(90, 166), style)}", inline=False)
        # embed.add_field(name='test', value=str(60*'#'), inline=False)
        

        await interaction.response.send_message(embed=embed)
        
'''


@client.tree.command(name="add-font-styles", description="Adds alphabet emojis automatically")
@commands.check_any(commands.is_owner())
async def addElectricEmojis(interaction: Interaction):

    channel = interaction.channel

    await interaction.response.send_message("Adding Emoji")
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for g in TypeGuilds:
        # print(g.value['name'])
        guild = client.get_guild(int(g.value['origin']))
        await channel.send(guild.name)
        for a in alphabet:
            
            path = f"./assets/pokefonts/{g.value['name']}/{g.value['name']}_{a}.png"
            with open(path, "rb") as image:
                f = image.read()
                b = bytes(f)
            
            c = f"{g.value['name'][0]}_{a}"
            print(c)
            
            emoji = await guild.create_custom_emoji(name=c, image=b)
            time.sleep(1.5)
            await channel.send(f'{a} = "<:{c}-{emoji.id}>"')
        await channel.send()
'''

'''

# Uploads sprites from the specified folder up into discord servers. This script runs for around 3 hours.

@client.tree.command(name="upload-sprites", description="Uploads sprites and images to both discord and cockroachdb")
@commands.check_any(commands.is_owner())
async def uploadSprites(interaction: Interaction):
    
    # ---------- Changes DiscordDatabase enum into a list ----------
    discord_db = list(DiscordDatabase)
    
    # ---------- Defines constant paths to both the json (where the pokemon info is stored) and sprites ----------
    JSON_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/pokedex/'
    SPRITES_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/'

    # ---------- Saves the channel from interaction to send a message for each emoji created. ----------
    channel = interaction.channel
    
    # ---------- Sends beginning message to avoid interaction not responded error ----------
    await interaction.response.send_message("Beginning upload.")

    # ---------- Guild number starts a one, and gradually increases as space runs out. ----------
    guild_num = 0
    guild = client.get_guild(discord_db[guild_num].value)
    
    # ---------- Loop that goes through the specified range of pokemons that needs to be uploaded. ----------
    for poke in range(50, 1011):
        
        # ---------- Checks guild if there is still space left (full - 50). ----------
        if len(guild.emojis) < 50:
                
            # ---------- Translates [current index].png image into bytes. ----------
            with open(SPRITES_DIR + str(poke) + ".png", "rb") as image:
                f = image.read()
                imageBytes = bytes(f)
                
            # ---------- Loads the pokemon json file related to the current index. ----------
            with open(JSON_DIR + str(poke) + ".json", "r") as file:
                data = json.load(file)
            
            # ---------- Runs async function that creates the emoij. ----------
            emoji = await guild.create_custom_emoji(name=f"P{poke}", image=imageBytes)
            
            # ---------- Sets/Creates new key in json that stores the created emojis id. ----------
            data['discord_sprite'] = f"<:P{poke}:{emoji.id}>"
            
            # ---------- Sends confirmation. ----------
            await channel.send(f'P{poke} - {data["discord_sprite"]}')
            
            # ---------- Saves the json changes. ----------
            with open(JSON_DIR + str(poke) + ".json", "w") as file:
                json.dump(data, file, indent=4)
            
                
        else:
            # ---------- Else runs when server is full. ----------
            
            # ---------- Increment the guild_num by one to move onto the next server listed in DiscordDatabase ----------
            guild_num += 1
            guild = client.get_guild(discord_db[guild_num].value)
            
            # ----------  Does the same thing as above ----------
            with open(SPRITES_DIR + str(poke) + ".png", "rb") as image:
                f = image.read()
                b = bytes(f)
                
            
            with open(JSON_DIR + str(poke) + ".json", "r") as file:
                data = json.load(file)
                
            emoji = await guild.create_custom_emoji(name=f"P{poke}", image=b)
            data['discord_sprite'] = f"<:P{poke}:{emoji.id}>"
            
            await channel.send(f'P{poke} - {data["discord_sprite"]}')
            
            with open(JSON_DIR + str(poke) + ".json", "w") as file:
                json.dump(data, file, indent=4)
            
            # ---------------------------------------------------
        
        # ----------  Sleeps the function so we do not get rate limited by discord api. ----------
        time.sleep(10)
''' 


'''

# Mean't to remove sprites, however it is currently broken. It seems like it might not be required in the future.

@client.tree.command(name="remove-sprites", description='removes all sprites')
@commands.check_any(commands.is_owner())
async def removeSprites(interaction: Interaction):
    
    await interaction.response.send_message("deleting emojis")
    discord_db = list(DiscordDatabase)
    guild_num = 0
    guild = client.get_guild(discord_db[guild_num].value)
    
    if len(guild.emojis) < 50:
        
        for i in range(0, 50):
            try:
                print(guild.emojis[i])
                emoji = await guild.delete_emoji(guild.emojis[i])
                time.sleep(1.5)
            except IndexError:
                pass
    

    else:
        guild_num += 1
        guild = client.get_guild(discord_db[guild_num].value) 
'''

'''

# Uploads official artwork and saves the link inside of the json info file.

@client.tree.command(name="upload-official-art", description="Uploads official art to discord and adds them to the json list.")
async def uploadSprites(interaction: Interaction):
    
    # ---------- Saves the channel so it could be used to send the image after interaction expires ---------- #
    channel = interaction.channel
    
    await interaction.response.send_message("Uploading images now.")
    
    # ---------- path to the official-artwork folder, all of them in the format of [pokedex-number].png. ----------
    path = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/other/official-artwork/'
    JSON_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/pokedex/'
    
    # ---------- Loops through all the pokedex numbers (1 - 1010) ----------
    for i in range(1, 1010):
        print(str(i))
        message = await channel.send(file=File(path + str(i) + ".png"))
        
        # ---------- Saves the image url ----------
        image_url = message.attachments[0].url
        
        # ---------- Loads json file ----------
        with open(JSON_DIR + str(i) + ".json", "r") as file:
            data = json.load(file)
        
        # ---------- Create a new key and set the image url ----------
        data['discord_image'] = image_url
        
        # ---------- Saves the newly changed json back to its original file ----------
        with open(JSON_DIR + str(i) + ".json", "w") as file:
            json.dump(data, file, indent=4)
        
        # ---------- Sleep so we won't get rate limited by discord api (this should take ~24mins) ----------
        time.sleep(1.5)
'''

@client.tree.command(name='test-prag', description='testing prag functionality')
async def pragTest(interaction: Interaction):
    await interaction.response.send_message(embed=Embed(title="Creating Test", colour=Colour.light_grey()))
    message = await interaction.original_response()
    pages = [TestEmbed1(), TestEmbed2(), TestEmbed3()]
    prag = TestPrag(pages=pages)
    await prag.send(message=message)

@client.tree.command(name='search-pokemon', description='Searches for a pokemon via pokedex number or name.')
async def searchPokemon(interaction: Interaction, pokemon: str):

    message = None
    
    try:
        int(pokemon)
        query_type = 'number_based'
    except ValueError:
        query_type = 'name_based'
    
    queryEngine = PokeQuery(pokemon_object=registry[query_type])
    result_list = queryEngine.query(user_input=pokemon)
    
    if result_list is None:
        await interaction.response.send_message(embed=Embed(colour=Colour.red(), title='404 Error: Pokemon Not Found'))
        return
    else:
        await interaction.response.send_message(embed=Embed(color=Colour.yellow(), title=f'Generating result for {result_list[0]}'))
        message = await interaction.original_response()
        
    fetch = FetchWild(os.environ['DATABASE_URL'], os.environ['DEFAULT_POKEMON_DATABASE'])
    response = fetch.getPokemon(int(result_list[1]))
    
    pokemon_response = Pokemon(response[1])
    
    pokestats = PokeStats(pokemon=pokemon_response)
    pokeinfo = PokeInfo(pokemon=pokemon_response)
    
    testview = TestPrag([pokeinfo, pokestats])
    await testview.send(message=message)
    

@client.tree.command(name="get-random-pokemon", description="Searches for a pokemon")
async def getRandomPokemon(interaction: Interaction):
    fetch = FetchWild(os.environ['DATABASE_URL'], os.environ['DEFAULT_POKEMON_DATABASE'])
    
    pokemon = fetch.getRandom()
    
    pokemonMessage = f"Pokedex Number: {pokemon[0]}\n{pokemon[1][pokemon[1]['name']]}"
    await interaction.response.send_message(pokemonMessage)
    
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(os.environ['DISCORD_API_KEY'], log_handler=handler)
        
        


