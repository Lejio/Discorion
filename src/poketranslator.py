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
            return Bug
        case 'Dark':
            return Dark
        case 'Dragon':
            return Dragon
        case 'Electric':
            return Electric
        case 'Fairy':
            return Fairy
        case 'Fighting':
            return Fighting
        case 'Fire':
            return Fire
        case 'Flying':
            return Flying
        case 'Ghost':
            return Ghost
        case 'Grass':
            return Grass
        case 'Ground':
            return Ground
        case 'Ice':
            return Ice
        case 'Normal':
            return Normal
        case 'Poison':
            return Poison
        case 'Psychic':
            return Psychic
        case 'Rock':
            return Rock
        case 'Steel':
            return Steel
        case 'Water':
            return Water
        
