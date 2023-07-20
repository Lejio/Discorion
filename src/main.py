from dotenv import load_dotenv
import os
import time
from datetime import datetime

import logging
from discord.ext import commands
from discord import Intents, Guild, Embed, Colour, Interaction, errors

from poketools.pokemon.pokecalc import *
from poketypes.electric import Electric
from poketools.pokegenerator.pokedatabase import FetchWild
from pokeguilds import TypeGuilds
from poketranslator import Style, PokeTranslator


load_dotenv()
cogs: list = ["pokestyles"]

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
        
        print(f"Joined {guild.name}/{guild.id}")
        
client = Discorion()

@client.tree.command(name="pikachu", description="Displays example pikachu pokemon.")
@commands.check_any(commands.is_owner())
async def pikachu(interaction: Interaction):
            
        embed = Embed(colour=Colour.yellow(), title=f"{interaction.user.display_name}'s", description=f"{Electric.P.value}{Electric.I.value}{Electric.K.value}{Electric.A.value}{Electric.C.value}{Electric.H.value}{Electric.U.value}")
        # embed.set_image(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938114247016548/pikachu-removebg-preview.png")
        # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938978797916180/Electric_icon_SwSh.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938114247016548/pikachu-removebg-preview.png")
        
        # embed.add_field(name="", value=f"{createSeparator(10)}", inline=False)
        embed.add_field(name="Level", value=f"5", inline=False)
        # embed.add_field(name="", value=f"{createSeparator(10)}", inline=False)
        
        embed.add_field(name=f"{Electric.H.value}{Electric.P.value} [100/180]", value=f"{createBar(calcBar(100, 180))}", inline=False)
        embed.add_field(name=f"{Electric.A.value}{Electric.T.value}{Electric.T.value}{Electric.A.value}{Electric.C.value}{Electric.K.value} [55/103]", value=f"{createBar(calcBar(55, 103))}", inline=False)
        embed.add_field(name=f"{Electric.D.value}{Electric.E.value}{Electric.F.value}{Electric.E.value}{Electric.N.value}{Electric.S.value}{Electric.E.value} [40/79]", value=f"{createBar(calcBar(40, 79))}", inline=False)
        embed.add_field(name=f"{Electric.S.value}{Electric.P.value} {Electric.A.value}{Electric.T.value}{Electric.K.value} [50/94]", value=f"{createBar(calcBar(50, 94))}", inline=False)
        embed.add_field(name=f"{Electric.S.value}{Electric.P.value} {Electric.D.value}{Electric.E.value}{Electric.F.value} [50/94]", value=f"{createBar(calcBar(50, 94))}", inline=False)
        embed.add_field(name=f"{Electric.S.value}{Electric.P.value}{Electric.E.value}{Electric.E.value}{Electric.D.value} [90/166]", value=f"{createBar(calcBar(90, 166))}", inline=False)
        embed.add_field(name='test', value=str(60*'#'), inline=False)
        

        await interaction.response.send_message(embed=embed)
        

# @client.tree.command(name="addemoji", description="Adds emoji automatically")
# async def addElectricEmojis(interaction: Interaction):

#     channel = interaction.channel

#     await interaction.response.send_message("Adding Emoji")
    
#     alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
#     for g in TypeGuilds:
#         # print(g.value['name'])
#         guild = client.get_guild(int(g.value['origin']))
#         await channel.send(guild.name)
#         for a in alphabet:
            
#             path = f"./assets/pokefonts/{g.value['name']}/{g.value['name']}_{a}.png"
#             with open(path, "rb") as image:
#                 f = image.read()
#                 b = bytes(f)
            
#             c = f"{g.value['name'][0]}_{a}"
#             print(c)
            
#             emoji = await guild.create_custom_emoji(name=c, image=b)
#             time.sleep(1.5)
#             await channel.send(f'{a} = "<:{c}-{emoji.id}>"')
#         await channel.send()
    
    
@client.tree.command(name="get-random-pokemon", description="Searches for a pokemon")
async def searchPokemon(interaction: Interaction):
    fetch = FetchWild(os.environ['DATABASE_URL'], os.environ['DEFAULT_POKEMON_DATABASE'])
    
    pokemon = fetch.getRandom()
    
    pokemonMessage = f"Pokedex Number: {pokemon[0]}\n{pokemon[1]}"
    
    await interaction.response.send_message(pokemonMessage)
    
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(os.environ['DISCORD_API_KEY'], log_handler=handler)
        
        


