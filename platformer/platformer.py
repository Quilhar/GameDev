from settings import *
import components as comps
import pygame



################################################################################


screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Game Title")


clock = pygame.time.Clock()

def loading_level(level_count):

# Loading imgs
    block_img = pygame.image.load('platformer/images/block.png')
    front_img = pygame.image.load('platformer/images/front.png')
    slime_img = pygame.image.load('platformer/images/slime_normal.png')
    ground_img = pygame.image.load('platformer/images/ground.png')
    checkpoint_on_img = pygame.image.load('platformer/images/switch_green_on.png')
    checkpoint_off_img = pygame.image.load('platformer/images/switch_red_on.png')
    door_img = pygame.image.load('platformer/images/lock_red.png')
    spike_img = pygame.image.load('platformer/images/spikes.png')

 
    right_list = []
    left_list = []
    

    for i in range(1, 12):
        # initial right img
        img = f"platformer/images/player/walk000{i}.png"
        right = pygame.image.load(img)

        # scaling img
        right = pygame.transform.scale(right, (BRICK_WIDTH - 20, BRICK_HEIGHT- 20))
        left = pygame.transform.flip(right, True, False)

        right_list.append(right)
        left_list.append(left)


    player = None
    brick_list = []
    enemy_list = []
    barrier_list = []
    ground_list = []
    spike_list = []
    door_list = []
    checkpoint_list = []




    current_level = LAYOUTS[level_count]


    for row in range(len(current_level)):
        y_loc = row * BRICK_HEIGHT


        for col in range(len(current_level[row])):
            x_loc = col * BRICK_WIDTH


            if current_level[row][col] == "1":
                brick = comps.Brick(x_loc, y_loc, BRICK_WIDTH, BRICK_HEIGHT, BRICK, screen, block_img)


                brick_list.append(brick)        


            elif current_level[row][col] == "p":
                player = comps.Player(x_loc, y_loc + 20, screen, right_list, left_list)
               
           
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

            elif current_level[row][col] == "c":
                checkpoint = comps.Checkpoint(x_loc + 5, y_loc + (BRICK_HEIGHT/2), BRICK_WIDTH - 10, BRICK_HEIGHT/2, BRICK, screen, checkpoint_off_img, checkpoint_on_img)

                checkpoint_list.append(checkpoint)

    return player, brick_list, enemy_list, barrier_list, ground_list, spike_list, door_list, checkpoint_list
    #######################################################################






#####################################################
level_count = 0  # Start at the first level
playing = True


player, brick_list, enemy_list, barrier_list, ground_list, spike_list, door_list, checkpoint_list = loading_level(level_count)


while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False


   
    screen.fill(BG_COLOR)


    # Draw game objects
    for brick in brick_list:
        brick.draw_brick()


    for ground in ground_list:
        ground.draw_ground()

    for enemy in enemy_list:
        enemy.draw_enemy()
        enemy.enemy_update(ground_list, barrier_list)

    for spike in spike_list:
        spike.draw_spike()


    for door in door_list:
        door.draw_door()

    for checkpoint in checkpoint_list:
        checkpoint.draw()
        checkpoint.update(player)


    if player:
        level_transition = player.update(brick_list, enemy_list, ground_list, spike_list, door_list, checkpoint_list)
        player.draw()
        
      

    # Handle level transition
    if level_transition:
        level_count = (level_count + 1) % len(LAYOUTS)
        player, brick_list, enemy_list, barrier_list, ground_list, spike_list, door_list, checkpoint_list = loading_level(level_count)


    # Control text
    font = pygame.font.SysFont('Calibri', 50, True, False)
    start_txt = 'Use "A" and "D" to move left and right and Spacebar to jump'
    title_img = font.render(start_txt, True, WHITE)
    screen.blit(title_img, [425,450])


    # Update display
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
