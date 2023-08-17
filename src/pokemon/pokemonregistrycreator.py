import json

# POKEDEX_PATH = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/pokedex/'
POKEDEX_PATH = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/new_pokedex/'

if __name__ == "__main__":
    statsnotfound = []
    registry = {
        'name_based': {},
        'number_based': {}
    }


    for i in range(1, 1011):

        with open(POKEDEX_PATH + str(i) + ".json") as pokemon:
            p = json.load(pokemon)
            # try:
            #     p = json.load(pokemon)
            #     registry['name_based'][p['name']] = p[p['name']]['pokedex_data']['National No.']
            #     registry['number_based'][str(p[p['name']]['pokedex_data']['National No.'])] = p['name']
            # except KeyError:
            #     registry['name_based'][p['name']] = p[p['alt-version(s)'][0]]['pokedex_data']['National No.']
            #     registry['number_based'][str(p[p['alt-version(s)'][0]]['pokedex_data']['National No.'])] = p['name']
            
            versions: list = p['versions']
            # versions.append(p['name'])
            name: str = p['name']
            registry['name_based'][name]: dict = {
                'id': str(int(versions[0]['data']['pokedex_data']['National No.'])),
                'versions': []
            }
            registry['number_based'][str(int(versions[0]['data']['pokedex_data']['National No.']))]: dict = {
                'name': name,
                'versions': []
            }
            
            for v in versions:

                registry['name_based'][name]['versions'].append(v['name'])
                registry['number_based'][str(int(versions[0]['data']['pokedex_data']['National No.']))]['versions'].append(v['name'])
                # registry['name_based'][v] = p[v]['pokedex_data']['National No.']
                # registry['number_based'][p[v]['pokedex_data']['National No.']] = v
                
                

    with open('registry_v2.json', 'w') as reg:
        json.dump(registry, reg, indent=4)
            