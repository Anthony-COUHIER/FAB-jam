
local json = require("dkjson")

step = 1
mapDec = {}
local points = {0, 0, 0, 0, 0, 0, 0}
local categories = {"Amour", "Education", "Chance", "Santé", "Argent", "Illégalité", "Apparence"}

local first_display
local second_display
local answer = 0

love.graphics.setDefaultFilter('nearest', 'nearest')

function get_question()

end

function love.load()
    love.window.setTitle('FAB')

    love.keyboard.keysPressed = {}

    mapJson = love.filesystem.read("dico.json")

    mapDec = json.decode(mapJson)

    print(categories[1])

end

function love.resize(w, h)
    -- ...
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    end

    love.keyboard.keysPressed[key] = true
end

function love.keyboard.wasPressed(key)
    return love.keyboard.keysPressed[key]
end

function love.update(dt)
    -- change some values based on your actions

    love.keyboard.keysPressed = {}
end

function love.draw()

end

