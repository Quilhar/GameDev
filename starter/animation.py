import pygame
import math
import random

#Constant Variables
display_width = 1400
display_height = 1000

flake_speed = 50

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MOON = (246, 241, 213)
GREY = (182, 186, 183)
DARKGREEN = (31, 77, 35)
DARKISHYELLOW = (188, 194, 29)
LIGHTBLUE = (29, 186, 194)

# Create List
flakes = []

for i in range(4):
    loc = [random.randint(0, display_width), random.randint(0, display_height)]

    flakes.append(loc)
    


FPS = 60

# Game Setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([display_width, display_height])
clock = pygame.time.Clock()

playing = True

# Main Game Loop
while playing:

    # The Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing == False

    # Game Logic



    # Clear The Screen
    screen.fill(BLUE)


    # Draw Code Should Go Here
    for i in range(len(flakes)):
        pygame.draw.circle(screen, WHITE, flakes[i], 5)

        flakes[i][1] += flake_speed

        if flakes[i][1] > display_height:
            flakes[i] = [random.randint(0, display_width), random.randint(-20, -6)]


    # Update the Screen With New Drawings
    pygame.display.flip()

    # Limit to FPS
    clock.tick(FPS)
    


pygame.quit()