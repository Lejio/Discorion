
class Pokemon:
    
    class Stat:
        def __init__(self, base: int, min_: int, max_: int) -> None:
            self.base = base
            self.min = min_
            self.max = max_
            
    
    class Ability:
        def __init__(self, ability) -> None:
            self.effect = ability['effect']
            self.hidden = ability['hidden']
    
    
    class Version:
        
        def __init__(self, name: str, version: dict) -> None:
            
            self.version_name = name
            self.__getPokedexData(version['pokedex_data'])
        
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
            
            
            
    
    def __init__(self, pokemon_raw: dict) -> None:
        
        self.name = pokemon_raw['name']
        
        self.alt_versions = {}
        for alt_name in pokemon_raw['alt-version(s)']:
            self.alt_versions[alt_name] = pokemon_raw[alt_name]