from discord import Embed, InteractionMessage, Interaction, SelectOption
from discord.components import SelectOption
from discord.interactions import Interaction
from discord.ui import View, Button, Select, Item, button
from poketranslator import translateText, Style
from poketools.pokemon.pokecalc import *
from pokemon.pokeobject import PokeObject
from poketypes.default import Default
from random import choice

from random import Random


class PokeStats(Embed):
    """Creates a stats page for Pokemon. Is a discord embed object.

    Args:
        Embed (_type_): Discord.Embed
    """

    def __init__(self, pokemon: PokeObject):
        super().__init__(
            colour=Style(pokemon.versions[0].pokedex_data.poke_types[0])[1],
            title=translateText(Style(pokemon.versions[0].pokedex_data.poke_types[0])[0], "stats"),
            description=f"{createSeparator(10)}",
        )
        self.set_thumbnail(url=pokemon.versions[0].images.discord_image)

        version = pokemon.versions[0]
        style = Style(pokemon.versions[0].pokedex_data.poke_types[0])[0]

        self.add_field(
            name=f"{translateText(text_style=style, text='HP')} [{int(version.base_stats.hp.base)}/{int(version.base_stats.hp.minimum)}]",
            value=f"{createBar(calcBar(int(version.base_stats.hp.base), int(version.base_stats.hp.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Attack')} [{int(version.base_stats.attack.base)}/{int(version.base_stats.attack.minimum)}]",
            value=f"{createBar(calcBar(int(version.base_stats.attack.base), int(version.base_stats.attack.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Defense')} [{int(version.base_stats.defense.base)}/{int(version.base_stats.defense.minimum)}]",
            value=f"{createBar(calcBar(int(version.base_stats.defense.base), int(version.base_stats.defense.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Sp Atk')} [{int(version.base_stats.sp_atk.base)}/{int(version.base_stats.sp_atk.minimum)}]",
            value=f"{createBar(calcBar(int(version.base_stats.sp_atk.base), int(version.base_stats.sp_atk.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Sp Def')} [{int(version.base_stats.sp_def.base)}/{int(version.base_stats.sp_def.minimum)}]",
            value=f"{createBar(calcBar(int(version.base_stats.sp_def.base), int(version.base_stats.sp_def.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Speed')} [{int(version.base_stats.speed.base)}/{int(version.base_stats.speed.minimum)}]",
            value=f"{createBar(calcBar(int(version.base_stats.speed.base), int(version.base_stats.speed.minimum)), style)}",
            inline=False,
        )

        self.add_field(
            name=f"{createSeparator(10)}",
            value=f'{translateText(text_style=style, text="Total")} **[{version.base_stats.total}]**',
        )


class PokeInfo(Embed):
    def __init__(self, pokemon: PokeObject):
        super().__init__(
            colour=Style(pokemon.versions[0].pokedex_data.poke_types[0])[1],
            title="Search Result",
            description=f"{translateText(text_style=Style(pokemon.versions[0].pokedex_data.poke_types[0])[0], text=pokemon.name)}",
        )
        types = ""

        for s in pokemon.versions[0].pokedex_data.poke_types:
            types += Style(style=s)[0].ICON.value
            types += Default.BLANK.value

        self.add_field(name=types, value=str(createSeparator(16)), inline=False)

        if len(pokemon.entries) > 0:
            version, entry = choice(list(pokemon.entries.items()))
            rand = Random()
            entry_val = entry.entries[rand.randint(0, len(entry.entries) - 1)]
            self.add_field(
                name="Pokedex Entry:",
                value=f"{entry_val.text}",
                inline=False,
            )
        else:
            self.add_field(name="Pokedex Entry:", value="???", inline=False)
        self.set_image(url=pokemon.versions[0].images.discord_image)


# class PokePokedex(Embed):
#     def __init__(self, pokemon: PokeObject):
#         style = Style(pokemon.versions[0].pokedex_data.poke_types[0])[0]
#         super().__init__(
#             colour=Style(pokemon.versions[0].pokedex_data.poke_types[0])[1],
#             title=translateText(style, "pokedex"),
#             description=f"{createSeparator(10)}",
#         )

