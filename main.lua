--[[
    Your love2d game start here
]]

local json = require("dkjson")

step = 1
mapDec = {}

love.graphics.setDefaultFilter('nearest', 'nearest')

function love.load()
    love.window.setTitle('FAB')

    love.keyboard.keysPressed = {}

    mapJson = love.filesystem.read("dico.json")

    mapDec = json.decode(mapJson)

    for i, texture in ipairs(mapDec.categories) do
    		print(texture.name)
    		print("---")
    	end

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
    if step == 0 then
        love.graphics.print('Welcome to the Love2d world!', 10, 10)
    else
        love.graphics.print('1', 10, 10)
    end
end

