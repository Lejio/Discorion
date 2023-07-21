from discorddatabase import DiscordDatabase
import json

def test():
    discord_db = list(DiscordDatabase)
    # JSON_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/pokedex/'
    JSON_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/test/'
    SPRITES_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/'
    guild_num = 0
    
    guild_emojis = 0
        
    for poke in range(1, 10):
        
        if guild_emojis < 50:
                
            # Need to add different versions in the future.
            with open(SPRITES_DIR + str(poke) + ".png", "rb") as image:
                f = image.read()
                b = bytes(f)
                img = SPRITES_DIR + str(poke) + ".png"
                
            
            with open(JSON_DIR + str(poke) + ".json", "r") as file:
                data = json.load(file)
                
            data['discord_sprite'] = f"<:{data['name']}:{img}>"
            
            
            with open(JSON_DIR + str(poke) + ".json", "w") as file:
                json.dump(data, file, indent=4)
            
            guild_emojis += 1
            
                
        else:
            guild_num += 1
            

test()
        