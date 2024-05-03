import csv
import time
from dotenv import load_dotenv
import os

from datetime import datetime
import json

import logging
from discord.ext import commands
from discord import File, Intents, Guild, Embed, Colour, Interaction, Emoji, TextChannel

from pymongo.collection import Collection
from discorddata.discorddatabase import DiscordDatabase

from utils.supabase import supabase_loader
from utils.mongodriver import load_mongodb
from poketools.pokemon.pokecalc import *
from poketools.pokegenerator.pokedatabase import FetchWild
from poketranslator import *
from pokemon.pokeobject import PokeObject
from poketools.pokequery import PokeQuery
from pokeembed import *

from testembed import *


load_dotenv()
cogs: list = ["pokestyles", "catch"]
registry = json.load(open("./pokemon/registry_v2.json"))
catch_registry = json.load(open("./pokemon/catch_registry.json"))
cache: dict = {
    "supabase": supabase_loader(),
    "mongodb": load_mongodb()["pokemon_templates"],
}


class Discorion(commands.Bot):
    def __init__(
        self, command_prefix="!p", description: str | None = None, intents=Intents.all()
    ) -> None:
        super().__init__(command_prefix, description=description, intents=intents)

    async def on_ready(self):
        """
        Client event. Runs when the bot is ready and has successfully logged in.
        """

        self.registry = registry
        self.cache = cache
        self.catch_registry = catch_registry

        print("Cache successfully loaded.")

        print(
            f"\n{datetime.utcnow()}: Logged in successfully as: "
            + str(client.user)
            + "\n"
        )

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


@client.tree.command(
    name="search-pokemon",
    description="Searches for a pokemon via pokedex number or name.",
)
async def searchPokemon(interaction: Interaction, name: str):
    message = None

    try:
        int(name)
        query_type = "number_based"
    except ValueError:
        query_type = "name_based"

    queryEngine = PokeQuery(pokemon_object=registry[query_type])
    result_list = queryEngine.query(user_input=name)

    if result_list is None:
        await interaction.response.send_message(
            embed=Embed(colour=Colour.red(), title="404 Error: Pokemon Not Found")
        )
        return
    else:
        await interaction.response.send_message(
            embed=Embed(
                color=Colour.yellow(), title=f"Generating result for {result_list[0]}"
            )
        )
        message = await interaction.original_response()

    pokeCollection: Collection = cache["mongodb"]["pokemon"]
    pokemon_response = PokeObject(
        pokeCollection.find_one({"_id": int(result_list[1]["id"])})["data"]
    )
    print("Creating pokemon response.")
    pokepage = [
        PokeInfo(pokemon=pokemon_response)
        # PokeStats(pokemon=pokemon_response),
        # PokePokedex(pokemon=pokemon_response),
    ]

    testview = TestPrag(pokepage)
    await testview.send(message=message)


@client.tree.command(name="test-select", description="Testing select pagination.")
async def testPagination(interaction: Interaction, poke_id: int):
    await interaction.response.send_message(
        embed=Embed(color=Colour.yellow(), title=f"Generating result for {poke_id}")
    )
    message = await interaction.original_response()

    pokeCollection: Collection = cache["mongodb"]["pokemon"]
    pokemon_response = PokeObject(pokeCollection.find_one({"_id": poke_id})["data"])

    pokeselect = PokemonSelect(pokemon=pokemon_response, message=message, cache=cache)

    await pokeselect.send()


# @client.tree.command(name="get-random-pokemon", description="Searches for a pokemon")
# async def getRandomPokemon(interaction: Interaction):
#     fetch = FetchWild(os.environ['DATABASE_URL'], os.environ['DEFAULT_POKEMON_DATABASE'])

#     pokemon = fetch.getRandom()

#     pokemonMessage = f"Pokedex Number: {pokemon[0]}\n{pokemon[1][pokemon[1]['name']]}"
#     await interaction.response.send_message(pokemonMessage)


