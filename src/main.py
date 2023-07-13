from dotenv import load_dotenv
import os
import math

import logging
from discord.ext import commands
from discord import Intents, Guild, Embed, Colour, Interaction, errors

from poketools.pokemon.pokecalc import *
from poketypes.electric import Electric

load_dotenv()


class Discorion(commands.Bot):
    
    def __init__(self, command_prefix="!p", description: str | None = None, intents=Intents.all()) -> None:
        super().__init__(command_prefix, description=description, intents=intents)
        
    
    async def on_ready(self):
        
        print("Discorion is ready!")
        
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
        
        
@client.tree.command(name="electric", description="Displays text back in Electric font")
async def electricCheck(interaction: Interaction, text: str):
    
    channel = interaction.channel
        
    try: 
        eWord = translateText(text_style=Electric, text=text)
    except KeyError:
        await interaction.response.send_message(embed=Embed(title="Command Error", description=f"KeyError '{eWord}' not supported."))
        return
            
    embed = Embed(colour=Colour.yellow(), title=f"{interaction.user} says: ", description=eWord)
    
    # print(eWord)
    try:
        await interaction.response.send_message(embed=embed)
    except errors.NotFound:
        await channel.send("Interaction took too long to load.", embed=embed)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(os.environ['DISCORD_API_KEY'], log_handler=handler)
        
        


