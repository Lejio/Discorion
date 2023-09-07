from random import Random
from typing import Dict, List
from discord.colour import Colour
from discord.types.embed import EmbedType
from discord.ui import Select, button, View, Button
from discord import SelectOption, Interaction, Message, InteractionMessage, Embed
from poketools.pokemon.pokecalc import (
    calcBar,
    createBar,
    createSeparator,
    translateText,
)
from poketranslator import Style

from pymongo.collection import Collection

from pokemon.pokeobject import PokeObject
from poketypes.default import Default

# CONSTANTS:
SEPARATOR_LENGTH = 10
DEFAULT_VERSION = 0
DEFAULT_TYPE = 0


class PokedexExtras(Embed):
    def __init__(self, pokemon: PokeObject.Version):
        style = Style(pokemon.pokedex_data.poke_types[DEFAULT_TYPE])[0]
        super().__init__(
            colour=Style(pokemon.pokedex_data.poke_types[DEFAULT_TYPE])[1],
            title=translateText(style, "pokedex"),
            description=f"{createSeparator(SEPARATOR_LENGTH)}",
        )

        self.set_thumbnail(url=style.ICON_IMAGE.value)
        self.add_field(
            name=f'{translateText(text_style=style, text="number")}',
            value=f"{pokemon.pokedex_data.national_no}",
            inline=False,
        )
        self.add_field(name=f"{Default.BLANK.value}", value="")
        self.add_field(
            name=f'{translateText(text_style=style, text="species")}',
            value=f"{pokemon.pokedex_data.species}",
            inline=False,
        )
        self.add_field(name=f"{Default.BLANK.value}", value="")
        self.add_field(
            name=f'{translateText(text_style=style, text="weight")}',
            value=f"{pokemon.pokedex_data.weight}",
            inline=False,
        )
        self.add_field(name=f"{Default.BLANK.value}", value="")
        self.add_field(
            name=f'{translateText(text_style=style, text="height")}',
            value=f"{pokemon.pokedex_data.height}",
            inline=False,
        )
        self.add_field(name=f"{Default.BLANK.value}", value="")
        self.add_field(
            name=f'{translateText(text_style=style, text="base xp")}',
            value=f"{pokemon.training_data.base_exp}",
            inline=False,
        )
        self.add_field(name=f"{Default.BLANK.value}", value="")
        self.add_field(
            name=f'{translateText(text_style=style, text="growth")}',
            value=f"{pokemon.training_data.growth_rate}",
            inline=False,
        )
        self.add_field(name=f"{Default.BLANK.value}", value="")
        self.add_field(
            name=f'{translateText(text_style=style, text="catch")}',
            value=f"{pokemon.training_data.catch_rate}",
            inline=False,
        )


class PokedexStats(Embed):
    def __init__(self, pokemon: PokeObject.Version):
        style = Style(pokemon.pokedex_data.poke_types[0])
        super().__init__(
            colour=style[1],
            title=translateText(style[0], "stats"),
            description=f"{createSeparator(SEPARATOR_LENGTH)}",
        )

        self.set_thumbnail(url=pokemon.images.discord_image)
        style = Style(pokemon.pokedex_data.poke_types[DEFAULT_TYPE])[0]
        pokemon_stats = pokemon.base_stats

        self.add_field(
            name=f"{translateText(text_style=style, text='HP')} [{int(pokemon_stats.hp.base)}/{int(pokemon_stats.hp.minimum)}]",
            value=f"{createBar(calcBar(int(pokemon_stats.hp.base), int(pokemon_stats.hp.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Attack')} [{int(pokemon_stats.attack.base)}/{int(pokemon_stats.attack.minimum)}]",
            value=f"{createBar(calcBar(int(pokemon_stats.attack.base), int(pokemon_stats.attack.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Defense')} [{int(pokemon_stats.defense.base)}/{int(pokemon_stats.defense.minimum)}]",
            value=f"{createBar(calcBar(int(pokemon_stats.defense.base), int(pokemon_stats.defense.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Sp Atk')} [{int(pokemon_stats.sp_atk.base)}/{int(pokemon_stats.sp_atk.minimum)}]",
            value=f"{createBar(calcBar(int(pokemon_stats.sp_atk.base), int(pokemon_stats.sp_atk.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Sp Def')} [{int(pokemon_stats.sp_def.base)}/{int(pokemon_stats.sp_def.minimum)}]",
            value=f"{createBar(calcBar(int(pokemon_stats.sp_def.base), int(pokemon_stats.sp_def.minimum)), style)}",
            inline=False,
        )

        self.add_field(name=f"{Default.BLANK.value}", value="")

        self.add_field(
            name=f"{translateText(text_style=style, text='Speed')} [{int(pokemon_stats.speed.base)}/{int(pokemon_stats.speed.minimum)}]",
            value=f"{createBar(calcBar(int(pokemon_stats.speed.base), int(pokemon_stats.speed.minimum)), style)}",
            inline=False,
        )

        self.add_field(
            name=f"{createSeparator(SEPARATOR_LENGTH)}",
            value=f'{translateText(text_style=style, text="Total")} **[{pokemon_stats.total}]**',
        )


