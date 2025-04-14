from settings import *
from sprites import *
from levels import Tiled_Map
import pygame
import random
import pytmx

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_images()
        self.playing = False
        self.cd = 0
 
    def load_images(self):
        '''load and get all images'''
        self.arrow_image = pygame.image.load('spritesheet/arrow.png')
        
        # tile_sheet = SpriteSheet('spritesheet/tilemap.png')
        # self.tile_list = []

        # #Map
        # for y in range(11):
        #     for x in range(12):
        #         locx = 17 * x
        #         locy = 17 * y
                    
        #         tile_x = 16
        #         tile_y = 16
                
        #         tile_image = tile_sheet.get_image(locx, locy, tile_x, tile_y, 2, 2, True)
        #         self.tile_list.append(tile_image)



        # self.grass_list = [self.tile_list[0], self.tile_list[1], self.tile_list[2]]
        # self.dirt_list = [self.tile_list[25], self.tile_list[40]]
        # self.path_list = [self.tile_list[13], self.tile_list[14], self.tile_list[15], self.tile_list[25], self.tile_list[27], self.tile_list[37], self.tile_list[38], self.tile_list[39]]
        # self.wall_img = self.tile_list[126]
        # self.token_img = self.tile_list[93]
        # self.token_img = pygame.transform.scale(self.token_img, (32, 32))

        # #Bullet
        self.bullet_image = pygame.image.load('spritesheet/arrow.png')
        self.bullet_image = pygame.transform.scale(self.bullet_image, (12, 16))
        self.bullet_image_list = [self.bullet_image, pygame.transform.rotate(self.bullet_image, -90), pygame.transform.rotate(self.bullet_image, 90), pygame.transform.rotate(self.bullet_image, 180)]

        # #Explosion
        # explosion_sheet = SpriteSheet('spritesheet/explosion.png')
        # self.explosion_list = []

        # for y in range(5):
        #     for x in range(5):
        #         locx = 64 * x
        #         locy = 64 * y 

        #         explosion_image = explosion_sheet.get_image(locx, locy, 64, 64)

        #         explosion_image.set_colorkey(BLACK)

        #         self.explosion_list.append(explosion_image)

        ## Player 
        # player_x = 57
        # player_y = 43
        # player_sheet = SpriteSheet('spritesheet/spritesheet_characters.png')
        # self.player_image = player_sheet.get_image(0, 0, player_x, player_y, None)
        # self.player_image.set_colorkey(BLACK)
        # self.player_image_list = [self.player_image, pygame.transform.rotate(self.player_image, 90), pygame.transform.rotate(self.player_image, 180), pygame.transform.rotate(self.player_image, 270)]

        ## Zombie 
        # zombie_x = 36
        # zombie_y = 43
        # zombie_sheet = SpriteSheet('spritesheet/spritesheet_characters.png')
        # self.zombie_image = zombie_sheet.get_image(425, 0, zombie_x, zombie_y)
        # self.zombie_image.set_colorkey(BLACK)

    def new(self):
        '''Create all game objects, sprites, and groups'''
        '''Call run() method'''
        self.randx = random.randint(64, DISPLAY_WIDTH-64)
        self.randy = random.randint(64, DISPLAY_HEIGHT-64)

        #sprite groups
        # self.wall_sprite = pygame.sprite.Group()
        # self.token_sprite = pygame.sprite.Group()
        self.bullet_sprite = pygame.sprite.Group()

        
        self.all_sprites = pygame.sprite.Group()
        self.collider_sprites = pygame.sprite.Group() 
        self.enemy_sprites = pygame.sprite.Group()
        self.key_sprites = pygame.sprite.Group()
        

        self.map = pytmx.load_pygame("/Users/244213/Desktop/GameDev/tiles/level1.tmx")
        self.map_sprites = pygame.sprite.Group()


        # print(dir(self.map))
        # print(self.map.visible_layers)
        # for layer in self.map.layers:
        #     print(layer)
        # print(self.map.get_layer_by_name('Base'))

    
        for layer in self.map.visible_layers:
        
            tile_width = MAP_WIDTH // self.map.width
            tile_height = MAP_HEIGHT // self.map.height
            tile_size = min(tile_width, tile_height)

            if isinstance(layer, pytmx.TiledTileLayer):

                
                for x, y, surf in layer.tiles():
                    pos = (x * tile_size, y * tile_size)
                    surf = pygame.transform.scale(surf, (tile_size, tile_size))
                    
                    Tiled_Map(pos, surf, self.all_sprites)

            elif isinstance(layer, pytmx.TiledObjectGroup):
                
                for obj in layer:

                    # Player Object
                    if obj.name == 'Player':
                        # self.player_image_list = [obj.image, pygame.transform.rotate(obj.image, 90), pygame.transform.rotate(obj.image, 180), pygame.transform.rotate(obj.image, 270)]
                        self.player_image_list = [pygame.transform.scale(obj.image, (obj.image.get_width() * SCALEFACTOR, obj.image.get_height() * SCALEFACTOR))]
                        self.player = Player(self.screen, obj.x * SCALEFACTOR, obj.y * SCALEFACTOR, self.player_image_list, self)
                        self.all_sprites.add(self.player)
                    
                    # Collider Objects
                    elif obj.name == 'House':
                        self.collider = Colliders(self.screen, obj.x * SCALEFACTOR, obj.y * SCALEFACTOR, obj.width * SCALEFACTOR, obj.height * SCALEFACTOR)
                        self.collider_sprites.add(self.collider)
                        
                    elif obj.name == 'Fence':
                        self.collider = Colliders(self.screen, obj.x * SCALEFACTOR, obj.y * SCALEFACTOR, obj.width * SCALEFACTOR, obj.height * SCALEFACTOR)
                        self.collider_sprites.add(self.collider)
                        
                    elif obj.name == 'Sign':
                        self.collider = Colliders(self.screen, obj.x * SCALEFACTOR, obj.y * SCALEFACTOR, obj.width * SCALEFACTOR, obj.height * SCALEFACTOR)
                        self.collider_sprites.add(self.collider)

                    elif obj.name == 'Tree':
                        self.collider = Colliders(self.screen, obj.x * SCALEFACTOR, obj.y * SCALEFACTOR, obj.width * SCALEFACTOR, obj.height * SCALEFACTOR)
                        self.collider_sprites.add(self.collider)

                    elif obj.name == 'Bush':
                        self.collider = Colliders(self.screen, obj.x * SCALEFACTOR, obj.y * SCALEFACTOR, obj.width * SCALEFACTOR, obj.height * SCALEFACTOR)
                        self.collider_sprites.add(self.collider)
                    
                    # Enemy Objects
                    elif obj.name == 'Enemy':
                        self.enemy_image = pygame.transform.scale(obj.image, (obj.image.get_width() * SCALEFACTOR, obj.image.get_height() * SCALEFACTOR))
                        self.enemy = Enemy(self.screen, obj.x * SCALEFACTOR, obj.y * SCALEFACTOR, self.enemy_image, self)
                        self.enemy_sprites.add(self.enemy)
                        self.all_sprites.add(self.enemy)
                    
                    # Key Objects
                    elif obj.name == 'Key':
                        self.key_image = pygame.transform.scale(obj.image, (obj.image.get_width() * 2, obj.image.get_height() * 2))
                        self.key = Key(self.screen, obj.x * SCALEFACTOR, obj.y * SCALEFACTOR, self.key_image, self)
                        self.key_sprites.add(self.key)
                        self.all_sprites.add(self.key)

            self.bullet = Bullet(self.screen, self.randx, self.randy, self.bullet_image_list)

                     

        #player sprites
        # self.player = Player(self.screen, 175, 75, self.player_image_list, self)
        

        #token sprites
        # self.token = Token(self.screen, self.randx, self.randy, self.token_img)
        

        # for row_index, row in enumerate(LAYOUTS[0]):
        #     for col_index, tile in enumerate(row):

        #         x_loc = col_index * TILESIZE
        #         y_loc = row_index * TILESIZE 

        #         self.wall_list = []
        #         if tile == '1': 
        #             brick = Wall(self.screen, x_loc, y_loc, self.wall_img)
        #             self.wall_sprite.add(brick)
        #             self.all_sprites.add(brick)

        #         if tile == '0':
        #             dirt_path = Background(self.screen, x_loc, y_loc, self.dirt_list[1])
        #             self.all_sprites.add(dirt_path)

        #         if tile == ' ':
        #             grass_tile = Background(self.screen, x_loc, y_loc, self.grass_list[1])
        #             self.all_sprites.add(grass_tile)

        
        # #add sprites to groups
        # self.all_sprites.add(self.player)

        # self.all_sprites.add(self.token)
        # self.token_sprite.add(self.token)


        self.pov = Camera(MAP_WIDTH, MAP_HEIGHT)

        self.run()


    def update(self):
        '''Run all updates'''
        self.player.update()       
        # self.score = self.player.collide_with_token()
        self.pov.update(self.player)
        self.bullet.update()
        self.bullet.get_keys()
        self.enemy.move_towards_player()

        if self.bullet.rect.y < 0:
            self.bullet_sprite.remove(self.bullet)
            self.all_sprites.remove(self.bullet)

        if self.bullet.rect.y > MAP_HEIGHT:
            self.bullet_sprite.remove(self.bullet)
            self.all_sprites.remove(self.bullet)

        if self.bullet.rect.x < 0:
            self.bullet_sprite.remove(self.bullet)
            self.all_sprites.remove(self.bullet)

        if self.bullet.rect.x > MAP_WIDTH:
            self.bullet_sprite.remove(self.bullet)
            self.all_sprites.remove(self.bullet)

    def draw(self):
        '''Fill the screen, draw the objets and flip'''

        # self.screen.fill(WHITE)

        # camera requires blitting rather than calling all_sprites draw method
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.pov.get_view(sprite))


        # font = pygame.font.SysFont('Calibri', 35, True, False)
        # score_txt = f'Score: {self.score}'
        # score_img = font.render(score_txt, True, WHITE)
        # self.screen.blit(score_img, [260, 60])
        
        # self.screen.blit(self.player.mask_image, self.player.rect.topleft)
        # pygame.draw.rect(self.screen, BLACK, self.player.rect, 3)

        pygame.display.flip()

    def events(self):
        '''game loop events'''

        # self.cd += pygame.time.get_ticks()
        # if self.cd >= 3000:
        #     self.cd = 0

        for event in pygame.event.get():
            # Events to end the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                
                if self.playing:
                    self.playing = False
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    ############## BULLET ##############
                    self.bulletx = self.player.rect.centerx - 6
                    self.bullety = self.player.rect.centery - 5

                    self.bullet = Bullet(self.screen, self.bulletx, self.bullety, self.bullet_image_list)
                    self.bullet_sprite.add(self.bullet)
                    self.all_sprites.add(self.bullet)

                
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

