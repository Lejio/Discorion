import csv
import json

from poketools.pokequery import PokeQuery

if __name__ == "__main__":
    
    SPRITES_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/'
    IMAGE_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/other/official-artwork/'
    registry = json.load(open('./pokemon/registry_v2.json'))
    
    with open('pokemon_forms_1_clean.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            current_number = list(row)[0]
            try:
                int(current_number)
            except ValueError:
                continue
            queryEngine = PokeQuery(pokemon_object=registry['name_based'])
            result_list = queryEngine.query(user_input=row[1])
            sprite_number = result_list[1]['id']
            # print(sprite_number)
            print(row)
            
            try:
                with open(f'{SPRITES_DIR}{current_number}.png') as sprite:
                    # print('Sprite: ' + current_number + " " + row[1] + " " + row[2])
                    pass
                    
                with open(f'{IMAGE_DIR}{current_number}.png') as image:
                    # print('Image: ' + current_number)
                    pass
                
            except FileNotFoundError:
                print('Not found: ' + current_number)
            
            print()
    # with open('extra_sprites.json', 'r') as extra_sprites:
        
    #     sprites_list = json.load(extra_sprites)
        
    # print(len(sprites_list))
        
        