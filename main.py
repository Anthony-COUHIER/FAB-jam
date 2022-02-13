#!/usr/bin/env python3.9

import sys
import pygame


def main():
    global event
    pygame.init()
    clock = pygame.time.Clock()

    size = 1920, 1080

    screen = pygame.display.set_mode(size)

    background = pygame.image.load('resources/background.png')

    background_pos_x = 0
    background_pos_y = 0

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
        parallaxe(screen, background, background_pos_x, background_pos_y)
        pygame.display.flip()


def parallaxe(window, image, position_x, bg_position_y):
    window.blit(image, (position_x, bg_position_y))


if __name__ == '__main__':
    main()
