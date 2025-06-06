from settings import *
from classes import *
from levels import Tiled_Map
import pygame
import random
import pytmx


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
       
        # Game Window and other basic settings
        pygame.display.set_caption("Ocean Raiders")
        self.screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True


        # Sound/Music
        self.music = pygame.mixer.Sound('ocean_raiders/battle-mus.mp3')
        self.music.set_volume(0.5)
        self.music.play(-1)

        self.explosion_sound = pygame.mixer.Sound('ocean_raiders/explosion01.ogg')
        self.explosion_sound.set_volume(0.5)

        self.game_over_sound = pygame.mixer.Sound('ocean_raiders/GameOver.ogg')
        self.game_over_sound.set_volume(0.5)

        self.powerup_sound = pygame.mixer.Sound('ocean_raiders/powerup.wav')
        self.powerup_sound.set_volume(0.5)

        # Font
        self.font_path = 'ocean_raiders/ARCADE_I.TTF'
       
        # High score and score variables
        self.highscore = self.load_high_score()
        self.score = 0
        self.score_increment = 100

        # Random variables for when I might need them
        self.randx = random.randint(64, MAP_WIDTH-64)
        self.randy = random.randint(64, MAP_HEIGHT-64)

        # Variables for enemy movement
        self.enemy_direction = 1  
        self.enemy_speed = 2
        self.enemy_drop_distance = 15

        # Variables for the game
        self.level_count = 0

        # Cooldown for shooting variables
        self.cooldown = 0
        self.cooldown_time = 0.3

        # Powerup variables
        self.powerup_timer = 10
        self.powerup_cooldown = 30
        self.powerup_active = False
        self.powerup_spawn = False
        self.spawn_timer = 5

        # Loading images
        self.load_images()


    def load_images(self):
        '''load and/or get images'''

        # Map Images
        self.map = pytmx.load_pygame('/Users/244213/Desktop/GameDev/tiles/ocean_map.tmx')

        # Player Image
        self.player_image = pygame.image.load('ocean_raiders/player_ship.png')
        self.player_image = pygame.transform.scale(self.player_image, (TILESIZE, 64))

        # Bullet image
        self.bullet_image = pygame.image.load('ocean_raiders/bullet.png')
        self.bullet_image = pygame.transform.scale(self.bullet_image, (TILESIZE // 2, TILESIZE // 2))
       
        # Enemy Bullet Image
        self.enemy_bullet_image = pygame.image.load('ocean_raiders/red_laser.png')
        self.enemy_bullet_image = pygame.transform.scale(self.enemy_bullet_image, (TILESIZE // 2, TILESIZE // 2))
        self.enemy_bullet_image = pygame.transform.rotate(self.enemy_bullet_image, 90)

        # Powerup Images
        self.powerup_images_list = []

        # 2x Points Powerup
        self.points_powerup_image = pygame.image.load('ocean_raiders/2x_points.png')
        self.points_powerup_image = pygame.transform.scale(self.points_powerup_image, (TILESIZE, TILESIZE))
        self.powerup_images_list.append(self.points_powerup_image)

        # Lower CD Powerup
        self.lower_cd_powerup_image = pygame.image.load('ocean_raiders/cd_powerup.png')
        self.lower_cd_powerup_image = pygame.transform.scale(self.lower_cd_powerup_image, (TILESIZE, TILESIZE))
        self.powerup_images_list.append(self.lower_cd_powerup_image)    

        # Freezing Powerup
        self.freeze_powerup_image = pygame.image.load('ocean_raiders/freeze_powerup.png')
        self.freeze_powerup_image = pygame.transform.scale(self.freeze_powerup_image, (TILESIZE, TILESIZE))
        self.freeze_powerup_image.set_colorkey(WHITE)
        self.powerup_images_list.append(self.freeze_powerup_image)


    def new(self):
        '''create all game objects, sprites, and groups"
        call run() method'''

        # Sprite Groups
        self.all_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.map_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_bullet_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.powerup_sprites = pygame.sprite.Group()
        self.explosion_sprites = pygame.sprite.Group()

        # Finding Tiled Sprites
        for layer in self.map.visible_layers:
       
            tile_width = MAP_WIDTH // self.map.width
            tile_height = MAP_HEIGHT // self.map.height
            tile_size = min(tile_width, tile_height)


            # Map Tilesß
            if isinstance(layer, pytmx.TiledTileLayer):


                for x, y, surf in layer.tiles():
                    pos = (x * tile_size, y * tile_size)
                    surf = pygame.transform.scale(surf, (tile_size, tile_size))
                   
                    Tiled_Map(pos, surf, self.all_sprites)


            # Objects
            elif isinstance(layer, pytmx.TiledObjectGroup):
               
                for obj in layer:


                    # Enemy Object
                    if obj.name == 'enemy':
                        self.enemy_image = pygame.transform.scale(obj.image, (obj.image.get_width() * 3, obj.image.get_height() * 3))
                        self.enemy = Enemy(self.screen, obj.x * 4, obj.y * 4, self.enemy_image, self)
                        self.enemy_sprites.add(self.enemy)
                        self.all_sprites.add(self.enemy)

        # Player
        self.player = Player(self.screen, ((MAP_WIDTH // 2) - TILESIZE), ((MAP_HEIGHT // 2) + (12 * TILESIZE)), self.player_image, self)
        self.all_sprites.add(self.player)
        self.player_sprite.add(self.player)

        # Bullet
        self.bullet = Bullet(self.screen, self.randx, self.randy, self.bullet_image, self)

        # Powerups  
        self.powerup = Powerup(self.screen, (MAP_WIDTH // 2), random.randint((MAP_HEIGHT // 2), MAP_HEIGHT), random.choice(self.powerup_images_list), self)

        self.run()


    def update(self):
        '''run all updates'''

        # Update all sprites
        self.all_sprites.update()
    
        # Making sure bullets are removed when they leave the screen
        for bullet in self.bullet_sprites:
            if bullet.rect.y <= 0 or bullet.rect.y >= MAP_HEIGHT or bullet.rect.x <= 0 or bullet.rect.x >= MAP_WIDTH:
                self.bullet_sprites.remove(bullet)
                self.all_sprites.remove(bullet)

        for enemy_bullet in self.enemy_bullet_sprites:
            if enemy_bullet.rect.y <= 0 or enemy_bullet.rect.y >= MAP_HEIGHT or enemy_bullet.rect.x <= 0 or enemy_bullet.rect.x >= MAP_WIDTH:
                self.enemy_bullet_sprites.remove(enemy_bullet)
                self.all_sprites.remove(enemy_bullet)

        ############## ENEMY MOVEMENT ##############

        # This variable will be used to check if the enemies need to move down
        move_down = False

        # Move the enemies noramlly
        for enemy in self.enemy_sprites:

            enemy.rect.x += self.enemy_speed * self.enemy_direction
            
            # Check if any enemy hits the edge and if so it will make move down true
            if enemy.rect.right >= MAP_WIDTH or enemy.rect.left <= 0:

                move_down = True

        # If move down is true, then the enemies will move down and change direction
        
        if move_down:
            
            # Change the direction of the enemies
            self.enemy_direction *= -1
            
            # Move the enemies down
            for enemy in self.enemy_sprites:
                
                enemy.rect.y += self.enemy_drop_distance
                
        
        # Incase the player somehow manages to dodge all the bullets and the enemy goes off screen
        for enemy in self.enemy_sprites:
            if enemy.rect.y >= MAP_HEIGHT:
                self.game_over_sound.play()
                self.playing = False

        ##########################################

        # Enemy shooting

        # First part is just a random chance to shoot so not every enemy will shoot at the same time and its not too predictable
        # The second part is to make sure that the enemy will only shoot if there are enemies on the screen and makes it so errors don't happen when the enemy sprites are empty
        if random.randint(1, 100) <= 2 and len(self.enemy_sprites) > 0:
            
            # Randomly select an enemy to shoot
            random_enemy = random.choice(list(self.enemy_sprites))

            # Setting the bullet position to the center of the enemy
            enemy_bulletx = random_enemy.rect.centerx - 6
            enemy_bullety = random_enemy.rect.centery - 5

            # Creating the enemy bullet
            self.enemy_bullet = Enemy_Bullet(self.screen, enemy_bulletx, enemy_bullety, self.enemy_bullet_image, self)
            self.enemy_bullet_sprites.add(self.enemy_bullet)
            self.all_sprites.add(self.enemy_bullet)

        ##########################################

        # Updating the highscore
        if self.score > self.highscore:

            self.highscore = self.score
            self.save_high_score(self.highscore)

        ##########################################

        # What happens when all enemies are dead
        if len(self.enemy_sprites) == 0:

            # Increase the level count
            self.level_count += 1
            
            # Reset the enemy direction
            self.enemy_direction = 1

            # Score bonus for clearing a level
            self.score += 1000

            # Changing enemy speed for clearing a level
            self.enemy_speed += 1

            # Creating new enemies
            self.new()

        ##########################################

        # Cooldown for the bullet
        self.cooldown -= self.clock.get_time() / 1000

        ##########################################

        # Powerup 
        self.player.power_up_collision() 
    
        # If the powerup is active, start a timer for its duration
        if self.powerup_active: 

            self.powerup_timer -= self.clock.get_time() / 1000

            # If the powerup timer runs out, reset the powerup
            if self.powerup_timer <= 0:

                self.powerup_active = False
                self.powerup_cooldown_active = True 

                self.powerup_timer = 10  # Reset the timer for the next powerup
                self.score_increment = 100  # Reset the score increment to the default value
                self.cooldown_time = 0.3   # Reset the cooldown time to the default value 
                self.enemy_speed = self.level_count + 2 # Unfreeze the enemies
                self.enemy_drop_distance = 15
                
        # If the powerup is not active, start the cooldown for the next powerup and once that cooldown is over, the powerup will spawn
        if self.powerup_active == False:

            self.powerup_cooldown -= self.clock.get_time() / 1000

        if self.powerup_cooldown <= 0: 
            self.powerup = Powerup(self.screen, (MAP_WIDTH // 2), random.randint((MAP_HEIGHT // 2), MAP_HEIGHT), random.choice(self.powerup_images_list), self)
            self.all_sprites.add(self.powerup)
            self.powerup_sprites.add(self.powerup)
            self.powerup_spawn = True
            
            self.powerup_cooldown = 30 # Reset the cooldown for the next powerup
        
        # If the powerup is spawned, start a timer for how long the powerup will stay on the screen before you have to pick it up 
        if self.powerup_spawn:
            self.spawn_timer -= self.clock.get_time() / 1000

            if self.spawn_timer <= 0:
                self.powerup_spawn = False
                self.spawn_timer = 5
                self.powerup_sprites.remove(self.powerup)
                self.all_sprites.remove(self.powerup)

    def draw(self):
        '''fill the screen, draw the objects, and flip'''

        # Drawing all the sprites
        self.all_sprites.draw(self.screen)
        
        
        # Score and high score font while playing the game
        playing_score_font = pygame.font.Font(self.font_path, 18)

        # Creating and blitting the score and high score text
        scores_txt = f'Score:{self.score}'
        scores_img = playing_score_font.render(scores_txt, True, WHITE)
        self.screen.blit(scores_img, (50, 10))

        highscore_txt = f'High Score:{self.highscore}'
        highscore_img = playing_score_font.render(highscore_txt, True, WHITE)
        self.screen.blit(highscore_img, (MAP_WIDTH - 325, 10))

        # Powerup timer text
        if self.powerup_active:
            powerup_timer_font = pygame.font.Font(self.font_path, 18)
            powerup_timer_txt = f'Powerup Timer: {int(self.powerup_timer)}'
            powerup_timer_img = powerup_timer_font.render(powerup_timer_txt, True, WHITE)
            self.screen.blit(powerup_timer_img, (MAP_WIDTH // 2 - 125 , 40))

        # Updating the screen
        pygame.display.flip()


    def events(self):
        '''game loop events'''

        # Getting all events
        for event in pygame.event.get():

            # events to end the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):

                if self.playing:
                    self.playing = False
               
                self.running = False
           
            # Keydown events
            elif event.type == pygame.KEYDOWN:
               
                ############## BULLET SPAWNING ##############
                if event.key == pygame.K_SPACE and self.cooldown <= 0:

                    # Resetting the cooldown
                    self.cooldown = self.cooldown_time
                   
                    # The bullet will spawn at the center of the player
                    bulletx = self.player.rect.centerx - 6
                    bullety = self.player.rect.centery - 5

                    # Creating the bullet
                    self.bullet = Bullet(self.screen, bulletx, bullety, self.bullet_image, self)
                    self.bullet_sprites.add(self.bullet)
                    self.all_sprites.add(self.bullet)


    def run(self):
        '''contains the main game loop'''

        self.playing = True
       
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def show_start_screen(self):
        '''the screen to start the game'''

        # Filling the screen with black
        self.screen.fill(BLACK)

        # Creating and blitting the title text
        title_font = pygame.font.Font(self.font_path, 40)
        title_txt = 'OCEAN RAIDERS'
        title_img = title_font.render(title_txt, True, WHITE)
        title_rect = title_img.get_rect()
        title_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.5)
        self.screen.blit(title_img, title_rect)

        # Creating and blitting the instructions text
        instructions_font = pygame.font.Font(self.font_path, 20)
        instructions_txt = 'USE WASD OR ARROW KEYS TO MOVE'
        instructions_img = instructions_font.render(instructions_txt, True, WHITE)
        instructions_rect = instructions_img.get_rect()
        instructions_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.5 + 100)
        self.screen.blit(instructions_img, instructions_rect)

        instructions2_txt = 'PRESS SPACE TO SHOOT'  
        instructions2_img = instructions_font.render(instructions2_txt, True, WHITE)
        instructions2_rect = instructions2_img.get_rect()
        instructions2_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.5 + 135)
        self.screen.blit(instructions2_img, instructions2_rect)

        # Creating and blitting the start text
        start_font = pygame.font.Font(self.font_path, 20)
        start_txt = 'PRESS ANY KEY TO START'
        start_img = start_font.render(start_txt, True, WHITE)
        start_rect = start_img.get_rect()
        start_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.5 + 225)
        self.screen.blit(start_img, start_rect)

        # Updating the screen
        pygame.display.flip()

        # Calling the wait_for_key method
        self.wait_for_key()
       

    def game_over_screen(self):
        '''the game over screen'''

        # Creating and blitting game over text
        self.screen.fill(BLACK)
        font = pygame.font.Font(self.font_path, 40)
        game_over_txt = 'GAME OVER'
        game_over_img = font.render(game_over_txt, True, WHITE)
        game_over_rect = game_over_img.get_rect()
        game_over_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.5)
        self.screen.blit(game_over_img, game_over_rect)


        # Creating and blitting the high score and score text
        end_score_font = pygame.font.Font(self.font_path, 20)


        score_txt = f'YOUR SCORE WAS: {self.score}'
        score_img = end_score_font.render(score_txt, True, WHITE)
        score_rect = score_img.get_rect()
        score_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.5 + 100)
        self.screen.blit(score_img, score_rect)


        highscore_txt = f'YOUR HIGHSCORE IS: {self.highscore}'
        highscore_img = end_score_font.render(highscore_txt, True, WHITE)
        highscore_rect = highscore_img.get_rect()
        highscore_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.5 + 150)
        self.screen.blit(highscore_img, highscore_rect)


        # Creating and blitting the start text
        start_font = pygame.font.Font(self.font_path, 20)
        start_txt = 'PRESS ANY KEY TO RESTART'
        start_img = start_font.render(start_txt, True, WHITE)
        start_rect = start_img.get_rect()
        start_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 3 + 300)
        self.screen.blit(start_img, start_rect)

        # Updating the screen
        pygame.display.flip()
       
        # Reset the score after losing
        self.score = 0

        # Stop the music
        self.music.stop()

        # Reset some variables and stats
        self.enemy_speed = 2
        self.enemy_direction = 1 
        self.level_count = 0

        self.powerup_timer = 0
        self.powerup_cooldown = 30

        # Calling the wait_for_key method
        self.wait_for_key()


    def wait_for_key(self):
        '''wait for a key press'''

        # Waiting for a key press to restart the game
        self.waiting = True

        while self.waiting:

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.running = False
                
                # If the user presses a key or clicks the mouse, start the game and restart the music
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.waiting = False
                    self.playing = True
                    self.music.set_volume(0.5)
                    self.music.play(-1)
           
###########################################
######### FUNCTIONS FOR HIGHSCORE #########
###########################################

    def load_high_score(self):
        '''load the high score from the file'''
        
        # Try to open the high score file and read the high score, if there is no value in there yet or the file doesn't exist, just return a deafault value of 0
        try:
            with open('highscore.txt', 'r') as f:
                return int(f.readline())
        except (FileNotFoundError, ValueError):
            return 0
        

    def save_high_score(self, high_score):
        '''save the high score to the file'''
        
        # Open the high score file and write the high score to it

        with open('highscore.txt', 'w') as f:
            f.write(str(high_score))


##########################################
################ PLAY GAME ###############
##########################################

game = Game()


game.show_start_screen()


while game.running:
    game.new()
    game.game_over_screen()


pygame.quit()