#         version: PokeObject.Version = pokemon.versions[0]
#         self.set_thumbnail(url=style.ICON_IMAGE.value)
#         self.add_field(
#             name=f'{translateText(text_style=style, text="number")}',
#             value=f"{version.national_number}",
#             inline=False,
#         )
#         self.add_field(name=f"{Default.BLANK.value}", value="")
#         self.add_field(
#             name=f'{translateText(text_style=style, text="species")}',
#             value=f"{version.species}",
#             inline=False,
#         )
#         self.add_field(name=f"{Default.BLANK.value}", value="")
#         self.add_field(
#             name=f'{translateText(text_style=style, text="weight")}',
#             value=f"{version.weight}",
#             inline=False,
#         )
#         self.add_field(name=f"{Default.BLANK.value}", value="")
#         self.add_field(
#             name=f'{translateText(text_style=style, text="height")}',
#             value=f"{version.height}",
#             inline=False,
#         )
#         self.add_field(name=f"{Default.BLANK.value}", value="")
#         self.add_field(
#             name=f'{translateText(text_style=style, text="base xp")}',
#             value=f"{version.base_xp}",
#             inline=False,
#         )
#         self.add_field(name=f"{Default.BLANK.value}", value="")
#         self.add_field(
#             name=f'{translateText(text_style=style, text="growth")}',
#             value=f"{version.growth_rate}",
#             inline=False,
#         )
#         self.add_field(name=f"{Default.BLANK.value}", value="")
#         self.add_field(
#             name=f'{translateText(text_style=style, text="catch")}',
#             value=f"{version.catch_rate}",
#             inline=False,
#         )


# class PokeAttacks(Embed):
#     def __init__(self, pokemon: PokeObject):
#         style = Style(pokemon.versions[0].pokedex_data.poke_types[0])[0]
#         super().__init__(
#             colour=Style(pokemon.versions[0].pokedex_data.poke_types[0])[1],
#             title=translateText(style, "moves"),
#             description=f"{createSeparator(10)}",
#         )


class TestPrag(View):
    def __init__(self, pages: list[Embed]):
        super().__init__(timeout=600)
        self.pages = pages
        self.page_len = len(pages)

    async def send(self, message: InteractionMessage):
        self.curr_page = 0
        # Make custom select object that is able to do callback functions.
        # Add Embeds to a list and somehow make the buttons show each embed
        self.prevButton.disabled = True
        await message.edit(embed=self.pages[self.curr_page], view=self)
        self.message = message

    @button(label="Prev")
    async def prevButton(self, interaction: Interaction, button: Button):
        await interaction.response.defer()
        self.curr_page -= 1
        # print('Previous new page:', self.curr_page)

        if self.curr_page == 0:
            # print('Disabling')
            self.prevButton.disabled = True
            self.nextButton.disabled = False
        else:
            self.nextButton.disabled = False

        await self.message.edit(embed=self.pages[self.curr_page], view=self)

    @button(label="Next")
    async def nextButton(self, interaction: Interaction, button: Button):
        await interaction.response.defer()
        self.curr_page += 1
        # print('Next new page:', self.curr_page)

        if self.curr_page + 1 == self.page_len:
            # print('Disabling')
            self.nextButton.disabled = True
            self.prevButton.disabled = False
        else:
            self.prevButton.disabled = False

        await self.message.edit(embed=self.pages[self.curr_page], view=self)


# class VersionSelect(Select):
#     # Takes in the message and edits it based on the version selected.
#     def __init__(self, versions: list) -> None:
#         options = [SelectOption(label=v, value=v) for v in versions]
#         super().__init__(min_values=1, max_values=1, options=options)

#         self.options[0].default = True

#     async def callback(self, interaction: Interaction):
#         await interaction.response.send_message(
#             f"Selected: {self.values[0]}", ephemeral=True
#         )
