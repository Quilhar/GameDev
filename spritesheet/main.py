from settings import *
from sprites import *
import pygame
import random


def game_play():
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Game Title")

    clock = pygame.time.Clock()
    playing = True

    explosion_sheet = SpriteSheet('./spritesheet/explosion.png')
    explosion_list = []

    for y in range(5):
        for x in range(5):
            locx = 64 * x
            locy = 64 * y 


            image = explosion_sheet.get_image(locx, locy, 64, 64)

            image.set_colorkey(BLACK)

            explosion_list.append(image)
    print(explosion_list[0])

    while playing:
        for event in pygame.event.get():
            #Events to end the game
            if event.type == pygame.QUIT:
                playing = False

        screen.fill(BG_COLOR)

        screen.blit(explosion_list[0], (100, 100))

        pygame.display.flip()

game_play()