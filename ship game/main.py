import pygame as pg
import math
import random



#Constant Variables
width = 1400
height = 1000

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
ORANGE = (255, 165, 0)
OFFGRAY = (102, 86, 86)
BRICK = (188, 74, 60)

#Game screens
def game_start():
    FPS = 60
    pg.init()
    pg.font.init()

    screen = pg.display.set_mode([width, height])
    clock = pg.time.Clock()

    playing = True

    pg.mouse.set_visible(False)


    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    playing = False
      

    ####
        screen.fill(BLACK)

        font = pg.font.SysFont('Calibri', 50, True, False)
        start_txt = 'Press Enter to Start the Game'
        title_img = font.render(start_txt, True, WHITE)
        screen.blit(title_img, [425,450])
        
    ####
    # Update the Screen With New Drawings
        pg.display.flip()

    # Limit to FPS
        clock.tick(FPS)
def game_over(game_score):
    FPS = 60
    pg.init()
    pg.font.init()

    screen = pg.display.set_mode([width, height])
    clock = pg.time.Clock()

    playing = True

    pg.mouse.set_visible(False)

    high_score = 0
    if game_score > high_score:
        high_score = game_score

    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
                game_start()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    playing = False

    ####
        screen.fill(BLACK)

        font = pg.font.SysFont('Calibri', 50, True, False)

        score_txt = f'You got {game_score}pts'
        high_score_txt = f'High Score = {high_score}pts'
        play_again_txt = 'Press Enter to Play Again'

        score_img = font.render(score_txt, True, WHITE)
        high_score_img = font.render(high_score_txt, True, WHITE)
        play_again_img = font.render(play_again_txt, True, WHITE)

        screen.blit(score_img, [550,350])
        screen.blit(high_score_img, [500,450])
        screen.blit(play_again_img, [425,550])
        
    ####
    # Update the Screen With New Drawings
        pg.display.flip()

    # Limit to FPS
        clock.tick(FPS)
