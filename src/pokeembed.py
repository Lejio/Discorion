from discord import Embed
from poketranslator import translateText, Style
from poketools.pokemon.pokecalc import *
from pokemon.pokemon import Pokemon
from poketypes.default import Default

from random import Random

class PokeStats(Embed):
    
    def __init__(self, pokemon: Pokemon):
        # print(pokemon.versions[0].type[0])
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title='Search Result', description=f"{translateText(text_style=Style(pokemon.versions[0].type[0])[0], text=pokemon.name)}")
                
        self.set_thumbnail(url=pokemon.discord_image)
        
        version = pokemon.versions[0]
        style = Style(pokemon.versions[0].type[0])[0]
        
        # print("bruh", version[])
        
        self.add_field(name=f"{translateText(text_style=style, text='HP')} [100/180]", value=f"{createBar(calcBar(int(version.stats['HP'].base), int(version.stats['HP'].min)), style)}", inline=False)
        self.add_field(name=f"{translateText(text_style=style, text='Attack')} [55/103]", value=f"{createBar(calcBar(int(version.stats['Attack'].base), int(version.stats['Attack'].min)), style)}", inline=False)
        self.add_field(name=f"{translateText(text_style=style, text='Defense')} [40/79]", value=f"{createBar(calcBar(int(version.stats['Defense'].base), int(version.stats['Defense'].min)), style)}", inline=False)
        self.add_field(name=f"{translateText(text_style=style, text='Sp Atk')} [50/94]", value=f"{createBar(calcBar(int(version.stats['Sp. Atk'].base), int(version.stats['Sp. Atk'].min)), style)}", inline=False)
        self.add_field(name=f"{translateText(text_style=style, text='Sp Def')} [50/94]", value=f"{createBar(calcBar(int(version.stats['Sp. Def'].base), int(version.stats['Sp. Def'].min)), style)}", inline=False)
        self.add_field(name=f"{translateText(text_style=style, text='Speed')} [90/166]", value=f"{createBar(calcBar(int(version.stats['Speed'].base), int(version.stats['Speed'].min)), style)}", inline=False)


class PokeEmbed(Embed):
    
    def __init__(self, pokemon: Pokemon):
        super().__init__(colour=Style(pokemon.versions[0].type[0])[1], title='Search Result', description=f"{translateText(text_style=Style(pokemon.versions[0].type[0])[0], text=pokemon.name)}")
        # self.set_thumbnail(url='https://cdn.discordapp.com/attachments/1131758889575137330/1133936150042648606/240px-Pokemon_Steel_Type_Icon.png')
        
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
        