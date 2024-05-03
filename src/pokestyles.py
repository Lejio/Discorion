import discord
from discord import app_commands
from discord.ext import commands

from pokeutils import Types, PokeTranslator, StyleBundler

styles = StyleBundler()

@app_commands.default_permissions(administrator=True)
class PokeStyles(commands.GroupCog):
    
    def __init__(self, client: commands.Bot) -> None:
        super().__init__()

        self.client = client;


    # https://discordpy.readthedocs.io/en/stable/api.html?highlight=create_role#discord.Guild.create_role
    @app_commands.command(name="style", description="Displays the input text in a certain style.")
    @app_commands.describe(style="Available Styles")
    @app_commands.choices(style=[discord.app_commands.Choice(name=type_, value=type_) for type_ in styles])

    async def displayStyledText(self, interaction: discord.Interaction, style: discord.app_commands.Choice[str], text: str):
        
        translated = PokeTranslator(text=text, style=style.value)
    
        await interaction.response.send_message(translated)
    
        
async def setup(bot: commands.Bot):
    await bot.add_cog(PokeStyles(bot))