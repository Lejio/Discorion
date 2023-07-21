from discord import Embed
from discord.colour import Colour


class PokeCard(Embed):
    
    def __init__(self, font, color: Colour, pokemon: dict):
        
        self.colour = color
        
        