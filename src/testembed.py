from random import Random
from discord.colour import Colour
from discord.types.embed import EmbedType
from discord.ui import Select, button, View, Button
from discord import SelectOption, Interaction, Message, InteractionMessage, Embed
from poketools.pokemon.pokecalc import calcBar, createBar, createSeparator, translateText
from poketranslator import Style, StyleBundler

from pokemon.pokeobject import PokeObject
from poketypes.default import Default


class PokedexPageThree(Embed):
    
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

class PokedexPageTwo(Embed):
    
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
        
class PokedexPageOne(Embed):
    
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
  
class MovesPage(Embed):
    def __init__(self, pokemon: PokeObject, num: int):
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title='Moves Page', description=f'Page {num} of the moves page')        

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

class EvolutionPageOne(Embed):
    def __init__(self, pokemon: PokeObject):
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title='Evolution Stage One', description='Stage one in the evolution of this pokemon')
        evolution_tree = pokemon.evolution_tree[0]
        for i in evolution_tree:
            print(i)

class EvolutionPageTwo(Embed):
    def __init__(self, pokemon: PokeObject):
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title='Evolution Stage Two', description='Stage two in the evolution of this pokemon')

class EvolutionPageThree(Embed):
    def __init__(self, pokemon: PokeObject):
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title='Evolution Stage Three', description='Stage three in the evolution of this pokemon')

class EvolutionInformation(View):
    
    def __init__(self, pages: [Embed]):
        super().__init__(timeout=600)
        self.pages = pages
        self.page_len = len(pages)
        
    
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
            # print('Disabling')
            self.nextButton.disabled = True
            self.prevButton.disabled = False
        else:
            self.prevButton.disabled = False
              
        
        await self.message.edit(embed=self.pages[self.curr_page], view=self)
    
class MovesInformation(View):
    
    def __init__(self, pages: [Embed]):
        super().__init__(timeout=600)
        self.pages = pages
        self.page_len = len(pages)
        
    
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
            # print('Disabling')
            self.nextButton.disabled = True
            self.prevButton.disabled = False
        else:
            self.prevButton.disabled = False
              
        
        await self.message.edit(embed=self.pages[self.curr_page], view=self)

class PokemonPage(dict):
    
    def __init__(self, pokemon: PokeObject):
        
        self['Pokedex Information'] = PokedexInformation([PokedexPageOne(pokemon), PokedexPageTwo(pokemon), PokedexPageThree(pokemon)])
        self['Evolution Information'] = EvolutionInformation([EvolutionPageOne(pokemon), EvolutionPageTwo(pokemon), EvolutionPageThree(pokemon)])
        self['Moves Information'] = MovesInformation([MovesPage(pokemon, 1)])

class PokemonSelect(Select):
    
        # Takes in the message and edits it based on the version selected.
    def __init__(self, pokemon: PokeObject, message: InteractionMessage) -> None:
        pokepage = PokemonPage(pokemon=pokemon)
        options = [SelectOption(label=v, value=v) for v in pokepage]
        super().__init__(min_values=1, max_values=1, options=options)
        self.pokemon = pokemon
        self.message = message
        self.options[0].default = True
        self.default_val = self.options[0]
    async def send(self):
        pokepage = None
        
        match self.options[0].value:
            case 'Pokedex Information':
                pokepage = PokedexInformation([PokedexPageOne(self.pokemon), PokedexPageTwo(self.pokemon), PokedexPageThree(self.pokemon)])
            case 'Evolution Information':
                pokepage = EvolutionInformation([EvolutionPageOne(self.pokemon), EvolutionPageTwo(self.pokemon), EvolutionPageThree(self.pokemon)])
            case 'Moves Information':
                pokepage = MovesInformation([MovesPage(self.pokemon, 1)])
        
        await pokepage.send(message=self.message, select=self)
            
    async def callback(self, interaction: Interaction):
        
        self.default_val.default = False
        
        pokepage = None
        match self.values[0]:
            case 'Pokedex Information':
                pokepage = PokedexInformation([PokedexPageOne(self.pokemon), PokedexPageTwo(self.pokemon), PokedexPageThree(self.pokemon)])
                self.options[0].default = True
                self.default_val = self.options[0]
            case 'Evolution Information':
                pokepage = EvolutionInformation([EvolutionPageOne(self.pokemon), EvolutionPageTwo(self.pokemon), EvolutionPageThree(self.pokemon)])
                self.options[1].default = True
                self.default_val = self.options[1]
            case 'Moves Information':
                pokepage = MovesInformation([MovesPage(self.pokemon, 1)])
                self.options[2].default = True
                self.default_val = self.options[2]
                
        await interaction.response.defer()
        await pokepage.send(message=self.message, select=self)
        
