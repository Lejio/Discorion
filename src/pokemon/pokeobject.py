
class PokeObject:
    
    class PokemonEntry:
        
        def __init__(self, name, entries) -> None:
            
            self._name = name
            self._entries = entries
            
        @property
        def name(self) -> str:
            
            return self._name
        
        @property
        def entries(self) -> dict:
            
            return self._entries
        
    class Version:
        
        class Stat:
            def __init__(self, base: int, min_: int, max_: int) -> None:
                self._base = base
                self._min = min_
                self._max = max_
                
            @property
            def base(self):
                
                return self._base
            
            @property
            def minimum(self):
                
                return self._min
            
            @property
            def maximum(self):
                
                return self._max
            
        class Ability:
            def __init__(self, ability: dict) -> None:
                self.ability = ability
            
            @property
            def effect(self) -> str:
                
                return self.ability['effect']
            
            @property
            def hidden(self) -> bool:
                
                return self.ability['hidden']
                
            
        def __init__(self, name: str, version: dict) -> None:
            
            self.version_name = name
            self.__getPokedexData(version['pokedex_data'])
            self.__getTrainingData(version['training_data'])
            self.__getBreedingData(version['breeding_data'])
            self.__getBaseStats(version['base_stats'])
            self.__getDefenseStats(version['defense_stats'])
        
        def __getPokedexData(self, pokedex_data: dict):
            
            self._national_number = pokedex_data['National No.']
            self._type = pokedex_data['Type']
            self._species = pokedex_data['Species']
            self._height = pokedex_data['Height']
            self._weight = pokedex_data['Weight']
            self._abilities = {}
            for ability in pokedex_data['Abilities']:
                self._abilities[ability] = self.Ability(pokedex_data['Abilities'][ability])
                
        def __getTrainingData(self, training_data: dict):
            self._ev_yield = training_data['EV yield']
            self._catch_rate = training_data['Catch rate'] if training_data['Catch rate'] != '-' else None
            self._base_friendship = training_data['BaseFriendship'] if training_data['BaseFriendship'] != '-' else None
            self._base_xp = training_data['Base Exp.'] if training_data['Base Exp.'] != '-' else None
            self._growth_rate = training_data['Growth Rate']
        
        def __getBreedingData(self, breeding_data: dict):
            self._gender = breeding_data['Gender'].split(",")
            
        def __getBaseStats(self, base_stats: dict):
            
            self._stats = {}
            
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
            self._defense_stats = defense_stats

        @property
        def national_number(self):
            
            return self._national_number
        
        @property
        def pokemon_type(self):
            
            return self._type
        
        @property
        def species(self):
            
            return self._species
        
        @property
        def height(self):
            
            return self._height
        
        @property
        def weight(self):
            
            return self._weight
        
        @property
        def abilities(self):
            
            return self._abilities
        
        @property
        def ev_yield(self):
            
            return self._ev_yield
        
        @property
        def catch_rate(self):
            
            return self._catch_rate
        
        @property
        def base_friendship(self):
            
            return self._base_friendship
        
        @property
        def base_xp(self):
            
            return self._base_xp
        
        @property
        def growth_rate(self):
            
            return self._growth_rate

        @property
        def gender(self):
            
            return self._gender
        
        @property
        def stats(self):
            
            return self._stats
        
        @property
        def defense(self):
            
            return self._defense_stats




    def __init__(self, pokemon_raw: dict) -> None:
        
        
        self._name: str = pokemon_raw['name']
        self._versions: list = []
        
        for alt_num in pokemon_raw['versions']:
            self.versions.append(self.Version(name=alt_num['name'], version=alt_num['data']))
            
        self._evolution_tree: list = pokemon_raw['evo_stats']
        
        self._attacks_data: dict = pokemon_raw['attacks_data']
        
        self._pokedex_entries = []
        
        for e in pokemon_raw['entries']:
            self._pokedex_entries.append(self.PokemonEntry(e, pokemon_raw['entries'][e]))
            
        self._discord_image = pokemon_raw['discord_image']
        self._discord_sprite = pokemon_raw['discord_sprite']
        
    @property
    def evolution_tree(self):
        
        return self._evolution_tree
    
    @property
    def attacks(self):
        
        return self._attacks_data
    
    @property
    def pokedex_entries(self):
        
        return self._pokedex_entries
    
    @property
    def name(self):
        
        return self._name
    
    @property
    def versions(self):
        
        return self._versions
    
    @property
    def discord_image(self):
        
        return self._discord_image
    
    @property
    def discord_sprite(self):
        
        return self._discord_sprite