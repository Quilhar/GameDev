import pygame
from settings import *
import random

class SpriteSheet():
    
    def __init__(self, filename):
        self.SpriteSheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height, scale_x = None, scale_y = None, color_key = None):

        #Get the image at (x, y) on the spritesheet
        image = pygame.Surface((width, height))
        image.blit(self.SpriteSheet, (0, 0), (x, y, width, height))

        if scale_x and scale_y:
            image = pygame.transform.scale(image, (width * scale_x, height * scale_y))

        if color_key:
            color = BLACK
            image.set_colorkey(color)

        return image

# class Wall(pygame.sprite.Sprite):
#     def __init__(self, screen, x, y, img):

#         pygame.sprite.Sprite.__init__(self)

#         self.image = img
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y

#         self.display = screen

# class Token(pygame.sprite.Sprite):
#     def __init__(self, screen, x, y, img):

#         pygame.sprite.Sprite.__init__(self)

#         self.image = img
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y

#         self.display = screen

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image_list, dir, game):

        pygame.sprite.Sprite.__init__(self)

        self.image_list = image_list
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y_bullet_speed = 10
        self.x_bullet_speed = 10

        self.display = screen

        self.dir = dir

        self.game = game

    def update(self):
    
        if self.dir == 'left':
            self.x_bullet_speed = -10
            self.y_bullet_speed = 0
            self.image = self.image_list[2]
        elif self.dir == 'right':
            self.x_bullet_speed = 10
            self.y_bullet_speed = 0
            self.image = self.image_list[1]
        elif self.dir == 'up':
            self.y_bullet_speed = -10
            self.x_bullet_speed = 0
            self.image = self.image_list[0]
        elif self.dir == 'down':
            self.y_bullet_speed = 10
            self.x_bullet_speed = 0
            self.image = self.image_list[3]
        else:
            self.y_bullet_speed = 0
            self.x_bullet_speed = 0
            self.image = self.image_list[1]
        
        
        self.rect.x += self.x_bullet_speed
        self.rect.y += self.y_bullet_speed

        self.bullet_collision()

    def bullet_collision(self):
        hit = pygame.sprite.spritecollide(self, self.game.enemy_sprites, True)

        if hit:
            self.game.scorecount += 1
            self.game.all_sprites.remove(self)
            self.game.bullet_sprites.remove(self)
            

    def draw(self):
        self.display.blit(self.image, self.rect)
            

# class Background(pygame.sprite.Sprite):
#     def __init__(self, screen, x, y, img):

#         pygame.sprite.Sprite.__init__(self)

#         self.image = img
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
        
#         self.x = x
#         self.y = y
#         self.vy = 0
#         self.vx = 0

