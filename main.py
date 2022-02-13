#!/usr/bin/env python3.9

from random import randrange
import sys
import pygame

music = 'Sounds/bgm.mp3'
dice_sound = 'Sounds/DiceSource.mp3'
redbullcan_sound = 'Sounds/redbullcan_sound.mp3'
sucess_sound = 'Sounds/sucess_sound.mp3'

width, height = (200,300)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)

def main():
    global event
    pygame.init()

    pygame.mixer.init()

    dice_roll_s = pygame.mixer.Sound(dice_sound)
    # open_can_s = pygame.mixer.Sound(redbullcan_sound)
    # sucess_s = pygame.mixer.Sound(sucess_sound)

    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

    FONT = pygame.font.Font("resources/FreeSansBold.ttf", 50)
    clock = pygame.time.Clock()

    size = 1920, 1080

    screen = pygame.display.set_mode(size)

    background = pygame.image.load('resources/background.png')
    die =   [
            pygame.image.load('resources/PNG/Dice/dieWhite1.png'),
            pygame.image.load('resources/PNG/Dice/dieWhite2.png'),
            pygame.image.load('resources/PNG/Dice/dieWhite3.png'),
            pygame.image.load('resources/PNG/Dice/dieWhite4.png'),
            pygame.image.load('resources/PNG/Dice/dieWhite5.png'),
            pygame.image.load('resources/PNG/Dice/dieWhite6.png')
            ]

    background_pos_x = 0
    background_pos_y = 0

    pressing = False
    button = pygame.Rect(400, 400, 64, 64)
    number = randrange(1, 7)

    pygame.display.set_caption('FAB''s the game')

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

            # Test sounds
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.Sound.play(dice_roll_s)

                        # This block is executed once for each MOUSEBUTTONDOWN event.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # `event.pos` is the mouse position.
                if button.collidepoint(event.pos):
                    # Increment the number.
                    if pressing == False:
                        number = randrange(1, 7)
                        pressing = True
        else:
            pressing = False
        # pygame.draw.rect(screen, GRAY, button)
        # text_surf = FONT.render(str(number ), True, BLACK)
        # text_rect = text_surf.get_rect(center=(width/2, 30))
        # screen.blit(text_surf, text_rect)
        screen.blit(die[number - 1], (400, 400))
        pygame.display.update()
        parallaxe(screen, background, background_pos_x, background_pos_y)
        pygame.display.flip()


def parallaxe(window, image, position_x, bg_position_y):
    window.blit(image, (position_x, bg_position_y))


if __name__ == '__main__':
    main()