class PokedexFrontPage(Embed):
    def __init__(
        self,
        pokemon: PokeObject.Version,
        default_pokemon,
        entries: Dict[str, PokeObject.EntryVersion],
    ):
        super().__init__(
            colour=Style(pokemon.pokedex_data.poke_types[DEFAULT_TYPE])[1],
            title="Search Result",
            description=f"{translateText(text_style=Style(pokemon.pokedex_data.poke_types[DEFAULT_TYPE])[0], text=pokemon.name)}",
        )
        types = ""

        for s in pokemon.pokedex_data.poke_types:
            types += Style(style=s)[0].ICON.value
            types += Default.BLANK.value

        self.add_field(
            name=types, value=str(createSeparator(SEPARATOR_LENGTH + 6)), inline=False
        )

        # Randomizeing a entry for display.
        # -- Might mean the number of versions a pokemon has?

        try:
            if len(entries[pokemon.name].entries) > 0:
                rand = Random()
                self.add_field(
                    name="Pokedex Entry:",
                    value=entries[pokemon.name]
                    .entries[rand.randint(0, len(entries[pokemon.name].entries) - 1)]
                    .text,
                    inline=False,
                )
            else:
                self.add_field(name="Pokedex Entry:", value="???", inline=False)
        except KeyError:
            rand = Random()
            self.add_field(
                name="Pokedex Entry:",
                value=entries[default_pokemon]
                .entries[rand.randint(0, len(entries[default_pokemon].entries) - 1)]
                .text,
                inline=False,
            )
        self.set_image(url=pokemon.images.discord_image)


class PokedexInformation(View):
    def __init__(self, pages: [Embed]):
        super().__init__(timeout=600)
        self.pages = pages
        self.page_len = len(pages)

    async def send(self, message: InteractionMessage, select: Select):
        self.add_item(select)
        self.curr_page = 0
        # Make custom select object that is able to do callback functions.
        # Add Embeds to a list and somehow make the buttons show each embed
        self.prevButton.disabled = True

        if self.page_len == 1:
            self.nextButton.disabled = True

        await message.edit(embed=self.pages[self.curr_page], view=self)
        self.message = message

    @button(label="Prev")
    async def prevButton(self, interaction: Interaction, button: Button):
        await interaction.response.defer()
        self.curr_page -= 1

        if self.curr_page == 0:
            self.prevButton.disabled = True
            self.nextButton.disabled = False
        else:
            self.nextButton.disabled = False

        await self.message.edit(embed=self.pages[self.curr_page], view=self)

    @button(label="Next")
    async def nextButton(self, interaction: Interaction, button: Button):
        await interaction.response.defer()
        self.curr_page += 1

        if self.curr_page + 1 == self.page_len:
            self.nextButton.disabled = True
            self.prevButton.disabled = False
        else:
            self.prevButton.disabled = False

        await self.message.edit(embed=self.pages[self.curr_page], view=self)