@client.tree.command(
    name="upload-sprites",
    description="Uploads sprites and images to both discord and cockroachdb",
)
@commands.check_any(commands.is_owner())
async def uploadSprites(interaction: Interaction):
    # ---------- Defines constant paths to both the json (where the pokemon info is stored) and sprites ----------
    SPRITES_DIR = "/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/"
    IMAGE_DIR = "/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/other/official-artwork/"

    # ---------- Guild number starts a one, and gradually increases as space runs out. ----------
    guild_num = [0]
    # ---------- Saves the channel from interaction to send a message for each emoji created. ----------
    channel = interaction.channel

    # ---------- Sends beginning message to avoid interaction not responded error ----------
    await interaction.response.send_message("Beginning upload.")

    sprite_versions: dict = {}

    with open("pokemon_forms_1_clean.csv", "r") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            """
            row:
            1: The sprite number (int 10000 - 10263)
            2: Pokemon Name (str)
            3: Form (str) - Naming based on Pokemondb.net
            """
            # The pokemon version number.
            current_number = list(row)[0]

            # Catches the first row (which states the column names).
            try:
                int(current_number)
            except ValueError:
                continue

            queryEngine = PokeQuery(pokemon_object=registry["name_based"])
            result_list = queryEngine.query(user_input=row[1])
            # print(result_list)
            # The pokemon number (not the sprite number).
            sprite_number = int(result_list[1]["id"])
            # The pokemon version name.
            version_name = row[2]

            # try:
            #     with open(f'{SPRITES_DIR}{current_number}.png') as sprite:
            #         payload['emoji'] = sprite.name

            #     with open(f'{IMAGE_DIR}{current_number}.png') as image:
            #         payload['png'] = image.name

            # except FileNotFoundError:
            #     print('Not found: ' + current_number)

            payload = await uploader(
                channel=channel, guild_num=guild_num, version_id=current_number
            )

            # Checks if the number already exists in the sprite_versions dictionary.
            if sprite_number in sprite_versions.keys():
                sprite_versions[sprite_number][version_name] = {
                    "sprite": payload["emoji"],
                    "png": payload["png"],
                }

            else:
                # Creates a new key entry.
                sprite_versions[sprite_number] = {}
                sprite_versions[sprite_number][version_name] = {
                    "sprite": payload["emoji"],
                    "png": payload["png"],
                }
            # await channel.send(f'{sprite_number} | {version_name}')
            print(f"{sprite_number} | {version_name}")

            time.sleep(10)

    with open("extra_sprites_v2.json", "w") as outfile:
        json.dump(sprite_versions, outfile, indent=4)


async def uploader(channel: TextChannel, guild_num: list, version_id: str) -> dict:
    SPRITES_DIR = "/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/"
    IMAGE_DIR = "/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/other/official-artwork/"

    # ---------- Changes DiscordDatabase enum into a list ----------
    discord_db = list(DiscordDatabase)

    payload = {"emoji": None, "png": None}
    guild: Guild | None = client.get_guild(discord_db[guild_num[0]].value)

    while len(guild.emojis) == 50:
        guild_num[0] += 1
        guild = client.get_guild(discord_db[guild_num[0]].value)

    try:
        with open(SPRITES_DIR + str(version_id) + ".png", "rb") as image:
            f = image.read()
            imageBytes = bytes(f)

        emoji: Emoji = await guild.create_custom_emoji(
            name=f"P{version_id}", image=imageBytes
        )
        message = await channel.send(file=File(IMAGE_DIR + str(version_id + ".png")))

        image_url = message.attachments[0].url

        payload["emoji"] = f"<:P{version_id}:{emoji.id}>"
        payload["png"] = image_url
    except Exception as error:
        print(f"ERR: {version_id}")
        print(error)

    return payload


handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

client.run(os.environ["DISCORD_API_KEY"], log_handler=handler)
