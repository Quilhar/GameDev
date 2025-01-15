from settings import *
from sprites import *
import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_images()

    def load_images(self):
        '''load and get all images'''
        tile_sheet = SpriteSheet('spritesheet/tilemap.png')
        self.tile_list = []

        #Map
        for y in range(11):
            for x in range(12):
                locx = 17 * x
                locy = 17 * y
                    
                tile_x = 16
                tile_y = 16
                
                tile_image = tile_sheet.get_image(locx, locy, tile_x, tile_y, 4, 4)
                tile_image.set_colorkey(BLACK)
                self.tile_list.append(tile_image)



        self.grass_list = [self.tile_list[0], self.tile_list[1], self.tile_list[2]]
        self.dirt_list = [self.tile_list[25], self.tile_list[40]]
        self.path_list = [self.tile_list[13], self.tile_list[14], self.tile_list[15], self.tile_list[25], self.tile_list[27], self.tile_list[37], self.tile_list[38], self.tile_list[39]]
        self.wall_list = [self.tile_list[127]]

        #Explosion
        explosion_sheet = SpriteSheet('spritesheet/explosion.png')
        self.explosion_list = []

        for y in range(5):
            for x in range(5):
                locx = 64 * x
                locy = 64 * y 


                explosion_image = explosion_sheet.get_image(locx, locy, 64, 64)

                explosion_image.set_colorkey(BLACK)

                self.explosion_list.append(explosion_image)

        #Player 
        player_x = 57
        player_y = 43
        player_sheet = SpriteSheet('spritesheet/spritesheet_characters.png')
        self.player_image = player_sheet.get_image(0, 0, player_x, player_y)
        self.player_image.set_colorkey(BLACK)
        self.player_image_list = [self.player_image, pygame.transform.rotate(self.player_image, 90), pygame.transform.rotate(self.player_image, 180), pygame.transform.rotate(self.player_image, 270)]

        #Zombie 
        zombie_x = 36
        zombie_y = 43
        zombie_sheet = SpriteSheet('spritesheet/spritesheet_characters.png')
        self.zombie_image = zombie_sheet.get_image(425, 0, zombie_x, zombie_y)
        self.zombie_image.set_colorkey(BLACK)

    def new(self):
        '''Create all game objects, sprites, and groups'''
        '''Call run() method'''
        self.player = Player(self.screen, self.player_image_list)

        self.run()


    def update(self):
        '''Run all updates'''
        self.player.get_keys()

    def draw(self):
        '''Fill the screen, draw the objets and flip'''

        self.screen.fill(WHITE)
     
        for row_index, row in enumerate(LAYOUTS[0]):
            for col_index, tile in enumerate(row):

                x_loc = col_index * TILESIZE
                y_loc = row_index * TILESIZE 

                if tile == '0':
                    self.screen.blit(self.dirt_list[1], (x_loc, y_loc))

                elif tile == '2':
                    self.screen.blit(self.grass_list[1], (x_loc, y_loc))

                elif tile == '3':
                    self.screen.blit(self.grass_list[2], (x_loc, y_loc))

                elif tile == '1':
                    self.screen.blit(self.wall_list[0], (x_loc, y_loc))
                
        
        self.player.draw()
        pygame.display.flip()

    def events(self):
        '''game loop events'''
        for event in pygame.event.get():
            # Events to end the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                
                if self.playing:
                    self.playing = False

                self.running = False


    def run(self):
        '''contains main game loop'''

        self.playing = True

        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def show_start_screen(self):
        '''the screen to start the game'''
        pass

    def game_over_screen(self):
        '''the game over screen'''
        pass

#########################################################
###                     PLAY GAME                     ###
#########################################################

game = Game()

game.show_start_screen()

while game.running:
    game.new()
    game.game_over_screen()

pygame.quit()


# def game_play():
#     pygame.init()
#     screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
#     pygame.display.set_caption("Game Title")

#     clock = pygame.time.Clock()
#     playing = True

#     tile_sheet = SpriteSheet('spritesheet/tilemap.png')
#     tile_list = []

#     #Map
#     for y in range(11):
#         for x in range(12):
#             locx = 17 * x
#             locy = 17 * y
                
#             tile_x = 16
#             tile_y = 16
            
#             tile_image = tile_sheet.get_image(locx, locy, tile_x, tile_y, 4, 4)
#             tile_image.set_colorkey(BLACK)
#             tile_list.append(tile_image)



#     grass1_img = tile_list[0]
#     grass2_img = tile_list[60]

#     #Explosion
#     explosion_sheet = SpriteSheet('spritesheet/explosion.png')
#     explosion_list = []

#     for y in range(5):
#         for x in range(5):
#             locx = 64 * x
#             locy = 64 * y 


#             explosion_image = explosion_sheet.get_image(locx, locy, 64, 64)

#             explosion_image.set_colorkey(BLACK)

#             explosion_list.append(explosion_image)

#     #Player 
#     player_x = 57
#     player_y = 43
#     player_sheet = SpriteSheet('spritesheet/spritesheet_characters.png')
#     player_image = player_sheet.get_image(0, 0, player_x, player_y)
#     player_image.set_colorkey(BLACK)

#     #Zombie 
#     zombie_x = 36
#     zombie_y = 43
#     zombie_sheet = SpriteSheet('spritesheet/spritesheet_characters.png')
#     zombie_image = zombie_sheet.get_image(425, 0, zombie_x, zombie_y)
#     zombie_image.set_colorkey(BLACK)


#     while playing:
#         for event in pygame.event.get():
#             #Events to end the game
#             if event.type == pygame.QUIT:
#                 playing = False

#         screen.fill(BG_COLOR)

#         screen.blit(explosion_list[0], (100, 100))
#         screen.blit(player_image, (100, 100))
#         screen.blit(zombie_image, (200, 100))
#         screen.blit(grass2_img, (0, 0))
#         pygame.display.flip()

# game_play()