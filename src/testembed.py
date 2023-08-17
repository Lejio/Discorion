from random import Random
from typing import List
from discord.colour import Colour
from discord.types.embed import EmbedType
from discord.ui import Select, button, View, Button
from discord import SelectOption, Interaction, Message, InteractionMessage, Embed
from poketools.pokemon.pokecalc import calcBar, createBar, createSeparator, translateText
from poketranslator import Style

from pymongo.collection import Collection

from pokemon.pokeobject import PokeObject
from poketypes.default import Default


class PokedexExtras(Embed):
    
    def __init__(self, pokemon: PokeObject):
        style = Style(pokemon.versions[0].type[0])[0]
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title=translateText(style, 'pokedex'), description=f"{createSeparator(10)}")
        
        version: PokeObject.Version = pokemon.versions[0]
        self.set_thumbnail(url=style.ICON_IMAGE.value)
        self.add_field(name=f'{translateText(text_style=style, text="number")}', value=f'{version.national_number}', inline=False)
        self.add_field(name=f'{Default.BLANK.value}', value='')
        self.add_field(name=f'{translateText(text_style=style, text="species")}', value=f'{version.species}', inline=False)
        self.add_field(name=f'{Default.BLANK.value}', value='')
        self.add_field(name=f'{translateText(text_style=style, text="weight")}', value=f'{version.weight}', inline=False)
        self.add_field(name=f'{Default.BLANK.value}', value='')
        self.add_field(name=f'{translateText(text_style=style, text="height")}', value=f'{version.height}', inline=False)
        self.add_field(name=f'{Default.BLANK.value}', value='')
        self.add_field(name=f'{translateText(text_style=style, text="base xp")}', value=f'{version.base_xp}', inline=False)
        self.add_field(name=f'{Default.BLANK.value}', value='')
        self.add_field(name=f'{translateText(text_style=style, text="growth")}', value=f'{version.growth_rate}', inline=False)
        self.add_field(name=f'{Default.BLANK.value}', value='')
        self.add_field(name=f'{translateText(text_style=style, text="catch")}', value=f'{version.catch_rate}', inline=False)

class PokedexStats(Embed):
    
    def __init__(self, pokemon: PokeObject):
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title=translateText(Style(pokemon.versions[0].type[0])[0], 'stats'), description=f"{createSeparator(10)}")

        self.set_thumbnail(url=pokemon.discord_image)
        
        version = pokemon.versions[0]
        style = Style(pokemon.versions[0].type[0])[0]
                
        self.add_field(name=f"{translateText(text_style=style, text='HP')} [{int(version.stats['HP'].base)}/{int(version.stats['HP'].min)}]", value=f"{createBar(calcBar(int(version.stats['HP'].base), int(version.stats['HP'].min)), style)}", inline=False)
        
        self.add_field(name=f'{Default.BLANK.value}', value='')
        
        self.add_field(name=f"{translateText(text_style=style, text='Attack')} [{int(version.stats['Attack'].base)}/{int(version.stats['Attack'].min)}]", value=f"{createBar(calcBar(int(version.stats['Attack'].base), int(version.stats['Attack'].min)), style)}", inline=False)
        
        self.add_field(name=f'{Default.BLANK.value}', value='')
        
        self.add_field(name=f"{translateText(text_style=style, text='Defense')} [{int(version.stats['Defense'].base)}/{int(version.stats['Defense'].min)}]", value=f"{createBar(calcBar(int(version.stats['Defense'].base), int(version.stats['Defense'].min)), style)}", inline=False)
        
        self.add_field(name=f'{Default.BLANK.value}', value='')
        
        self.add_field(name=f"{translateText(text_style=style, text='Sp Atk')} [{int(version.stats['Sp. Atk'].base)}/{int(version.stats['Sp. Atk'].min)}]", value=f"{createBar(calcBar(int(version.stats['Sp. Atk'].base), int(version.stats['Sp. Atk'].min)), style)}", inline=False)
        
        self.add_field(name=f'{Default.BLANK.value}', value='')
        
        self.add_field(name=f"{translateText(text_style=style, text='Sp Def')} [{int(version.stats['Sp. Def'].base)}/{int(version.stats['Sp. Def'].min)}]", value=f"{createBar(calcBar(int(version.stats['Sp. Def'].base), int(version.stats['Sp. Def'].min)), style)}", inline=False)
        
        self.add_field(name=f'{Default.BLANK.value}', value='')
        
        self.add_field(name=f"{translateText(text_style=style, text='Speed')} [{int(version.stats['Speed'].base)}/{int(version.stats['Speed'].min)}]", value=f"{createBar(calcBar(int(version.stats['Speed'].base), int(version.stats['Speed'].min)), style)}", inline=False)
        
        self.add_field(name=f'{createSeparator(10)}', value=f'{translateText(text_style=style, text="Total")} **[{version.stats["Total"]}]**')
        
