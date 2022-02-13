#!/usr/bin/env python3.9

from random import randrange
from Game import Game
import sys
import pygame

music = 'Sounds/bgm.mp3'
dice_sound = 'Sounds/DiceSource.mp3'
redbullcan_sound = 'Sounds/redbullcan_sound.mp3'
sucess_sound = 'Sounds/sucess_sound.mp3'

width, height = (200, 300)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)

texturing = []


def main():
    global event
    pygame.init()

    pygame.mixer.init()

    my_game = Game()

    my_game.create_players(4, ["resources/PNG/Pieces (Blue)/pieceBlue_single03.png",
                               "resources/PNG/Pieces (Red)/pieceRed_single03.png",
                               "resources/PNG/Pieces (Yellow)/pieceYellow_single03.png",
                               "resources/PNG/Pieces (Green)/pieceGreen_single03.png"])

    dice_roll_s = pygame.mixer.Sound(dice_sound)
    # open_can_s = pygame.mixer.Sound(redbullcan_sound)
    # sucess_s = pygame.mixer.Sound(sucess_sound)

    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    FONT = pygame.font.Font("resources/FreeSansBold.ttf", 50)
    clock = pygame.time.Clock()

    size = 1800, 1080

    screen = pygame.display.set_mode(size)

    background = pygame.image.load('resources/background.png')
    die = [
        pygame.image.load('resources/PNG/Dice/dieWhite1.png'),
        pygame.image.load('resources/PNG/Dice/dieWhite2.png'),
        pygame.image.load('resources/PNG/Dice/dieWhite3.png'),
        pygame.image.load('resources/PNG/Dice/dieWhite4.png'),
        pygame.image.load('resources/PNG/Dice/dieWhite5.png'),
        pygame.image.load('resources/PNG/Dice/dieWhite6.png')
    ]
    x_offset = 100
    y_offset = 150

    background_pos_x = 0
    background_pos_y = 0

    pressing = False
    button = pygame.Rect((1800 / 2) - 80, (1080 / 2) - 40, 64, 64)
    number = 1

    pygame.display.set_caption('FAB''s the game')

    for i in my_game.board.tiles:
        if i.path == "grass":
            texturing.append(pygame.image.load('resources/Tiles/grass_center_E.png'))
        if i.path == "corner1":
            texturing.append(pygame.image.load('resources/Tiles/grass_pathCorner_N.png'))
        if i.path == "corner3":
            texturing.append(pygame.image.load('resources/Tiles/grass_pathCorner_W.png'))
        if i.path == "corner4":
            texturing.append(pygame.image.load('resources/Tiles/grass_pathCorner_S.png'))
        if i.path == "corner2":
            texturing.append(pygame.image.load('resources/Tiles/grass_pathCorner_E.png'))
        if i.path == "line1":
            texturing.append(pygame.image.load('resources/Tiles/grass_path_E.png'))
        if i.path == "line2":
            texturing.append(pygame.image.load('resources/Tiles/grass_path_N.png'))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if background_pos_x > -1920:
                    background_pos_x -= 192
            if event.key == pygame.K_LEFT:
                if background_pos_x < 0:
                    background_pos_x += 192

        if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.MOUSEBUTTONUP):
            if event.button == 1:
                if button.collidepoint(event.pos):
                    if not pressing:
                        number = randrange(1, 7)
                        pygame.mixer.Sound.play(dice_roll_s)
                        pressing = True
                        my_game.play(number)
        else:
            pressing = False
        # pygame.draw.rect(screen, GRAY, button)
        # text_surf = FONT.render(str(number ), True, BLACK)
        # text_rect = text_surf.get_rect(center=(width/2, 30))
        # screen.blit(text_surf, text_rect)
        pygame.display.update()

        parallaxe(screen, background, background_pos_x, background_pos_y)

        for i in range(len(texturing)):
            parallaxe(screen, texturing[i], my_game.board.tiles[i].x, my_game.board.tiles[i].y)

        parallaxe(screen, die[number - 1], (1800 / 2) - 80, (1080 / 2) - 40)

        for i in range(4):
            parallaxe(screen, my_game.players[i].image, my_game.players[i].x + x_offset,
                      my_game.players[i].y + y_offset)

        pygame.display.flip()


def parallaxe(window, image, position_x, bg_position_y):
    window.blit(image, (position_x, bg_position_y))


if __name__ == '__main__':
    main()
