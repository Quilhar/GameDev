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
        
        self.screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.load_images()

    def load_images(self):
        '''load and/or get images'''

        # Map Images
        self.map = pytmx.load_pygame('/Users/244213/Desktop/GameDev/tiles/ocean_map.tmx')

        # Player Image
        self.player_image = pygame.image.load('ocean_raiders/player_ship.png')
        
        

    def new(self):
        '''create all game objects, sprites, and groups"
        call run() method'''

        # Sprite Groups
        self.all_sprites = pygame.sprite.Group()
        self.map_sprites = pygame.sprite.Group()

        # Create the map
        for layer in self.map.visible_layers:
        
            tile_width = MAP_WIDTH // self.map.width
            tile_height = MAP_HEIGHT // self.map.height
            tile_size = min(tile_width, tile_height)

            if isinstance(layer, pytmx.TiledTileLayer):

                
                for x, y, surf in layer.tiles():
                    pos = (x * tile_size, y * tile_size)
                    surf = pygame.transform.scale(surf, (tile_size, tile_size))
                    
                    Tiled_Map(pos, surf, self.all_sprites)

        self.run()

    def update(self):
        '''run all updates'''
        self.all_sprites.update()



    def draw(self):
        '''fill the screen, draw the objects, and flip'''
        

        pygame.display.flip()

    def events(self):
        '''game loop events'''
        for event in pygame.event.get():
            # events to end the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                if self.playing:
                    self.playing = False
                    self.running = False

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
        pass

    def game_over_screen(self):
        '''the game over screen'''
        pass

##########################################
#### PLAY GAME ####
##########################################

game = Game()

game.show_start_screen()

while game.running:
    game.new()
    game.game_over_screen()

pygame.quit()