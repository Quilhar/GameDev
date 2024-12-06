from settings import *
import components as comps
import pygame



################################################################################

# LAYOUTS[level_count]
# current_level

def loading_level(level_count):
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Game Title")

    clock = pygame.time.Clock()

    block_img = pygame.image.load('platformer/images/block.png')
    front_img = pygame.image.load('platformer/images/front.png')
    slime_img = pygame.image.load('platformer/images/slime_normal.png')
    ground_img = pygame.image.load('platformer/images/ground.png')
    switch_on_img = pygame.image.load('platformer/images/switch_green_on.png')
    switch_off_img = pygame.image.load('platformer/images/switch_red_on.png')
    door_img = pygame.image.load('platformer/images/lock_red.png')
    spike_img = pygame.image.load('platformer/images/spikes.png')


    brick_list = []
    enemy_list = []
    barrier_list = []
    ground_list = []
    spike_list = []
    door_list = []

    current_level = LAYOUTS[level_count]

    for row in range(len(current_level[0])):
        y_loc = row * BRICK_HEIGHT

        for col in range(len(current_level[0][1])):
            x_loc = col * BRICK_WIDTH

            if current_level[row][col] == "1":
                brick = comps.Brick(x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT, BRICK, screen, block_img)

                brick_list.append(brick)        

            elif current_level[row][col] == "p":
                player = comps.Player(x_loc, y_loc + 20, PLAYER_WIDTH, PLAYER_HEIGHT, BLUE, screen, front_img)
                
            
            elif current_level[row][col] == "e":
                enemy = comps.Enemy(x_loc, y_loc + 20, ENEMY_WIDTH, ENEMY_HEIGHT, RED, screen, slime_img)

                enemy_list.append(enemy)

            

            elif current_level[row][col] == "b":
                barrier = comps.Barrier(x_loc, y_loc, BARRIER_WIDTH, BARRIER_HEIGHT, BG_COLOR, screen)

                barrier_list.append(barrier)

                

            elif current_level[row][col] == "g":
                ground = comps.Ground(x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT, BRICK, screen, ground_img)

                ground_list.append(ground)
                
                
            
            elif current_level[row][col] == "d":
                door = comps.Door(x_loc, y_loc - (BRICK_HEIGHT * .5), BRICK_WIDTH, BRICK_HEIGHT * 1.5, BRICK, screen, door_img)

                door_list.append(door)

                
            elif current_level[row][col] == "s":
                spike = comps.Spike(x_loc + 5, y_loc + (BRICK_HEIGHT/2), BRICK_WIDTH - 10, BRICK_HEIGHT/2, BRICK, screen, spike_img)

                spike_list.append(spike)

    #######################################################################
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            playing = False
                
    screen.fill(BG_COLOR)

    #####################################################################
    # Invis barrier
    for barrier in barrier_list:

        barrier.draw_barrier()


    # Enemy
    for mob in enemy_list:
        mob.enemy_update(brick_list, barrier_list)
        mob.draw_enemy()


    # Platforms
    for block in brick_list:
        block.draw_brick()

    for ground in ground_list:
        ground.draw_ground()
    

    # Obstacles
    for spike in spike_list:
        spike.draw_spike()

    # Player
    player.update(brick_list, enemy_list, ground_list, spike_list, door_list)
    player.draw()
    

    #######################################################################
    pygame.display.flip()

    clock.tick(FPS)

    # return player
#####################################################


# loading_level(0)

playing = True

while playing: 
    loading_level(1)

pygame.quit()