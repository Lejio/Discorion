
import discord
from discord import app_commands
from discord.ext import commands

import random

from pokeutils import Types, PokeTranslator, StyleBundler

types = StyleBundler()

@app_commands.default_permissions(administrator=True)
class PokeCatch(commands.GroupCog):
    
    def __init__(self, client: commands.Bot) -> None:
        super().__init__()

        self.client = client;
        self.registry = client.registry
        self.cache = client.cache
        self.catch_registry = client.catch_registry

    # https://discordpy.readthedocs.io/en/stable/api.html?highlight=create_role#discord.Guild.create_role
    @app_commands.command(name="catch", description="Spawns a random pokemon from the selected type.")
    @app_commands.describe(type_="Available types.")
    @app_commands.choices(type_=[discord.app_commands.Choice(name=type_, value=type_) for type_ in types])

    async def spawnRandomPokemon(self, interaction: discord.Interaction, type_: discord.app_commands.Choice[str]):
        
        random_pokemon = random.choices(self.catch_registry[type_.value]['name'], self.catch_registry[type_.value]['catch_rate'])
    
        await interaction.response.send_message(random_pokemon)
    
        
async def setup(bot: commands.Bot):
    await bot.add_cog(PokeCatch(bot))