def game_play():

    #Speed and initial location for the ship
    ship_x_speed = 0
    ship_y_speed = 0

    ship_x_loc = 100
    ship_y_loc = height - 145

    # Window Variables
    win_color_list = [DARKISHYELLOW, WHITE]

    random_win_color = win_color_list[random.randint(0, 1)]

    # Star Variables
    stars = []

    for i in range(100):
        offset_x = random.randint(0, width)
        offset_y = random.randint(0, height)
        stars.append([offset_x, offset_y])

    #Meteor Variables
    meteor_lines = [[(0, 20), (250, 35)], [(150, 50), (400, 65)], [(100, 65), (350, 80)], [(50, 80), (400, 95)], [(120, 105), (350, 120)]]

    meteor_speed = 15

    #Moon Shadow Variables
    shadow_speed = 1
    shadow_pos = 275

    count = 100

    ##Spaceship
    var_body_width = 70

    var_body_height= 25

    var_win_width = 50

    var_win_height = 20

    ship_height = var_body_height + var_win_height

    def draw_ship(x, y, body_width, body_height, win_width, win_height, top_col, bot_col):
    
        #Ship top
        pg.draw.ellipse(screen, top_col, [x + (body_width - win_width) // 2, y - win_height, win_width, win_height + 20])


        #Ship bot
        pg.draw.ellipse(screen, bot_col, [x, y, body_width, body_height])

    ##### Bullet
    b_xloc = None
    b_yloc = None
    b_speed = 0 
    bullets = []

    def draw_bullet(player_x, player_y):
        
        pg.draw.arc(screen, WHITE, [(player_x + var_body_width/2) - 5, player_y + 10, 10, 10], 0, math.pi)

        b_xcollision = (player_x + var_body_width/2) - 5
        b_ycollision = player_y + 10

        return b_xcollision, b_ycollision


    ##Buildings 
    def drawBuilding(color, x1, y1, width, height, window_color, cols, rows):

        #Main
        pg.draw.rect(screen, color, [x1, y1, width, height])

        #Windows
        winx_offset = 35

        winy_offset = 25

        
        for row in range(rows):
            for col in range(cols):

                pg.draw.rect(screen, window_color, [x1 + winx_offset, y1 + winy_offset, width/4, width/4], )
            
                winx_offset += 75

            winx_offset -= 150
            winy_offset += 100

    #Lasers
    laser_speed = 10
    lasers = []
    score = 0 
    for i in range(4):
        loc = [random.randint(0, width), -20]

        lasers.append(loc)

    def dodge():

        

        for i in range(len(lasers)):
    
            pg.draw.rect(screen, RED, [lasers[i][0], lasers[i][1], 10, 20], 5)

            lasers[i][1] += laser_speed
           



        if lasers[0][1] > height:
            lasers[0] = [random.randint(0, width), random.randint(-20, -6)]

            score += 1

        return score

    #Collion Vars 
    laser_hitbox_x = lasers[0][0]
    FPS = 60
    pg.init()
    pg.font.init()

    screen = pg.display.set_mode([width, height])
    clock = pg.time.Clock()

    playing = True

    pg.mouse.set_visible(False)

    # Main Game Loop
    while playing:

        # The Event Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    ship_x_speed = -10
                elif event.key == pg.K_d:
                    ship_x_speed = 10
                elif event.key == pg.K_s:
                    ship_y_speed = 10
                elif event.key == pg.K_w:
                    ship_y_speed = -10
                elif event.key == pg.K_RETURN:
                    playing = False
                
                if event.key == pg.K_SPACE:
                    b_speed = -3
                    b_xloc = ship_x_loc
                    b_yloc = ship_y_loc
                    bullets.append([b_xloc, b_yloc])

            elif event.type == pg.KEYUP:
                if event.key == pg.K_a or event.key == pg.K_d:
                    ship_x_speed = 0
                elif event.key == pg.K_w or event.key == pg.K_s:
                    ship_y_speed = 0
        
        # mouse_pos = pg.mouse.get_pos()

        ship_x_loc += ship_x_speed
        ship_y_loc += ship_y_speed

        if ship_x_loc <= 0:
            ship_x_loc = 0
        elif ship_x_loc >= width - var_body_width:  
            ship_x_loc = width - var_body_width

        if ship_y_loc <= 0:
            ship_y_loc = 0
        elif ship_y_loc >= height - ship_height:
            ship_y_loc = height - ship_height

    # Game Logic

        # Clear The Screen
        screen.fill(BLACK)

    # Draw Code Should Go Here

        ## Stars

        for star in stars:
            pg.draw.ellipse(screen, WHITE, [0 + star[0], 0 + star[1], 5, 5])

        ##Buildings
        drawBuilding(BRICK, 20, height/2, 200, height/2, DARKISHYELLOW, 2, 8)
        drawBuilding(BRICK, 350, 400, 200, 600, DARKISHYELLOW, 2, 8)
        drawBuilding(BRICK, 550, 600, 200, 400, DARKISHYELLOW, 2, 8)
        drawBuilding(BRICK, 850, 450, 200, 650, DARKISHYELLOW, 2, 8)
        drawBuilding(BRICK, 1050, 650, 200, 250, DARKISHYELLOW, 2, 8)

        ##Ground 
        pg.draw.rect(screen, DARKGREEN, [0, 900, 1400, 100])


        ##Meteor Shower
        for meteor_line in meteor_lines:
            
            start = list(meteor_line[0])
            end = list(meteor_line[1])

            

            start[0] += meteor_speed
            end[0] += meteor_speed



            meteor_line[0] = tuple(start)
            meteor_line[1] = tuple(end)

            pg.draw.line(screen, WHITE, start, end, 5)

            if meteor_line[0][0] > width:
                meteor_line[0] = (-250, meteor_line[0][1])
                meteor_line[1] = (0, meteor_line[1][1])

        ## Moon
        if shadow_pos >= 375:
            shadow_speed = -1
        if shadow_pos < 275:
            shadow_speed = 1

        pg.draw.ellipse(screen, MOON, [275, 75, 100, 100])
        pg.draw.ellipse(screen, BLACK, [shadow_pos, 75, 100, 100])
        shadow_pos += shadow_speed
            
        ## Ship

        if bullets:
            for bullet in bullets:
                bullet[1] += b_speed
                draw_bullet(bullet[0], bullet[1])

        # bullet_collision_list = []
        # bullet_collision_list.append(draw_bullet(ship_x_loc, ship_y_loc))
        draw_ship(ship_x_loc, ship_y_loc, var_body_width, var_body_height, var_win_width, var_win_height, OFFGRAY, BLUE)
        
        ## Laser
        dodge()

        ## Collision
        if lasers[0][1] + 5 >= ship_y_loc and lasers[0][1] + 5 <= ship_y_loc and laser_hitbox_x >= ship_x_loc and laser_hitbox_x <= ship_x_loc + var_body_width:
            game_over(game_score)
    
    
        elif lasers[0][1] + 5 >= ship_y_loc and lasers[0][1] + 5 <= ship_y_loc and laser_hitbox_x + 5 >= ship_x_loc and laser_hitbox_x + 5 <= ship_x_loc + var_body_width:
            game_over(game_score)
        
    # Update the Screen With New Drawings
        pg.display.flip()

    # Limit to FPS
        clock.tick(FPS)

    final_score = dodge()
    return final_score

game_start()

playing = True

while playing:
    game_score = game_play()
    playing = game_over(game_score)

pg.quit()



