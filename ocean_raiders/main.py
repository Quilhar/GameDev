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

        # Font
        font_path = 'ocean_raiders/ARCADE_I.TTF' # or wherever your font file is
        size = 18
        self.my_font = pygame.font.Font(font_path, size)

        self.load_images()
        
        # High score and score variables
        self.highscore = 0
        self.score = 0

        # Random variables for when I might need them
        self.randx = random.randint(64, MAP_WIDTH-64)
        self.randy = random.randint(64, MAP_HEIGHT-64)

    def load_images(self):
        '''load and/or get images'''

        # Map Images
        self.map = pytmx.load_pygame('/Users/244213/Desktop/GameDev/tiles/ocean_map.tmx')

        # Player Image
        self.player_image = pygame.image.load('ocean_raiders/player_ship.png')
        self.player_image = pygame.transform.scale(self.player_image, (TILESIZE, 64))

        # Bullet Image
        self.bullet_image = pygame.image.load('ocean_raiders/bullet.png')
        self.bullet_image = pygame.transform.scale(self.bullet_image, (TILESIZE // 2, TILESIZE // 2))
        
        

    def new(self):
        '''create all game objects, sprites, and groups"
        call run() method'''

        # Sprite Groups
        self.all_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.map_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group() 

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
                        self.enemy_image = pygame.transform.scale(obj.image, (obj.image.get_width() * 4, obj.image.get_height() * 4))
                        self.enemy = Enemy(self.screen, obj.x * 4, obj.y * 4, self.enemy_image, self)
                        self.enemy_sprites.add(self.enemy)
                        self.all_sprites.add(self.enemy)

        # Player
        self.player = Player(self.screen, ((MAP_WIDTH // 2) - TILESIZE), ((MAP_HEIGHT // 2) + (8 * TILESIZE)), self.player_image, self)
        self.all_sprites.add(self.player)

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

        # Updating the highscore
        if self.score > self.highscore:
            self.highscore = self.score


    def draw(self):
        '''fill the screen, draw the objects, and flip'''

        # Blitting all sprites
        for sprite in self.all_sprites:               
            self.screen.blit(sprite.image, sprite.rect)
        
        # Scores image
        scores_txt = f'Score: {self.score}   High Score: {self.highscore}'
        scores_img = self.my_font.render(scores_txt, True, WHITE)
        self.screen.blit(scores_img, (30, 10))

        # Updating the screen 
        pygame.display.flip()

    def events(self):
        '''game loop events'''
        for event in pygame.event.get():

            # events to end the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):

                if self.playing:
                    self.playing = False
                
                self.running = False
            
            # Keydown events
            elif event.type == pygame.KEYDOWN:
                
                ############## BULLET SPAWNING ##############
                if event.key == pygame.K_SPACE:

                    
                    bulletx = self.player.rect.centerx - 6
                    bullety = self.player.rect.centery - 5

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
        
        # Creating and blitting the title text
        self.screen.fill(BLACK)
        font = pygame.font.SysFont('Calibri', 50, True, False)
        title_txt = 'Ocean Raiders'
        title_img = font.render(title_txt, True, WHITE)
        title_rect = title_img.get_rect()
        title_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2)
        self.screen.blit(title_img, title_rect)

        # Creating and blitting the instructions text
        font = pygame.font.SysFont('Calibri', 25, True, False)
        instructions_txt = 'Press any key to start'
        instructions_img = font.render(instructions_txt, True, WHITE)
        instructions_rect = instructions_img.get_rect()
        instructions_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2 + 50)
        self.screen.blit(instructions_img, instructions_rect)
    
        pygame.display.flip()
    
        self.wait_for_key()
        

    def game_over_screen(self):
        '''the game over screen'''

        # Creating and blitting game over text
        self.screen.fill(BLACK)
        font = pygame.font.SysFont('Calibri', 50, True, False)
        game_over_txt = 'Game Over'
        game_over_img = font.render(game_over_txt, True, WHITE)
        game_over_rect = game_over_img.get_rect()
        game_over_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2)
        self.screen.blit(game_over_img, game_over_rect)

        # Creating and blitting the instructions text
        font = pygame.font.SysFont('Calibri', 25, True, False)
        instructions_txt = 'Press any key to start'
        instructions_img = font.render(instructions_txt, True, WHITE)
        instructions_rect = instructions_img.get_rect()
        instructions_rect.center = (MAP_WIDTH // 2, MAP_HEIGHT // 2 + 50)
        self.screen.blit(instructions_img, instructions_rect)

        pygame.display.flip()
        
        # Reset the score after losing
        self.scorecount = 0

        # Calling the wait_for_key method
        self.wait_for_key()
        
        # Stop the music
        self.music.stop()



    def wait_for_key(self):
        '''wait for a key press'''

        # Waiting for a key press to restart the game 
        self.waiting = True

        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.waiting = False
                    self.playing = True
                    self.music.play(-1)
            
                
                

##########################################
#### PLAY GAME ####
##########################################

game = Game()

game.show_start_screen()

while game.running:
    game.new()
    game.game_over_screen()

pygame.quit()