class PokedexFrontPage(Embed):
    
    def __init__(self, pokemon: PokeObject):
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title='Search Result', description=f"{translateText(text_style=Style(pokemon.versions[0].type[0])[0], text=pokemon.name)}")        
        types = ''
        
        for s in pokemon.versions[0].type:
            types += Style(style=s)[0].ICON.value
            types += Default.BLANK.value
            
        
        self.add_field(name=types, value=str(createSeparator(16)), inline=False)
        
        if len(pokemon.pokedex_entries) > 0:
            rand = Random()
            entry = rand.randint(0, len(pokemon.pokedex_entries) - 1)
            self.add_field(name='Pokedex Entry:', value=pokemon.pokedex_entries[entry].entries[rand.randint(0, len(pokemon.pokedex_entries[entry].entries) - 1)], inline=False)
        else:
            self.add_field(name='Pokedex Entry:', value="???", inline=False)
        self.set_image(url=pokemon.discord_image)    

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
        
class EvolutionInformation(View):
    
    class EvolutionPage(Embed):
        def __init__(self, stage_number: int = None, pokemon: PokeObject = PokeObject, requirement: str | None = None, no_evolution = False):
            if no_evolution:
                super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title=f'This pokemon has no evolutions.')
                return None
            super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title=f'Evolution stage {stage_number}', description=f"{translateText(text_style=Style(pokemon.versions[0].type[0])[0], text=pokemon.name)}")        
            types: str = ''
            self._stage = stage_number
            self._name = pokemon.name
            for s in pokemon.versions[0].type:
                types += Style(style=s)[0].ICON.value
                types += Default.BLANK.value
                
            self.add_field(name=types, value=str(createSeparator(16)), inline=False)
            
            if len(pokemon.pokedex_entries) > 0:
                rand = Random()
                entry = rand.randint(0, len(pokemon.pokedex_entries) - 1)
                self.add_field(name='Pokedex Entry:', value=pokemon.pokedex_entries[entry].entries[rand.randint(0, len(pokemon.pokedex_entries[entry].entries) - 1)], inline=False)
            else:
                self.add_field(name='Pokedex Entry:', value="???", inline=False)
            self.set_image(url=pokemon.discord_image)
            
            self.add_field(name='**Requirement**', value=requirement[1:-1] if requirement is not None else 'None', inline=False)

        
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
        self.raw_evolution_tree = pokemon.evolution_tree if pokemon.evolution_tree != [] else []
        self.pages = self.generate_pages()
        self.page_len = len(self.pages)
        
    def find_stage(self, _id: str) -> PokeObject:
        
        pokeCollection: Collection = self.cache['mongodb']['pokemon']
        return PokeObject(pokeCollection.find_one({ "_id": _id})['data'])    
    
    def generate_pages(self) -> List[Embed]:
        
        pages: List[self.EvolutionPage] = []
        evo_tree: dict = {}
        evo_cnt: int = 1
        
        if self.raw_evolution_tree == []:
                pages.append(self.EvolutionPage(pokemon=self.pokemon, no_evolution = True))
                return pages
            
        for tree in self.raw_evolution_tree:
            for stage in tree:
                if pages == []:
                    pages.append(self.EvolutionPage(stage_number=evo_cnt, pokemon=self.find_stage(int(stage['from']['nationalNo'][1:]))))
                    evo_tree[str(int(stage['from']['nationalNo'][1:]))] = evo_cnt
                    
                    evo_cnt += 1
                    
                    pages.append(self.EvolutionPage(stage_number=evo_cnt, pokemon=self.find_stage(int(stage['to']['nationalNo'][1:])), requirement=stage['requirement']))
                    evo_tree[str(int(stage['to']['nationalNo'][1:]))] = evo_cnt
                else:
                    from_stage = evo_tree.get(str(int(stage['from']['nationalNo'][1:])))
                    
                    if from_stage:
                        pages.append(self.EvolutionPage(stage_number=from_stage + 1, pokemon=self.find_stage(int(stage['to']['nationalNo'][1:])), requirement=stage['requirement']))
                        evo_tree[str(int(stage['to']['nationalNo'][1:]))] = from_stage + 1
                        
                    else:

                        raise Exception(f'From evolution is {from_stage} even though it is not the base pokemon.')
                
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
            super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title='Moves Page', description=f'Page {num} of the moves page')
            
            if len(range_) != 2:
                raise IndexError('Invalid pair range.')
            
            
            try:
                self.add_field(name='Moves', value=str(pokemon.attacks))
            except Exception:
                print(str(pokemon.attacks))
            
    def __init__(self, pokemon: PokeObject):
        super().__init__(timeout=600)
        self.pages = [self.MovesPage(pokemon, 1, [0,0])]
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

            self.nextButton.disabled = True
            self.prevButton.disabled = False
        else:
            self.prevButton.disabled = False
              
        
        await self.message.edit(embed=self.pages[self.curr_page], view=self)

