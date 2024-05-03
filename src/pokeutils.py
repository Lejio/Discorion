from discord import Colour
import math
from enum import Enum

from poketypes.default import Default
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

def StyleBundler():
    """Returns a dictionary pointing to the type classes.
    
    TypeClass contains the emojis, images and style bars for each type.

    Returns:
        dict(Enum): 'type_name': TypeClass(Enum)
    """
    
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
    """Uses translateText pokeutil function to translate text to emojis.

    Args:
        style (str): String name of the style (pokemon type).
        text (str): The text to translate.

    Returns:
        str : A string of character discord emojis that is the translated version of the text.
    """
    return translateText(text_style=Style(style=style)[0], text=text)

def Types():
    """Returns a list of all the type classes.

    Returns:
        list(Enum): List of all the type classes.
    """
    return [Bug, Dark, Dragon, Electric, Fairy, Fighting, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Steel, Water]

def Style(style: str):
    """Finds and returns the type class and colour of the style.

    Args:
        style (str): _description_

    Returns:
        list[TypeClass, Colour]: The type class and discord colour of the style.
    """
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
        

def calcBar(cur: int, max: int) -> int:
    """Calculates amount of bars full.

    Args:
        cur (int): Current stat number.
        max (int): Maximum stat number.

    Returns:
        int: How many bars are full (out of 10).
    """
    
    return math.floor(round(int((cur/max) * 100), 1) / 10)


def createBar(style: Enum, barLevel: int = 0):
    """Creates a bar emoji string depending on the bar level and style.\n
    The bar level is the amount of bars that are full. The bar goes from 0 to 10.

    Args:
        style (Enum): The style of the bar.
        barLevel (int, optional): Fill level of the bar. Goes from 0 - 10. Defaults to 0.

    Returns:
        str: String of bar emojis.
    """
    
    BAR_START_EMPTY = Default.BAR_START_EMPTY.value
    BAR_MIDDLE_EMPTY = Default.BAR_MIDDLE_EMPTY.value
    BAR_END_EMPTY = Default.BAR_END_EMPTY.value
            
    bar = ""
    
    if barLevel == 0:
        
        bar += BAR_START_EMPTY
        bar += 8*BAR_MIDDLE_EMPTY
        bar+= BAR_END_EMPTY
        
        return bar
    
    else:
        
        if barLevel - 1 == 0:
            bar += style.BAR_START_FILL_SPLIT.value
            bar += 8*BAR_MIDDLE_EMPTY
        elif barLevel == 10:
            bar += style.BAR_START_FILL.value
            bar += 8*style.BAR_MIDDLE_FILL.value
        else:
            bar += style.BAR_START_FILL.value
            fill = barLevel - 2
            bar += (fill)*style.BAR_MIDDLE_FILL.value
            bar += style.BAR_MIDDLE_FILL_SPLIT.value
            bar += (7 - fill)*BAR_MIDDLE_EMPTY
            
            
        if barLevel < 10:
            bar += BAR_END_EMPTY
        else:
            bar += style.BAR_END_FILL.value
    
    return bar
                
            
def createSeparator(num: int):
    """Creates a horizontal separator depending on the given size.

    Args:
        num (int): Size of separator.

    Returns:
        str: A string of separator emojis.
    """
    
    return num*f"{Default.SEPARATOR.value}"


def translateText(text_style, text) -> str:
    """Translates text into emojis.

    Args:
        text_style (_type_): The style to be translated into.
        text (_type_): The text to be translated.

    Returns:
        str: String of translated text emojis.
    """
        
    eWord = ""
    
    for char in text:
        
        try:
        
            if char == " ":
                
                eWord += Default.BLANK.value
                
            else:
                eWord += text_style[f'{char.upper()}'].value
        
        except KeyError:
            
            eWord += char
           
    return eWord