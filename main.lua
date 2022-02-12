--[[
    Your love2d game start here
]]

local json = require("dkjson")
local helium = require 'helium'
local scene = helium.scene.new(true)
local input = require 'helium.core.input'
local useState = require 'helium.hooks.state'
local Dice = require("lovedice")
local useButton = require('helium.shell.button')
scene:activate()

step = 1
mapDec = {}

love.graphics.setDefaultFilter('nearest', 'nearest')

local useButton = require('helium.shell.button')

local d1 = 0
local d2 = 0

local elementCreator = helium(function(param, view)
	local buttonState = useButton()

	return function()
		if buttonState.down then
			love.graphics.setColor(1, 0, 0)
            d1 = Dice.roll()
            d2 = Dice.roll()
            love.audio.play(dicesource)
		else
			love.graphics.setColor(0, 1, 1)
		end
		love.graphics.print(param.text, 0, 0, 0, 2)
	end
end)

local element = elementCreator({text = 'roll dice'}, 100, 100)
element:draw(100, 100)
local source

function love.load()
    dicesource = love.audio.newSource("Sounds/DiceSource.mp3", "stream")

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
    scene:update(dt)
    love.keyboard.keysPressed = {}
end

function love.draw()
    scene:draw()
    if d1 > 0 then
        love.graphics.print("You rolled a " .. d1, 200, 200)
        love.graphics.print("And a " .. d2, 200, 220)
        love.graphics.print("That makes " .. d1 + d2, 200, 250)
    end
    if step == 0 then
        love.graphics.print('Welcome to the Love2d world!', 10, 10)
    else
        love.graphics.print('1', 10, 10)
    end
end

