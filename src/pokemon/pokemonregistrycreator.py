import json

POKEDEX_PATH = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/pokedex/'

if __name__ == "__main__":
    statsnotfound = []
    registry = {
        'name_based': {},
        'number_based': {}
    }


    for i in range(1, 1011):

        with open(POKEDEX_PATH + str(i) + ".json") as pokemon:
            try:
                p = json.load(pokemon)
                # print(p['name'], p[p['name']]['pokedex_data']['National No.'])
                registry['name_based'][p['name']] = p[p['name']]['pokedex_data']['National No.']
                registry['number_based'][str(p[p['name']]['pokedex_data']['National No.'])] = p['name']
            except KeyError:
                # print(p['name'], p[p['alt-version(s)'][0]]['pokedex_data']['National No.'])
                registry['name_based'][p['name']] = p[p['alt-version(s)'][0]]['pokedex_data']['National No.']
                registry['number_based'][str(p[p['alt-version(s)'][0]]['pokedex_data']['National No.'])] = p['name']
                

    with open('registry.json', 'w') as reg:
        json.dump(registry, reg, indent=4)
            