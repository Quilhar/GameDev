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

# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, screen, x, y, image_list):

#         pygame.sprite.Sprite.__init__(self)

#         self.image_list = image_list
#         self.image = self.image_list[0]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y

#         self.display = screen

#     def update(self):
#         self.rect.x -= 10

#     def get_keys(self):

#         keys = pygame.key.get_pressed()

#         if keys[pygame.K_a]:
#             self.image = self.image_list[2]
#         if keys[pygame.K_d]:
#             self.image = self.image_list[0]
#         if keys[pygame.K_w]:
#             self.image = self.image_list[1]
#         if keys[pygame.K_s]:
#             self.image = self.image_list[3]

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = image
        self.player_speed = 3
        self.display = screen

        self.x = x
        self.y = y
        self.vy = 0
        self.vx = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
class Key(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = image
        self.player_speed = 3
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
        
        

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.scorecount = 0

    def get_keys(self):
        self.vx, self.vy = 0, 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vx = -self.player_speed
            self.vy = 0
            self.image = self.image_list[0]
        if keys[pygame.K_d]:
            self.vx = self.player_speed
            self.vy = 0
            self.image = self.image_list[0]
        if keys[pygame.K_w]:
            self.vy = -self.player_speed
            self.vx = 0
            self.image = self.image_list[0]
        if keys[pygame.K_s]:
            self.vy = self.player_speed
            self.vx = 0
            self.image = self.image_list[0]


    def collide_with_buildings(self, dir):
        if dir == 'x':

            hits = pygame.sprite.spritecollide(self, self.game.collider_sprites, False)

            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                
                self.vx = 0
                self.rect.x = self.x

        if dir == 'y':

            hits = pygame.sprite.spritecollide(self, self.game.collider_sprites, False)

            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                
                self.vy = 0
                self.rect.y = self.y

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

    # def shoot(self):
    #     self.get_keys()

    #     self.bulletx = self.rect.centerx - 30
    #     self.bullety = self.rect.centery - 10

    #     bullet = Bullet(self.display, self.bulletx, self.bullety, self.game.bullet_image_list)
    #     self.game.bullet_sprite.add(bullet)
    #     self.game.all_sprites.add(bullet)

    #     if self.bullety < 0:
    #         self.game.bullet_sprite.remove(bullet)
    #         self.game.all_sprites.remove(bullet)

    #     if self.bullety > 768:
    #         self.game.bullet_sprite.remove(bullet)
    #         self.game.all_sprites.remove(bullet)

    #     if self.bulletx < 0:
    #         self.game.bullet_sprite.remove(bullet)
    #         self.game.all_sprites.remove(bullet)

    #     if self.bulletx > 1568:
    #         self.game.bullet_sprite.remove(bullet)
    #         self.game.all_sprites.remove(bullet)

        

class Camera:
    def __init__(self, width, height):
        # create a rectangle that encompasses the entire map
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def get_view(self, sprite_object):
        # all sprite objects will be moved based on the camera's position
        return sprite_object.rect.move(self.camera.topleft)
    
    def update(self, target):
        # shift the tile map in the opposite directs of the target
        # addding half the window size to keep the target in the center
        x = -target.rect.x + DISPLAY_WIDTH // 2
        y = -target.rect.y + DISPLAY_HEIGHT // 2

        # to stop scrollling when the edge at the edge of the title map
        # if the target moes too far left, or up, make x/y stay at 0
        x = min(0, x)
        y = min(0, y)

        # if the target moves too far right or down, make the target stop
        # at the width of the title map minus the width of the window
        x = max(-1 * (self.width - DISPLAY_WIDTH), x)
        y = max(-1 * (self.height - DISPLAY_HEIGHT), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)



