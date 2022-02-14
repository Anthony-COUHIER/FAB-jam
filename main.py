#!/usr/bin/env python3.9

from random import randrange
from Game import Game
import sys
import pygame

from common import parallaxe, draw_text

music = 'Sounds/bgm.mp3'
game_music = 'Sounds/game_bgm.mp3'
dice_sound = 'Sounds/DiceSource.mp3'
redbullcan_sound = 'Sounds/redbullcan_sound.mp3'
sucess_sound = 'Sounds/sucess_sound.mp3'

width, height = (200, 300)

texturing = []


def main():
    global event
    pygame.init()
    open_menu = 1

    pygame.mixer.init()

    my_game = Game()

    my_game.create_players(4, ["resources/PNG/Pieces (Blue)/pieceBlue_single01.png",
                               "resources/PNG/Pieces (Red)/pieceRed_single03.png",
                               "resources/PNG/Pieces (Yellow)/pieceYellow_single02.png",
                               "resources/PNG/Pieces (Green)/pieceGreen_single02.png"])
    gorilla = pygame.image.load('resources/gorilla.png')

    dice_roll_s = pygame.mixer.Sound(dice_sound)

    size = 1800, 1080
    profiles = [pygame.image.load('resources/profil_blue.png'), pygame.image.load('resources/profil_red.png'),
                pygame.image.load('resources/profil_green.png'), pygame.image.load('resources/profil_yellow.png')]
    profiles_positions = [[0, 0], [size[0] - 450, 0], [0, size[1] - 100], [size[0] - 450, size[1] - 100]]

    # sucess_s = pygame.mixer.Sound(sucess_sound)

    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    FONT = pygame.font.Font("resources/FreeSansBold.ttf", 18)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    background = pygame.image.load('resources/back.png')
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
    button_open = pygame.Rect(600, 540, 600, 100)
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

    while open_menu == 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.MOUSEBUTTONUP):
                if event.button == 1:
                    if button_open.collidepoint(event.pos):
                        if not pressing:
                            open_menu = 0
                            pressing = True
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(game_music)
                            pygame.mixer.music.play(-1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                open_menu = 0
                pressing = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load(game_music)
                pygame.mixer.music.play(-1)
            else:
                pressing = False

        pygame.display.update()

        parallaxe(screen, background, 0, 0)
        parallaxe(screen, gorilla, size[0] / 2 - 305, size[1] / 2 + 100)

        pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if background_pos_x > -1920:
                        background_pos_x -= 192
                if event.key == pygame.K_LEFT:
                    if background_pos_x < 0:
                        background_pos_x += 192

            if (event.type == pygame.MOUSEBUTTONDOWN):
                if event.button == 1:
                    if button.collidepoint(event.pos):
                        if not pressing:
                            number = randrange(1, 7)
                            pygame.mixer.Sound.play(dice_roll_s)
                            pressing = True
                            my_game.play(number, screen, FONT)
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
            parallaxe(screen, my_game.players[i].image, my_game.players[i].x + x_offset + 5 * (i - 2),
                      my_game.players[i].y + y_offset + 5 * (i - 2))

        for i in range(4):
            x = 50
            y = 20
            if (i == 1 or i == 3):
                x = size[0] - 300
            if (i == 2 or i == 3):
                y = size[1] - 80
            parallaxe(screen, profiles[i], profiles_positions[i][0], profiles_positions[i][1])
            draw_text(str(my_game.players[i].skills.love), x, y, screen, FONT)
            draw_text(str(my_game.players[i].skills.luck), x + 120, y, screen, FONT)
            draw_text(str(my_game.players[i].skills.money), x + 240, y, screen, FONT)
            draw_text(str(my_game.players[i].skills.education), x, y + 40, screen, FONT)
            draw_text(str(my_game.players[i].skills.health), x + 120, y + 40, screen, FONT)
            draw_text(str(my_game.players[i].skills.illegal), x + 240, y + 40, screen, FONT)

        pygame.display.flip()


if __name__ == '__main__':
    main()
