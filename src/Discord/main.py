from dotenv import load_dotenv
import os
import math

from discord.ext import commands
from discord import Intents, Guild, Embed, Colour, Interaction 


load_dotenv()

def calcBar(cur: int, max: int) -> int:
    """Calculates amount of bars full.

    Args:
        cur (int): Current stat number.
        max (int): Maximum stat number.

    Returns:
        int: How many bars are full (out of 10).
    """
    
    return math.floor(round(int((cur/max) * 100), 1) / 10)


def createBar(barLevel: int = 0):
    
        # print(barLevel)
        
        BAR_START_EMPTY = "<:bar_start_empty:1125966950854574090>"
        BAR_MIDDLE_EMPTY = "<:bar_middle_empty:1125966934391926824>"
        BAR_END_EMPTY = "<:bar_end_empty:1125966913521057853>"
        
        BAR_START_FILL_ELECTRIC = "<:bar_start_fill_electric:1125967053522739321>"
        BAR_START_FILL_ELECTRIC_END = "<:bar_start_fill2_electric_128:1125985276410466386>"
        BAR_MIDDLE_FILL_ELECTRIC= "<:bar_middle_fill_electric:1125967066894180372>"
        BAR_MIDDLE_FILL_ELECTRIC_END = "<:bar_middle_fill2_electric_128:1125985217438548039>"
        BAR_END_FILL_ELECTRIC = "<:bar_end_fill_electric:1125967075060494487>"
        
        bar = ""
        
        if barLevel == 0:
            
            bar += BAR_START_EMPTY
            bar += 8*BAR_MIDDLE_EMPTY
            bar+= BAR_END_EMPTY
            
            return bar
        
        else:
            
            if barLevel - 1 == 0:
                bar += BAR_START_FILL_ELECTRIC_END
                bar += 8*BAR_MIDDLE_EMPTY
            elif barLevel == 10:
                bar += BAR_START_FILL_ELECTRIC
                bar += 8*BAR_MIDDLE_FILL_ELECTRIC
            else:
                bar += BAR_START_FILL_ELECTRIC
                fill = barLevel - 2
                bar += (fill)*BAR_MIDDLE_FILL_ELECTRIC
                bar += BAR_MIDDLE_FILL_ELECTRIC_END
                bar += (7 - fill)*BAR_MIDDLE_EMPTY
                
                
            if barLevel < 10:
                bar += BAR_END_EMPTY
            else:
                bar += BAR_END_FILL_ELECTRIC
        
        return bar
                
            
def createSeparator(num: int):
    
    return num*"<:separator:1125988800884117514>"
    

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
            
        embed = Embed(colour=Colour.yellow(), title=f"{interaction.user.display_name}'s", description="<:Electric_P2_128:1125980509676249109><:Electric_I2_128:1125980544920981585><:Electric_K2_128:1125980564487405588><:Electric_A2_128:1125980583814774888><:Electric_C2_128:1125980895917121556><:Electric_H2_128:1125980654857883689><:Electric_U2_128:1125980699749523527>")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938114247016548/pikachu-removebg-preview.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938978797916180/Electric_icon_SwSh.png")
        
        embed.add_field(name="", value=f"{createSeparator(10)}", inline=False)
        embed.add_field(name="Level", value=f"5", inline=True)
        embed.add_field(name="", value=f"{createSeparator(10)}", inline=False)
        
        embed.add_field(name="HP [35/180]", value=f"{createBar(calcBar(35, 180))}", inline=False)
        embed.add_field(name="HP [35/180]", value=f"{createBar(calcBar(55, 103))}", inline=False)
        embed.add_field(name="Defense [40/79]", value=f"{createBar(calcBar(40, 79))}", inline=False)
        embed.add_field(name="Special Attack [50/94]", value=f"{createBar(calcBar(50, 94))}", inline=False)
        embed.add_field(name="Special Defense [50/94]", value=f"{createBar(calcBar(50, 94))}", inline=False)
        embed.add_field(name="Speed [90/166]", value=f"{createBar(calcBar(90, 166))}", inline=False)

        
        await interaction.response.send_message(embed=embed)
        
        
        


client.run(os.environ['DISCORD_API_KEY'])
        
        