class EvolutionInformation(View):
    class EvolutionPage(Embed):
        def __init__(
            self,
            stage_number: int = None,
            pokemon: PokeObject = PokeObject,
            requirement: str | None = None,
            no_evolution=False,
        ):
            if no_evolution:
                super().__init__(
                    colour=Style(
                        pokemon.versions[DEFAULT_VERSION].pokedex_data.poke_types[
                            DEFAULT_TYPE
                        ]
                    )[1],
                    title=f"This pokemon has no evolutions.",
                )
                return None
            super().__init__(
                colour=Style(
                    pokemon.versions[DEFAULT_VERSION].pokedex_data.poke_types[
                        DEFAULT_TYPE
                    ]
                )[1],
                title=f"Evolution stage {stage_number}",
                description=f"{translateText(text_style=Style(pokemon.versions[DEFAULT_VERSION].pokedex_data.poke_types[DEFAULT_TYPE])[0], text=pokemon.name)}",
            )
            types: str = ""
            self._stage = stage_number
            self._name = pokemon.name
            for s in pokemon.versions[DEFAULT_VERSION].pokedex_data.poke_types:
                types += Style(style=s)[0].ICON.value
                types += Default.BLANK.value

            self.add_field(
                name=types,
                value=str(createSeparator(SEPARATOR_LENGTH + 6)),
                inline=False,
            )

            if len(pokemon.entries) > 0:
                rand = Random()
                print(pokemon.entries[rand.choice(list(pokemon.entries))])
                self.add_field(
                    name="Pokedex Entry:",
                    value=0,
                    inline=False,
                )
            else:
                self.add_field(name="Pokedex Entry:", value="???", inline=False)
            self.set_image(url=pokemon.versions[0].images.discord_image)

            self.add_field(
                name="**Requirement**",
                value=requirement[1:-1] if requirement is not None else "None",
                inline=False,
            )

        @property
        def name(self) -> str:
            return self._name

        @property
        def stage(self) -> int:
            return self._stage

    def __init__(self, cache, pokemon: PokeObject) -> None:
        super().__init__(timeout=600)
        self.pokemon = pokemon
        self.cache = cache
        self.raw_evolutions = pokemon.evolutions if pokemon.evolutions != [] else []
        self.pages = self.generate_pages()
        self.page_len = len(self.pages)

    def find_stage(self, _id: str) -> PokeObject:
        pokeCollection: Collection = self.cache["mongodb"]["pokemon"]
        return PokeObject(pokeCollection.find_one({"_id": _id})["data"])

    def generate_pages(self) -> List[Embed]:
        pages: List[self.EvolutionPage] = []
        evo_tree: dict = {}
        evo_cnt: int = 1

        if self.raw_evolutions == []:
            pages.append(self.EvolutionPage(pokemon=self.pokemon, no_evolution=True))
            return pages

        for tree in self.raw_evolutions:
            for stage in tree:
                if pages == []:
                    pages.append(
                        self.EvolutionPage(
                            stage_number=evo_cnt,
                            pokemon=self.find_stage(stage.evolution_from.national_no),
                        )
                    )
                    evo_tree[str(stage.evolution_from.national_no)] = evo_cnt

                    evo_cnt += 1

                    pages.append(
                        self.EvolutionPage(
                            stage_number=evo_cnt,
                            pokemon=self.find_stage(stage.evolution_to.national_no),
                            requirement=stage.requirement,
                        )
                    )
                    evo_tree[str(stage.evolution_to.national_no)] = evo_cnt
                else:
                    from_stage = evo_tree.get(str(stage.evolution_from.national_no))

                    if from_stage:
                        pages.append(
                            self.EvolutionPage(
                                stage_number=from_stage + 1,
                                pokemon=self.find_stage(stage.evolution_to.national_no),
                                requirement=stage.requirement,
                            )
                        )
                        evo_tree[str(stage.evolution_to.national_no)] = from_stage + 1

                    else:
                        raise Exception(
                            f"From evolution is {from_stage} even though it is not the base pokemon."
                        )

        return pages

    async def send(self, message: InteractionMessage, select: Select):
        self.curr_page: int = 0
        # Make custom select object that is able to do callback functions.
        # Add Embeds to a list and somehow make the buttons show each embed
        self.prevButton.disabled = True

        if self.page_len == 1:
            self.nextButton.disabled = True

        self.add_item(select)
        await message.edit(embed=self.pages[self.curr_page], view=self)
        self.message = message

    @button(label="Prev")
    async def prevButton(self, interaction: Interaction, button: Button):
        await interaction.response.defer()
        self.curr_page -= 1

        if self.curr_page == 0:
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


