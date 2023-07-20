-- Step 1: Load the Aseprite file
app.open("path/to/your/input/file.aseprite")

-- Step 2: Get the active sprite
local sprite = app.activeSprite

-- Step 3: Define the new color (replace R, G, and B values with the desired color)
local newColor = Color{ r = 255, g = 0, b = 0, a = 255 }

-- Step 4: Loop through the pixels and fill the sprite with the new color
for y = 0, sprite.height - 1 do
    for x = 0, sprite.width - 1 do
        local pixelColor = sprite:getPixel(x, y)
        if pixelColor.a > 0 then
            sprite:setPixel(x, y, newColor)
        end
    end
end

-- Step 5: Save the modified sprite to a new file
app.command.SaveFileAs{ filename="path/to/your/output/file.aseprite" }
