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

        # Font
        self.font_path = 'ocean_raiders/ARCADE_I.TTF'
       
        # High score and score variables
        self.highscore = 0
        self.score = 0

        # Random variables for when I might need them
        self.randx = random.randint(64, MAP_WIDTH-64)
        self.randy = random.randint(64, MAP_HEIGHT-64)

        # Variables for enemy movement
        self.enemy_direction = 1  
        self.enemy_speed = 5
        self.enemy_drop_distance = 15

        # Variables for the game
        self.level_count = 0

        # Cooldown variables
        self.cooldown = 0
        self.cooldown_time = 0.5
        

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


        # Finding Tiled Sprites
        for layer in self.map.visible_layers:
       
            tile_width = MAP_WIDTH // self.map.width
            tile_height = MAP_HEIGHT // self.map.height
            tile_size = min(tile_width, tile_height)


            # Map Tiles
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
        self.player = Player(self.screen, ((MAP_WIDTH // 2) - TILESIZE), ((MAP_HEIGHT // 2) + (8 * TILESIZE)), self.player_image, self)
        self.all_sprites.add(self.player)
        self.player_sprite.add(self.player)


        # Bullets
        self.bullet = Bullet(self.screen, self.randx, self.randy, self.bullet_image, self)

        self.run()


    def update(self):
        '''run all updates'''

        # Update all sprites
        self.all_sprites.update()


        # Making sure the bullets are removed when they leave the screen
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
                
        # Updating the highscore
        if self.score > self.highscore:

            self.highscore = self.score

        # What happens when all enemies are dead
        if len(self.enemy_sprites) == 0:

            # Increase the level count
            self.level_count += 1
            
            # Reset the enemy direction
            self.enemy_direction = 1

            # Score bonus for clearing a level
            self.score += 1000

            # Changing enemy speed based on level
            self.enemy_speed += 2

            # Creating new enemies
            self.new()

        # Cooldown for the bullet
        self.cooldown -= self.clock.get_time() / 1000

    def draw(self):
        '''fill the screen, draw the objects, and flip'''


        # Blitting all sprites
        for sprite in self.all_sprites:   

            self.screen.blit(sprite.image, sprite.rect)
       
        # Score and high score font while playing the game
        playing_score_font = pygame.font.Font(self.font_path, 18)

        # Creating and blitting the score and high score text
        scores_txt = f'Score:{self.score}'
        scores_img = playing_score_font.render(scores_txt, True, WHITE)
        self.screen.blit(scores_img, (50, 10))

        highscore_txt = f'High Score:{self.highscore}'
        highscore_img = playing_score_font.render(highscore_txt, True, WHITE)
        self.screen.blit(highscore_img, (MAP_WIDTH - 325, 10))


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
        title_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.25)
        self.screen.blit(title_img, title_rect)


        # Creating and blitting the instructions text
        instructions_font = pygame.font.Font(self.font_path, 25)
        instructions_txt = 'PRESS ANY KEY TO START'
        instructions_img = instructions_font.render(instructions_txt, True, WHITE)
        instructions_rect = instructions_img.get_rect()
        instructions_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2.25 + 75)
        self.screen.blit(instructions_img, instructions_rect)

        # Updating the screen
        pygame.display.flip()

        # Calling the wait_for_key method
        self.wait_for_key()
       


    def game_over_screen(self):
        '''the game over screen'''

        # Creating and blitting game over text
        self.screen.fill(BLACK)
        font = pygame.font.Font(self.font_path, 50)
        game_over_txt = 'GAME OVER'
        game_over_img = font.render(game_over_txt, True, WHITE)
        game_over_rect = game_over_img.get_rect()
        game_over_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 3)
        self.screen.blit(game_over_img, game_over_rect)


        # Creating and blitting the high score and score text
        end_score_font = pygame.font.Font(self.font_path, 25)


        score_txt = f'YOUR SCORE WAS: {self.score}'
        score_img = end_score_font.render(score_txt, True, WHITE)
        score_rect = score_img.get_rect()
        score_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 3 + 100)
        self.screen.blit(score_img, score_rect)


        highscore_txt = f'YOUR HIGHSCORE IS: {self.highscore}!'
        highscore_img = end_score_font.render(highscore_txt, True, WHITE)
        highscore_rect = highscore_img.get_rect()
        highscore_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 3 + 150)
        self.screen.blit(highscore_img, highscore_rect)

        


        # Creating and blitting the instructions text
        instructions_font = pygame.font.Font(self.font_path, 25)
        instructions_txt = 'PRESS ANY KEY TO RESTART'
        instructions_img = instructions_font.render(instructions_txt, True, WHITE)
        instructions_rect = instructions_img.get_rect()
        instructions_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 3 + 300)
        self.screen.blit(instructions_img, instructions_rect)

        # Updating the screen
        pygame.display.flip()
       
        # Reset the score after losing
        self.score = 0

        # Stop the music
        self.music.stop()

        # Reset enemy stats and 
        self.enemy_speed = 5
        self.enemy_direction = 1
        self.level_count = 0

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
           
               

##########################################
################ PLAY GAME ###############
##########################################


game = Game()


game.show_start_screen()


while game.running:
    game.new()
    game.game_over_screen()


pygame.quit()
