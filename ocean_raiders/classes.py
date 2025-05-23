import pygame
from settings import *
import random


class Player(pygame.sprite.Sprite):


    def __init__(self, screen, x, y, image, game):


        pygame.sprite.Sprite.__init__(self)


        # Miscellaneous Variables
        self.game = game
        self.image = image
        self.display = screen


        # Variables for movement and position
        self.player_speed = 8
        self.x = x
        self.y = y
        self.vy = 0
        self.vx = 0


        # Rect and position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        

    def get_keys(self):


        # Set starting velocity to 0 to stop it from moving without keys pressed and stop it from moving diagonally
        self.vx, self.vy = 0, 0
       
        keys = pygame.key.get_pressed()


        ## Player Movement
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vx = -self.player_speed
            self.vy = 0


        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vx = self.player_speed
            self.vy = 0


        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.vy = -self.player_speed
            self.vx = 0


        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
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
       
        # Player Collision
        self.collide_with_enemy()


    def collide_with_enemy(self):


        # Check for collision with enemies
        enemy_collision = pygame.sprite.spritecollide(self, self.game.enemy_sprites, False)


        # If there is a collision, end the game and play the game over sound
        if enemy_collision:
            self.game.game_over_sound.play()
            self.game.playing = False
    
    def power_up_collision(self):


        # Check for collision with player
        hit = pygame.sprite.spritecollide(self, self.game.powerup_sprites, True)


        # What happens when a powerup hits the player
        if hit:
            self.game.powerup_sound.play()
            self.game.powerup_active = True
            print("Powerup activated")
            
            if self.game.powerup.image == self.game.powerup_images_list[0]:
                while self.game.powerup_active:
                    self.game.score_increment == 200
            elif self.game.powerup.image == self.game.powerup_images_list[1]:
                print('speed')
           
   
class Bullet(pygame.sprite.Sprite):


    def __init__(self, screen, x, y, image, game):


        pygame.sprite.Sprite.__init__(self)


        # Basic position and rect
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        # Variables for movement
        self.y_bullet_speed = 10


        # Micellaneous Variables
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

            # Play explosion sound
            self.game.explosion_sound.play()
            
            # Increase the score
            self.game.score += self.game.score_increment
            
            # Remove the enemy and bullet from the game
            self.game.all_sprites.remove(self)
            self.game.bullet_sprites.remove(self)

class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, image, game):
        pygame.sprite.Sprite.__init__(self)


        # Miscellaneous Variables
        self.game = game
        self.image = image
        self.display = screen


        # Set the initial position of the enemy and creating rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy_Bullet(pygame.sprite.Sprite):


    def __init__(self, screen, x, y, image, game):


        pygame.sprite.Sprite.__init__(self)


        # Basic position and rect
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        # Variables for movement
        self.y_bullet_speed = 10


        # Micellaneous Variables
        self.display = screen
        self.game = game

    def update(self):

        # Update Bullet Position
        self.rect.y += self.y_bullet_speed

        # Bullet Collision
        self.bullet_collision()

    def bullet_collision(self):

        # Check for collision with player
        hit = pygame.sprite.spritecollide(self, self.game.player_sprite, False)

        # What happens when a bullet hits the player
        if hit:
            self.game.game_over_sound.play()
            self.game.playing = False

class Powerup(pygame.sprite.Sprite):


    def __init__(self, screen, x, y, image, game):


        pygame.sprite.Sprite.__init__(self)


        # Miscellaneous Variables
        self.game = game
        self.image = image
        self.display = screen


        # Set the initial position of the powerup and creating rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.active = False


                
            
                
                




 
