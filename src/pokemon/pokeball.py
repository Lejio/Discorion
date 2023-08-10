from enum import Enum
from pokemon.pokemon import Pokemon


class PokeballObject:
    
    def __init__(self, name: str, gen: int, index: int, catch_rate: float, effect: str) -> None:
        self.name = name
        self.gen = gen
        self.index = index
        self.catch_rate = catch_rate
        self.effect = effect

class PokeballEnum(Enum):
    
    POKEBALL = PokeballObject(name="Poke", gen=1, index=4, catch_rate=1, effect=None)
    GREATEBALL = PokeballObject(name="Great", gen=1, index=3, catch_rate=1.5, effect=None)
    ULTRABALL = PokeballObject(name="Ultra", gen=1, index=2, catch_rate=2, effect=None)
    MASTERBALL = PokeballObject(name="Master", gen=1, index=1, catch_rate=255, effect="Guaranteed capture.")
    SAFARIBALL = PokeballObject(name="Safari", gen=1, index=5, catch_rate=1, effect=None)
    FASTBALL = PokeballObject(name="Fast", gen=2, index=17, catch_rate=4, effect="Base speed must be at least 100, otherwise 1")
    LEVELBALL = PokeballObject(name="Level", gen=2, index=18, catch_rate=1, effect="1× if the player's Pokémon is the same level as or a lower level than the wild Pokémon 2× if the player's Pokémon is at a higher level than the wild Pokémon but less than double it 4× if the player's Pokémon is more than double but less than four times the level of the wild Pokémon 8× if the player's Pokémon is of a level four times or more than that of the wild Pokémon")
    LUREBALL = PokeballObject(name="Lure", gen=2, index=19, catch_rate=4, effect="If used on a Pokemon while fishing.")
    HEAVYBALL = PokeballObject(name="Heavy", gen=2, index=20, catch_rate=1, effect="-20 if used on a Pokémon weighing 220.2 lbs. (99.9 kg) or less ±0 if used on a Pokémon weighing 220.5 lbs. (100.0 kg) – 440.7 lbs. (199.9 kg) +20 if used on a Pokémon weighing 440.9 lbs. (200.0 kg) – 661.2 lbs. (299.9 kg) +30 if used on a Pokémon weighing 661.4 lbs. (300.0 kg) or more")
    LOVEBALL = PokeballObject(name="Love", gen=2, index=21, catch_rate=8, effect="8× if used on a Pokémon of the same species but opposite gender of the player's Pokémon 1× otherwise")
    FRIENDBALL = PokeballObject(name="Friend", gen=2, index=22, catch_rate=1, effect="Sets caught Pokemon's friendship to 150")
    MOONBALL = PokeballObject(name="Moon", gen=2, index=23, catch_rate=4, effect="4× if used on a Pokémon that belongs to an evolutionary family which includes a Pokémon that evolves by using a Moon Stone 1× otherwise")
    NETBALL = PokeballObject(name="Net", gen=3, index=6, catch_rate=3.5, effect="3.5× if used on a Water or Bug-type Pokémon 1× otherwise")
    DIVEBALL = PokeballObject(name="Dive", gen=3, index=7, catch_rate=3.5, effect="3.5× if used on a water-dwelling Pokémon 1× otherwise")
    NESTBALL = PokeballObject(name="Nest", gen=3, index=8, catch_rate=1, effect="((41 - Pokémon's level) ÷ 10)× if Pokémon's level is between 1 and 29 1× otherwise")
    REPEATBALL = PokeballObject(name="Repeat", gen=3, index=9, catch_rate=3.5, effect="3.5× if used on a Pokémon that is registered in the player's Pokédex as caught 1× otherwise")
    TIMERBALL = PokeballObject(name="Timer", gen=3, index=10, catch_rate=1, effect="(1 + number of turns passed in battle * 1229/4096)×, maximum 4× at 10 turns")
    LUXURYBALL = PokeballObject(name="Luxury", gen=3, index=11, catch_rate=1, effect="Doubles the rate at which the contained Pokémon's friendship increases.")
    DUSKBALL = PokeballObject(name="Dust", gen=4, index=13, catch_rate=3, effect="3× if used in a cave or at night 1× otherwise")    
    HEALBALL = PokeballObject(name="Heal", gen=4, index=14, catch_rate=1, effect="Fully restores a caught Pokémon's HP and PP and removes their status conditions.")
    QUICKBALL = PokeballObject(name="Quick", gen=4, index=15, catch_rate=5, effect="5× if used on the first turn of a battle 1× otherwise")
    DREAMBALL = PokeballObject(name="Dream", gen=5, index=25, catch_rate=4, effect="4× if used on a sleeping Pokémon 1× otherwise")
    BEASTBALL = PokeballObject(name="Beast", gen=6, index=26, catch_rate=5, effect="5× if used on an Ultra Beast 0.1× otherwise")



class Pokeball:
    
    def __init__(self, pokeball_type: PokeballEnum, pokemon: Pokemon) -> None:
        
        self.pokeball = pokeball_type
        self.pokemon = pokemon