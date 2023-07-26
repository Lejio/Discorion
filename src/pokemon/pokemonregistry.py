import json
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, Table, insert, MetaData, update, inspect

load_dotenv(dotenv_path='/Users/geneni/Developer/Workspace/Projects/Discoreon/.env')
POKEDEX_PATH = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/pokedex/'

class PokeCreateRegistry:
    
    def __init__(self, database_url) -> None:
        
        self.__engine = create_engine(database_url)
        self.__conn = self.__engine.connect()
        self.__metadata = MetaData()
        self.__table = {}
    
    def table(self, name: str, *args: Column):
        if inspect(self.__engine).has_table(name):
            self.__table[name] = self.getTable(name=name)
        else:
            self.__metadata = MetaData()
            self.__table[name] = Table(name, self.__metadata, *(arg for arg in args ))
            self.__metadata.create_all(self.__engine, checkfirst=True)
            
    def commit(self):
        self.__conn.commit()
        
    def close(self):
        self.__conn.close()


statsnotfound = []
registry = {
    'name_based': {},
    'number_based': {}
}


for i in range(1, 1011):

    with open(POKEDEX_PATH + str(i) + ".json") as pokemon:
        try:
            p = json.load(pokemon)
            print(p['name'], p[p['name']]['pokedex_data']['National No.'])
            registry['name_based'][p['name']] = p[p['name']]['pokedex_data']['National No.']
            registry['number_based'][str(p[p['name']]['pokedex_data']['National No.'])] = p['name']
        except KeyError:
            print(p['name'], p[p['alt-version(s)'][0]]['pokedex_data']['National No.'])
            registry['name_based'][p['name']] = p[p['alt-version(s)'][0]]['pokedex_data']['National No.']
            registry['number_based'][str(p[p['alt-version(s)'][0]]['pokedex_data']['National No.'])] = p['name']
            

with open('registry.json', 'w') as reg:
    json.dump(registry, reg, indent=4)
            