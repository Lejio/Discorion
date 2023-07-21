from discord import Colour

from poketypes.bug import Bug
from poketypes.dark import Dark
from poketypes.dragon import Dragon
from poketypes.electric import Electric
from poketypes.fairy import Fairy
from poketypes.fighting import Fighting
from poketypes.fire import Fire
from poketypes.flying import Flying
from poketypes.ghost import Ghost
from poketypes.grass import Grass
from poketypes.ground import Ground
from poketypes.ice import Ice
from poketypes.normal import Normal
from poketypes.poison import Poison
from poketypes.psychic import Psychic
from poketypes.rock import Rock
from poketypes.steel import Steel
from poketypes.water import Water

from poketools.pokemon.pokecalc import *

def StyleBundler():
    
    return {'Bug': Bug,
            'Dark': Dark,
            'Dragon': Dragon,
            'Electric': Electric,
            'Fairy': Fairy,
            'Fighting': Fighting,
            'Fire': Fire,
            'Flying': Flying,
            'Ghost': Ghost,
            'Grass': Grass,
            'Ground': Ground,
            'Ice': Ice, 
            'Normal': Normal, 
            'Poison': Poison, 
            'Psychic': Psychic, 
            'Rock': Rock,
            'Steel': Steel, 
            'Water': Water}

def PokeTranslator(style: str, text: str):
    return translateText(text_style=Style(style=style), text=text)

def Types():
    return [Bug, Dark, Dragon, Electric, Fairy, Fighting, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Steel, Water]

def Style(style: str):
    
    filteredStyle = style.lower().capitalize()
        
    match filteredStyle:
        case 'Bug':
            return [Bug, Colour.from_rgb(169, 187, 34)]
        case 'Dark':
            return [Dark, Colour.from_rgb(119, 84, 68)]
        case 'Dragon':
            return [Dragon, Colour.from_rgb(118, 102, 238)]
        case 'Electric':
            return [Electric, Colour.from_rgb(255, 204, 51)]
        case 'Fairy':
            return [Fairy, Colour.from_rgb(238, 153, 238)]
        case 'Fighting':
            return [Fighting, Colour.from_rgb(186, 85, 68)]
        case 'Fire':
            return [Fire, Colour.from_rgb(255, 68, 34)]
        case 'Flying':
            return [Flying, Colour.from_rgb(135, 153, 255)]
        case 'Ghost':
            return [Ghost, Colour.from_rgb(102, 102, 186)]
        case 'Grass':
            return [Grass, Colour.from_rgb(118, 204, 85)]
        case 'Ground':
            return [Ground, Colour.from_rgb(221, 187, 84)]
        case 'Ice':
            return [Ice, Colour.from_rgb(101, 204, 255)]
        case 'Normal':
            return [Normal, Colour.from_rgb(170, 170, 153)]
        case 'Poison':
            return [Poison, Colour.from_rgb(170, 85, 153)]
        case 'Psychic':
            return [Psychic, Colour.from_rgb(254, 84, 152)]
        case 'Rock':
            return [Rock, Colour.from_rgb(187, 170, 102)]
        case 'Steel':
            return [Steel, Colour.from_rgb(170, 170, 187)]
        case 'Water':
            return [Water, Colour.from_rgb(51, 153, 254)]
        
