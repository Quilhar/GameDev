import pygame
from settings import *

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
        if self.rect.y < self.game.enemy.rect.y:
            self.rect.y = self.game.enemy.rect.y
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
            
            if self.game.powerup.image == self.game.powerup_images_list[0] and self.game.powerup_active:

                self.game.score_increment = 200

            elif self.game.powerup.image == self.game.powerup_images_list[1] and self.game.powerup_active:

                self.game.cooldown_time = 0

            elif self.game.powerup.image == self.game.powerup_images_list[2] and self.game.powerup_active:

                self.game.enemy_speed = 0
           
   
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

            # Create an explosion at the enemy's position
            explosion = Explosion(self.display, self.game.enemy.rect.x, self.game.enemy.rect.y, self.game)
            self.game.all_sprites.add(explosion)
            self.game.explosion_sprites.add(explosion)

            print(self.game.enemy.rect.x, self.game.enemy.rect.y)

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


class Explosion(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, game):

        pygame.sprite.Sprite.__init__(self)

        # Miscellaneous Variables
        self.game = game
        self.display = screen

        # Explosion Spritesheet
        explosion_sheet = SpriteSheet('spritesheet/explosion.png')
        self.explosion_list = []

        # Load the explosion images from the spritesheet
        for y in range(5):
            for x in range(5):
                locx = 64 * x
                locy = 64 * y 

                explosion_image = explosion_sheet.get_image(locx, locy, 64, 64)

                explosion_image.set_colorkey(BLACK)

                self.explosion_list.append(explosion_image)

        # Set the initial position of the explosion and creating rect
        self.index = 0
        self.image = self.explosion_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
        self.counter = 0

    def update(self):

        explosion_speed = .2

        #update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.explosion_list) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.explosion_list[self.index]

        #if the animation is complete, reset animation index
        if self.index >= len(self.explosion_list) - 1 and self.counter >= explosion_speed:
            self.kill()

 
