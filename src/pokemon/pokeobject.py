
class PokeObject:
    
    class PokemonEntry:
        
        def __init__(self, name, entries) -> None:
            
            self.name = name
            self.entries = entries
    
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
            self.catch_rate = training_data['Catch rate'] if training_data['Catch rate'] != '-' else None
            self.base_friendship = training_data['BaseFriendship'] if training_data['BaseFriendship'] != '-' else None
            self.base_xp = training_data['Base Exp.'] if training_data['Base Exp.'] != '-' else None
            self.growth_rate = training_data['Growth Rate']
        
        def __getBreedingData(self, breeding_data: dict):
            self.gender = breeding_data['Gender'].split(",")
            
        def __getBaseStats(self, base_stats: dict):
            
            self.stats = {}
            
            for s in base_stats:
                if s == 'Total':
                    self.stats[s] = base_stats[s]
                else:
                    self.stats[s] = self.Stat(
                        base=base_stats[s]["Base"],
                        max_=base_stats[s]["Max"],
                        min_=base_stats[s]["Min"]
                        )
        
        def __getDefenseStats(self, defense_stats):
            self.defense_stats = defense_stats


            

    def __init__(self, pokemon_raw: dict) -> None:
        
        
        self.name = pokemon_raw['name']
        self.versions = []
        
        try:
            self.versions.append(self.Version(self.name, pokemon_raw[self.name]))
        except KeyError:
            pass
        
        for alt_num in range(len(pokemon_raw['alt-version(s)'])):
            self.versions.append(self.Version(name=pokemon_raw['alt-version(s)'][alt_num], version=pokemon_raw[pokemon_raw['alt-version(s)'][alt_num]]))
            
        self.evolution_tree = pokemon_raw['evo_stats']
        
        self.attacks_data = pokemon_raw['attacks_data']
        
        self.pokedex_entries = []
        
        for e in pokemon_raw['entries']:
            self.pokedex_entries.append(self.PokemonEntry(e, pokemon_raw['entries'][e]))
            
        self.discord_image = pokemon_raw['discord_image']
        self.discord_sprite = pokemon_raw['discord_sprite']
        