class MovesInformation(View):
    class MovesPage(Embed):
        def __init__(self, pokemon: PokeObject, num: int, range_: List[int]):
            super().__init__(
                colour=Style(pokemon.versions[DEFAULT_VERSION].type[DEFAULT_TYPE])[1],
                title="Moves Page",
                description=f"Page {num} of the moves page",
            )

            if len(range_) != 2:
                raise IndexError("Invalid pair range.")

            try:
                self.add_field(name="Moves", value=str(pokemon.attacks))
            except Exception:
                print(str(pokemon.attacks))

    def __init__(self, pokemon: PokeObject):
        super().__init__(timeout=600)
        self.pages = [self.MovesPage(pokemon, 1, [0, 0])]
        self.page_len = len(self.pages)

    async def send(self, message: InteractionMessage, select: Select):
        self.curr_page = 0
        # Make custom select object that is able to do callback functions.
        # Add Embeds to a list and somehow make the buttons show each embed
        self.prevButton.disabled = True

        if self.page_len == 1:
            self.nextButton.disabled = True

        self.add_item(select)
        await message.edit(embed=self.pages[self.curr_page], view=self)
        self.message = message

    @button(label="Prev")
    async def prevButton(self, interaction: Interaction, button: Button):
        await interaction.response.defer()
        self.curr_page -= 1

        if self.curr_page == 0:
            self.prevButton.disabled = True
            self.nextButton.disabled = False
        else:
            self.nextButton.disabled = False

        await self.message.edit(embed=self.pages[self.curr_page], view=self)

    @button(label="Next")
    async def nextButton(self, interaction: Interaction, button: Button):
        await interaction.response.defer()
        self.curr_page += 1

        if self.curr_page + 1 == self.page_len:
            self.nextButton.disabled = True
            self.prevButton.disabled = False
        else:
            self.prevButton.disabled = False

        await self.message.edit(embed=self.pages[self.curr_page], view=self)


class PokemonPage(dict):
    def __init__(self, pokemon: PokeObject, cache):
        for version in range(len(pokemon.versions)):
            self[pokemon.versions[version].name] = PokedexInformation(
                [
                    PokedexFrontPage(
                        pokemon.versions[version],
                        pokemon.versions[0].name,
                        pokemon.entries,
                    ),
                    PokedexStats(pokemon.versions[version]),
                    PokedexExtras(pokemon.versions[version]),
                ]
            )
        self["Evolution Information"] = EvolutionInformation(
            cache=cache, pokemon=pokemon
        )
        self["Moves Information"] = MovesInformation(pokemon)


class PokemonSelect(Select):
    def __init__(self, pokemon: PokeObject, cache, message: InteractionMessage) -> None:
        self.pokepage_dictionary = PokemonPage(cache=cache, pokemon=pokemon)
        options = [SelectOption(label=v, value=v) for v in self.pokepage_dictionary]
        super().__init__(min_values=1, max_values=1, options=options)
        self.cache = cache
        self.pokemon = pokemon
        self.pokemon_version_len = len(self.pokemon.versions)
        self.message = message
        self.options[0].default = True
        self.default_val = self.options[0]

    async def send(self):
        # This should be the default sending of the Embed, therefore it should display the first version of the pokemon every single time.

        # pokepage = None
        # value = self.pokemon.versions[0].name
        chosen_version = 0
        # match value:
        #     case "Evolution Information":
        #         pokepage = EvolutionInformation(self.cache, pokemon=self.pokemon)
        #     case "Moves Information":
        #         pokepage = MovesInformation(self.pokemon)
        #     case _:
        pokepage = PokedexInformation(
            [
                PokedexFrontPage(
                    self.pokemon.versions[chosen_version],
                    self.pokemon.versions[0].name,
                    self.pokemon.entries,
                ),
                PokedexStats(self.pokemon.versions[chosen_version]),
                PokedexExtras(self.pokemon.versions[chosen_version]),
            ]
        )

        await pokepage.send(message=self.message, select=self)

    async def callback(self, interaction: Interaction):
        self.default_val.default = False
        pokepage = None
        value = self.values[0]

        match value:
            case "Evolution Information":
                pokepage = EvolutionInformation(cache=self.cache, pokemon=self.pokemon)
                self.options[self.pokemon_version_len + 1].default = True
                self.default_val = self.options[self.pokemon_version_len + 1]
            case "Moves Information":
                pokepage = MovesInformation(pokemon=self.pokemon)
                self.options[self.pokemon_version_len + 2].default = True
                self.default_val = self.options[self.pokemon_version_len + 2]
            case _:
                chosen_value = self.pokemon.versions_list.index(value)

                pokepage = PokedexInformation(
                    [
                        PokedexFrontPage(
                            self.pokemon.versions[chosen_value],
                            self.pokemon.versions[0].name,
                            self.pokemon.entries,
                        ),
                        PokedexStats(self.pokemon.versions[chosen_value]),
                        PokedexExtras(self.pokemon.versions[chosen_value]),
                    ]
                )
                self.options[chosen_value].default = True
                self.default_val = self.options[chosen_value]

        await interaction.response.defer()
        await pokepage.send(message=self.message, select=self)
