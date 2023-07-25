from discord import Embed
from discord.colour import Colour
from poketranslator import translateText, Style
from poketools.pokemon.pokecalc import *


class PokeCard(Embed):
    
    def __init__(self, font, color: Colour, pokemon: dict):
        
        self.colour = color
        
        self.set_thumbnail(url="https://cdn.discordapp.com/attachments/1125937900421398552/1125938114247016548/pikachu-removebg-preview.png")
        
        self.add_field(name="Level", value=f"5", inline=False)
        
        self.add_field(name=f"100 {translateText(text_style=Style('electric')[0], text='HP')} 180", value=f"{createBar(calcBar(100, 180))}", inline=False)
        self.add_field(name=f"55 {translateText(text_style=Style('electric')[0], text='Attack')} 103", value=f"{createBar(calcBar(55, 103))}", inline=False)
        self.add_field(name=f"40 {translateText(text_style=Style('electric')[0], text='Defense')} 79", value=f"{createBar(calcBar(40, 79))}", inline=False)
        self.add_field(name=f"50 {translateText(text_style=Style('electric')[0], text='Sp Atk')} 94", value=f"{createBar(calcBar(50, 94))}", inline=False)
        self.add_field(name=f"50 {translateText(text_style=Style('electric')[0], text='Sp Def')} 94", value=f"{createBar(calcBar(50, 94))}", inline=False)
        self.add_field(name=f"90 {translateText(text_style=Style('electric')[0], text='Speed')} 166", value=f"{createBar(calcBar(90, 166))}", inline=False)