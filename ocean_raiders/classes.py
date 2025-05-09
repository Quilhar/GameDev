import pygame
from settings import *
import random

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = image
        self.display = screen

        self.player_speed = 8
        self.x = x
        self.y = y
        self.vy = 0
        self.vx = 0
        
        
        self.dir = 'right'

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.scorecount = 0

    def get_keys(self):
        self.vx, self.vy = 0, 0
        
        keys = pygame.key.get_pressed()

        ## Player Movement
        if keys[pygame.K_a]:
            self.vx = -self.player_speed
            self.vy = 0
        if keys[pygame.K_d]:
            self.vx = self.player_speed
            self.vy = 0

        if keys[pygame.K_w]:
            self.vy = -self.player_speed
            self.vx = 0

        if keys[pygame.K_s]:
            self.vy = self.player_speed
            self.vx = 0

    def update(self):
        self.get_keys()
        
        # Update Player Position
        self.x += self.vx
        self.y += self.vy

        self.rect.x = self.x
        self.rect.y = self.y
        
        # Make sure player stays within the map
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > MAP_WIDTH - self.rect.width:
            self.rect.x = MAP_WIDTH - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > MAP_HEIGHT - self.rect.height:
            self.rect.y = MAP_HEIGHT - self.rect.height

    def collide_with_enemy(self):

        # Check for collision with enemies
        enemy_collision = pygame.sprite.spritecollide(self, self.game.enemy_sprites, False)

        # If there is a collision end the game
        if enemy_collision:
            self.game.playing = False
    

        return self.game.playing
    
class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y_bullet_speed = 10

        self.display = screen

        self.game = game

    def update(self):
        
        # Update Bullet Position
        self.rect.y -= self.y_bullet_speed

        # Bullet Collision
        self.bullet_collision()
    
    def bullet_collision(self):

        # Check for collision with enemies
        hit = pygame.sprite.spritecollide(self, self.game.enemy_sprites, True)

        # What happens when a bullet hits an enemy
        if hit:
            self.game.score += 100
            self.game.all_sprites.remove(self)
            self.game.bullet_sprites.remove(self)

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