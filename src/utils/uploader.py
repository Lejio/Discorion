'''


@client.tree.command(name="add-font-styles", description="Adds alphabet emojis automatically")
@commands.check_any(commands.is_owner())
async def addElectricEmojis(interaction: Interaction):

    channel = interaction.channel

    await interaction.response.send_message("Adding Emoji")
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for g in TypeGuilds:
        # print(g.value['name'])
        guild = client.get_guild(int(g.value['origin']))
        await channel.send(guild.name)
        for a in alphabet:
            
            path = f"./assets/pokefonts/{g.value['name']}/{g.value['name']}_{a}.png"
            with open(path, "rb") as image:
                f = image.read()
                b = bytes(f)
            
            c = f"{g.value['name'][0]}_{a}"
            print(c)
            
            emoji = await guild.create_custom_emoji(name=c, image=b)
            time.sleep(1.5)
            await channel.send(f'{a} = "<:{c}-{emoji.id}>"')
        await channel.send()
'''

'''

# Uploads sprites from the specified folder up into discord servers. This script runs for around 3 hours.

@client.tree.command(name="upload-sprites", description="Uploads sprites and images to both discord and cockroachdb")
@commands.check_any(commands.is_owner())
async def uploadSprites(interaction: Interaction):
    
    # ---------- Changes DiscordDatabase enum into a list ----------
    discord_db = list(DiscordDatabase)
    
    # ---------- Defines constant paths to both the json (where the pokemon info is stored) and sprites ----------
    JSON_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/pokedex/'
    SPRITES_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/'

    # ---------- Saves the channel from interaction to send a message for each emoji created. ----------
    channel = interaction.channel
    
    # ---------- Sends beginning message to avoid interaction not responded error ----------
    await interaction.response.send_message("Beginning upload.")

    # ---------- Guild number starts a one, and gradually increases as space runs out. ----------
    guild_num = 0
    guild = client.get_guild(discord_db[guild_num].value)
    
    # ---------- Loop that goes through the specified range of pokemons that needs to be uploaded. ----------
    for poke in range(50, 1011):
        
        # ---------- Checks guild if there is still space left (full - 50). ----------
        if len(guild.emojis) < 50:
                
            # ---------- Translates [current index].png image into bytes. ----------
            with open(SPRITES_DIR + str(poke) + ".png", "rb") as image:
                f = image.read()
                imageBytes = bytes(f)
                
            # ---------- Loads the pokemon json file related to the current index. ----------
            with open(JSON_DIR + str(poke) + ".json", "r") as file:
                data = json.load(file)
            
            # ---------- Runs async function that creates the emoij. ----------
            emoji = await guild.create_custom_emoji(name=f"P{poke}", image=imageBytes)
            
            # ---------- Sets/Creates new key in json that stores the created emojis id. ----------
            data['discord_sprite'] = f"<:P{poke}:{emoji.id}>"
            
            # ---------- Sends confirmation. ----------
            await channel.send(f'P{poke} - {data["discord_sprite"]}')
            
            # ---------- Saves the json changes. ----------
            with open(JSON_DIR + str(poke) + ".json", "w") as file:
                json.dump(data, file, indent=4)
            
                
        else:
            # ---------- Else runs when server is full. ----------
            
            # ---------- Increment the guild_num by one to move onto the next server listed in DiscordDatabase ----------
            guild_num += 1
            guild = client.get_guild(discord_db[guild_num].value)
            
            # ----------  Does the same thing as above ----------
            with open(SPRITES_DIR + str(poke) + ".png", "rb") as image:
                f = image.read()
                b = bytes(f)
                
            
            with open(JSON_DIR + str(poke) + ".json", "r") as file:
                data = json.load(file)
                
            emoji = await guild.create_custom_emoji(name=f"P{poke}", image=b)
            data['discord_sprite'] = f"<:P{poke}:{emoji.id}>"
            
            await channel.send(f'P{poke} - {data["discord_sprite"]}')
            
            with open(JSON_DIR + str(poke) + ".json", "w") as file:
                json.dump(data, file, indent=4)
            
            # ---------------------------------------------------
        
        # ----------  Sleeps the function so we do not get rate limited by discord api. ----------
        time.sleep(10)
''' 


'''

# Mean't to remove sprites, however it is currently broken. It seems like it might not be required in the future.

@client.tree.command(name="remove-sprites", description='removes all sprites')
@commands.check_any(commands.is_owner())
async def removeSprites(interaction: Interaction):
    
    await interaction.response.send_message("deleting emojis")
    discord_db = list(DiscordDatabase)
    guild_num = 0
    guild = client.get_guild(discord_db[guild_num].value)
    
    if len(guild.emojis) < 50:
        
        for i in range(0, 50):
            try:
                print(guild.emojis[i])
                emoji = await guild.delete_emoji(guild.emojis[i])
                time.sleep(1.5)
            except IndexError:
                pass
    

    else:
        guild_num += 1
        guild = client.get_guild(discord_db[guild_num].value) 
'''

'''

# Uploads official artwork and saves the link inside of the json info file.

@client.tree.command(name="upload-official-art", description="Uploads official art to discord and adds them to the json list.")
async def uploadSprites(interaction: Interaction):
    
    # ---------- Saves the channel so it could be used to send the image after interaction expires ---------- #
    channel = interaction.channel
    
    await interaction.response.send_message("Uploading images now.")
    
    # ---------- path to the official-artwork folder, all of them in the format of [pokedex-number].png. ----------
    path = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/sprites/pokemon/other/official-artwork/'
    JSON_DIR = '/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/pokedex/'
    
    # ---------- Loops through all the pokedex numbers (1 - 1010) ----------
    for i in range(1, 1010):
        print(str(i))
        message = await channel.send(file=File(path + str(i) + ".png"))
        
        # ---------- Saves the image url ----------
        image_url = message.attachments[0].url
        
        # ---------- Loads json file ----------
        with open(JSON_DIR + str(i) + ".json", "r") as file:
            data = json.load(file)
        
        # ---------- Create a new key and set the image url ----------
        data['discord_image'] = image_url
        
        # ---------- Saves the newly changed json back to its original file ----------
        with open(JSON_DIR + str(i) + ".json", "w") as file:
            json.dump(data, file, indent=4)
        
        # ---------- Sleep so we won't get rate limited by discord api (this should take ~24mins) ----------
        time.sleep(1.5)
'''