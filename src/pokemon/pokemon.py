
class Pokemon:
    
    class PokemonEntry:
        
        def __init__(self, name, entries) -> None:
            
            self.name = name
            self.entries = entries
    
    class Moves:
        
        class Move:
            
            def __init__(self, name: str, level: int) -> None:
                self.name = name
                self.level = level
        
        def __init__(self, reg_moves: dict) -> None:
            
            self.moves = {}
            
            for move in reg_moves:
                self.moves[move] = self.Move(move, reg_moves[move])
        
    class EggMoves:
        def __init__(self, egg_moves: dict) -> None:
            self.moves = {}
            for move in egg_moves:
                self.moves[move]
        
    class TMMoves:
        
        class Move:
            def __init__(self, name, number: int) -> None:
                self.name = name
                self.tm_number = number
        
        def __init__(self, tm_moves: dict) -> None:
            self.moves = {}
            for move in tm_moves:
                self.moves[move] = self.Move(move, str(tm_moves[move]))
    
    class Version:
        
        class Stat:
            def __init__(self, base: int, min_: int, max_: int) -> None:
                self.base = base
                self.min = min_
                self.max = max_
            
        class Ability:
            def __init__(self, ability: dict) -> None:
                self.effect = ability['effect']
                self.hidden = ability['hidden']
        
        def __init__(self, name: str, version: dict) -> None:
            
            self.version_name = name
            self.__getPokedexData(version['pokedex_data'])
            self.__getTrainingData(version['training_data'])
            self.__getBreedingData(version['breeding_data'])
            self.__getBaseStats(version['base_stats'])
            self.__getDefenseStats(version['defense_stats'])
        
        def __getPokedexData(self, pokedex_data: dict):
            
            self.national_number = pokedex_data['National No.']
            self.type = pokedex_data['Type']
            self.species = pokedex_data['Species']
            self.height = pokedex_data['Height']
            self.weight = pokedex_data['Weight']
            self.abilities = {}
            for ab in pokedex_data['Abilities']:
                self.abilities[ab] = self.Ability(pokedex_data['Abilities'][ab])
                
        def __getTrainingData(self, training_data: dict):
            self.ev_yield = training_data['EV yield']
            self.catch_rate = int(training_data['Catch rate'])
            self.base_friendship = int(training_data['BaseFriendship'])
            self.base_xp = int(training_data['Base Exp.'])
            self.growth_rate = training_data['Medium Fast']
        
        def __getBreedingData(self, breeding_data: dict):
            self.gender = breeding_data['Gender'].split(",")
            
        def __getBaseStats(self, base_stats: dict):
            
            self.stats = {}
            
            for s in base_stats:
                self.stats[s] = self.Stat(
                    base=base_stats[s]["Base"],
                    max_=base_stats[s]["Max"],
                    min_=base_stats[s]["Min"]
                    )
        
        def __getDefenseStats(self, defense_stats):
            self.defense_stats = defense_stats


            

    def __init__(self, pokemon_raw: dict) -> None:
        
        self.name = pokemon_raw['name']
        
        self.alt_versions = {}
        for alt_name in pokemon_raw['alt-version(s)']:
            self.alt_versions[alt_name] = self.Version(pokemon_raw[alt_name])
            
        self.evolution_tree = pokemon_raw['evo_stats']
        self.attacks_data = {
            self.Moves(pokemon_raw['attacks_data']['moves']),
            self.EggMoves(pokemon_raw['attacks_data']['egg']),
            self.TMMoves(pokemon_raw['attacks_data']['tm'])
            }
        
        self.pokedex_entries = {}
        
        for e in pokemon_raw['entries']:
            self.pokedex_entries[e] = self.PokemonEntries(e, pokemon_raw['entries'][e])
            
        self.discord_image = pokemon_raw['discord_image']
        self.discord_sprite = pokemon_raw['discord_sprite']
        