#         self.display = screen
class Colliders(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

        self.display = screen

        self.colliders_mask = pygame.mask.from_surface(self.image)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = image
        self.speed = 2
        self.display = screen

        self.x = x
        self.y = y
        self.vy = 0
        self.vx = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_towards_player(self):
        pass
        # # Find direction vector (dx, dy) between enemy and player.
        # dirvect = pygame.math.Vector2(self.game.player.rect.x - self.rect.x,
        #                             self.game.player.rect.y - self.rect.y)
        # dirvect.normalize()
        # # Move along this normalized vector towards the player at current speed.
        # dirvect.scale_to_length(self.speed)
        # self.rect.move_ip(dirvect)
    
class Key(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = image
        self.display = screen

        self.x = x
        self.y = y
        self.vy = 0
        self.vx = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, image_list, game):

        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image_list = image_list
        self.player_speed = 4
        self.display = screen

        self.x = x
        self.y = y
        self.vy = 0
        self.vx = 0
        self.image = self.image_list[0]
        
        self.dir = 'right'

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.scorecount = 0

        # Create Player Mask
        self.player_mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.player_mask.to_surface()      # An image of the mask (not needed)

    def get_keys(self):
        self.vx, self.vy = 0, 0
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vx = -self.player_speed
            self.vy = 0
            self.image = self.image_list[0]
            self.dir = 'left'
        if keys[pygame.K_d]:
            self.vx = self.player_speed
            self.vy = 0
            self.image = self.image_list[0]
            self.dir = 'right'
        if keys[pygame.K_w]:
            self.vy = -self.player_speed
            self.vx = 0
            self.image = self.image_list[0]
            self.dir = 'up' 
        if keys[pygame.K_s]:
            self.vy = self.player_speed
            self.vx = 0
            self.image = self.image_list[0]
            self.dir = 'down'

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.player_mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.player_mask.to_surface()      # Use this code if you change images during movement
        # return self.dir
    def collide_with_buildings(self, dir):
        
        # Mask Collision detection
        if pygame.sprite.spritecollide(self, self.game.collider_sprites, False):

            hits = pygame.sprite.spritecollide(self, self.game.collider_sprites, False, pygame.sprite.collide_mask)
            
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                    print(hits[0])
                    # print('right')
                if self.vx < 0:
                    self.x = hits[0].rect.right
                    # print('left')
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                    # print('down')
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                    # print('up')
                
                self.vx = 0
                self.rect.x = self.x
                self.vy = 0
                self.rect.y = self.y

        # Rectangle collision detection

        # if dir == 'x':
                
        #     hits = pygame.sprite.spritecollide(self, self.game.collider_sprites, False)

        #     if hits:
        #         if self.vx > 0:
        #             self.x = hits[0].rect.left - self.rect.width
        #         if self.vx < 0:
        #             self.x = hits[0].rect.right
                
        #         self.vx = 0
        #         self.rect.x = self.x

        # if dir == 'y':

        #     hits = pygame.sprite.spritecollide(self, self.game.collider_sprites, False)

        #     if hits:
        #         if self.vy > 0:
        #             self.y = hits[0].rect.top - self.rect.height
        #         if self.vy < 0:
        #             self.y = hits[0].rect.bottom
                
        #         self.vy = 0
        #         self.rect.y = self.y

    def collide_with_enemy(self):
        enemy_collision = pygame.sprite.spritecollide(self, self.game.enemy_sprites, False)

        if enemy_collision:
            self.game.playing = False

        return self.game.playing

    # def collide_with_token(self):
    #     token_collision = pygame.sprite.spritecollide(self, self.game.token_sprite, True)

    #     randx = random.randint(64, DISPLAY_WIDTH-64)
    #     randy = random.randint(64, DISPLAY_HEIGHT-64)
        
    #     if token_collision:
    #         token = Token(self.display, randx, randy, self.game.token_img)
    #         self.game.token_sprite.add(token)
    #         self.game.all_sprites.add(token)

    #         self.scorecount += 1

    #     return self.scorecount

    def update(self):
        self.get_keys()

        self.x += self.vx
        self.y += self.vy

        self.rect.x = self.x
        self.collide_with_buildings('x')
        self.rect.y = self.y
        self.collide_with_buildings('y')
        
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > MAP_WIDTH - self.rect.width:
            self.rect.x = MAP_WIDTH - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > MAP_HEIGHT - self.rect.height:
            self.rect.y = MAP_HEIGHT - self.rect.height
        
        self.collide_with_enemy()

        # self.collide_with_token()

class Camera():
   def __init__(self, width, height):
       #create a rect that encompasses the entire map
       self.camera = pygame.Rect(0, 0, width, height)
       self.width = width
       self.height = height

   def get_view(self, sprite_object):
       # all sprite objects (walls, platforms, etc) will be moved
       # based on the cameras updated position
       return sprite_object.rect.move(self.camera.topleft)

   def update(self, target):
       # shift the tile_map in the opposite direction of the target
       # adding half the window size to keep the target centered
       x = -target.rect.x + int(DISPLAY_WIDTH / 2)
       y = -target.rect.y + int(DISPLAY_HEIGHT / 2)

       # to stop the scrolling when at the edge of the tile map
       # if the target moves too far left or up make x/y stay 0
       x = min(0, x)
       y = min(0, y)
      
       # if the target moves too far down or right make x/y stay at
       # the width of the tile-map minus the width of the window
       x = max(-1*(self.width - DISPLAY_WIDTH), x)
       y = max(-1*(self.height - DISPLAY_HEIGHT), y)
      
       # adjust the camera based on the new location
       self.camera = pygame.Rect(x, y, self.width, self.height)