class PokemonPage(dict):
    
    def __init__(self, pokemon: PokeObject, cache):
        
        self['Pokedex Information'] = PokedexInformation([PokedexFrontPage(pokemon), PokedexStats(pokemon), PokedexExtras(pokemon)])
        self['Evolution Information'] = EvolutionInformation(cache=cache, pokemon=pokemon)
        self['Moves Information'] = MovesInformation(pokemon)

class PokemonSelect(Select):
    
    def __init__(self, pokemon: PokeObject, cache, message: InteractionMessage) -> None:
        pokepage = PokemonPage(cache=cache, pokemon=pokemon)
        options = [SelectOption(label=v, value=v) for v in pokepage]
        super().__init__(min_values=1, max_values=1, options=options)
        self.cache = cache
        self.pokemon = pokemon
        self.message = message
        self.options[0].default = True
        self.default_val = self.options[0]
        
    async def send(self):
        pokepage = None
        
        match self.options[0].value:
            case 'Pokedex Information':
                pokepage = PokedexInformation([PokedexFrontPage(self.pokemon), PokedexStats(self.pokemon), PokedexExtras(self.pokemon)])
            case 'Evolution Information':
                pokepage = EvolutionInformation(self.cache, pokemon=self.pokemon)
            case 'Moves Information':
                pokepage = MovesInformation(self.pokemon)
        
        await pokepage.send(message=self.message, select=self)
            
    async def callback(self, interaction: Interaction):
        
        self.default_val.default = False
        
        pokepage = None
        match self.values[0]:
            case 'Pokedex Information':
                pokepage = PokedexInformation([PokedexFrontPage(self.pokemon), PokedexStats(self.pokemon), PokedexExtras(self.pokemon)])
                self.options[0].default = True
                self.default_val = self.options[0]
            case 'Evolution Information':
                pokepage = EvolutionInformation(cache=self.cache, pokemon=self.pokemon)
                self.options[1].default = True
                self.default_val = self.options[1]
            case 'Moves Information':
                pokepage = MovesInformation(pokemon=self.pokemon)
                self.options[2].default = True
                self.default_val = self.options[2]
                
        await interaction.response.defer()
        await pokepage.send(message=self.message, select=self)