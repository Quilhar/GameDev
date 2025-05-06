import pygame as pygame
import math

#Constant Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)




FPS = 60

# Game Setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([700, 400])
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
    screen.fill(WHITE)


    # Draw Code Should Go Here

    # 1
    # pygame.draw.line(screen, BLACK, [20, 20], [300, 20], 2)
    # pygame.draw.polygon(screen, BLACK, [[75, 100], [225, 100], [150, 300]], 3)

    # offset = 0
    # for i in range(10):
    #     pygame.draw.line(screen, BLACK, [500, 50 + offset], [500, offset + 65], 2)
    #     offset += 25

    # 2
    # def drawRectangle(color, x1, y1, width, height):
    #     pygame.draw.rect(screen, color, [x1, y1, width, height])

    # drawRectangle(GREEN, 20, 20, 170, 120)
    # drawRectangle(RED, 200, 20, 170, 120)
    # drawRectangle(BLUE, 380, 20, 170, 120)

    # 3
    # pygame.draw.ellipse(screen, GREEN, [20, 20, 100, 100])
    # pygame.draw.ellipse(screen, RED, [20, 20, 100, 100], 2)
    # pygame.draw.ellipse(screen, GREEN, [150, 20, 200, 100])
    pygame.draw.rect(screen, GREEN, [400, 20, 150, 100])
    # pygame.draw.arc(screen, RED, [20, 150, 100, 100], 2*math.pi, 5.5*math.pi/4, 100)
    # pygame.draw.polygon(screen, GREEN, [[100, 325], [250, 150], [300, 165], [400, 325], [375, 350], [240, 250]])

    # 4
    # txt_font = pygame.font.SysFont('Helvetica', 8)
    # quest_4_txt = "Why you standing all by yourself?\nThose shoes were made for dancing with someone else\nWhy don't we move over to that empty space?\nI bet you 20 bucks I'll put a smile on your face\nI know a place where we can\n\nDance the night away\nBaby, we could try to\nMake the world spin slower\nWe could take our time and\nGet to know each other over cherry wine, huh"
    # title_text = quest_4_txt
    # title_img = txt_font.render(title_text, True, BLACK)
    

    # screen.blit(title_img, (50, 50))

    # Update the Screen With New Drawings
    pygame.display.flip()

    # Limit to FPS
    clock.tick(FPS)
    


pygame.quit()