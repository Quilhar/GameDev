import pygame
from settings import *
class Player():
    def __init__(self, x_loc, y_loc, width, height, color, display, image):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc

        self.x_loc = x_loc
        self.y_loc = y_loc
        self.width = width
        self.height = height
        self.color = color 
        self.display = display
        self.velo = 5
        self.x_velo = 0

        self.y_velo = 0
        self.jumping = False
        self.landed = True


        

    def draw(self):
        self.display.blit(self.image, self.rect)


    
    def update(self, surface_list, mob_list, ground_list, spike_list, door_list):
        x_change = 0 
        y_change = 0
        spawn_y = 0
        spawn_x = 0 

        # list of key presses 
        keys = pygame.key.get_pressed()

        # set x_velo based on key presses 
        if keys[pygame.K_a]:
            x_change = -1 * self.velo
        elif keys[pygame.K_d]:
            x_change = self.velo
        
        # jump on space key press
        if keys[pygame.K_SPACE] and not self.jumping and self.landed:
            self.jumping = True
            self.landed = False
            self.y_velo = -15
        if not keys[pygame.K_SPACE]:
            self.jumping = False
            
            

        # Gravity 
        self.y_velo += GRAVITY

        if self.y_velo > 10:
            self.y_velo = 10   # set terminal velocity

        #update change in y 
        y_change += self.y_velo 

        # no double jumps
        if y_change > 0:
            self.landed = False

        # Check for collision
        for surface in surface_list:
            # vertical collision
            if surface.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                # if player is going down
                if self.y_velo  >= 0:
                    y_change = surface.rect.top - self.rect.bottom
                    self.landed = True
                    self.jumping = False
                    self.y_velo = 0
                # if player is going up
                elif self.y_velo <=0:
                    y_change = surface.rect.bottom - self.rect.top
                    self.laned = True
                    self.jumping = False
                    self.y_velo = 0
            
            #horizontal collision
            if surface.rect.colliderect(self.rect.x + x_change, self.rect.y, self.rect.width, self.rect.height):
                
                x_change = 0

            # falling off map
            if self.rect.top >= DISPLAY_HEIGHT + 20:
                spawn_y = self.y_loc - 100
                self.rect.y = spawn_y

                spawn_x = self.x_loc
                self.rect.x = spawn_x

                y_change = 3
        
        for ground in ground_list:

        # vertical collision
            if ground.rect.colliderect(self.rect.x, self.rect.y + y_change, self.rect.width, self.rect.height):
                # if player is going down
                if self.y_velo  >= 0:
                    y_change = ground.rect.top - self.rect.bottom
                    self.landed = True
                    self.jumping = False
                    self.y_velo = 0
                # if player is going up
                elif self.y_velo <=0:
                    y_change = ground.rect.bottom - self.rect.top
                    self.laned = True
                    self.jumping = False
                    self.y_velo = 0

        # hitting enemy 

        for mob in mob_list:
            if mob.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                
                spawn_y = self.y_loc - 100
                self.rect.y = spawn_y

                spawn_x = self.x_loc
                self.rect.x = spawn_x

                y_change = 3

        for spike in spike_list:
            if spike.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                
                spawn_y = self.y_loc - 100
                self.rect.y = spawn_y

                spawn_x = self.x_loc
                self.rect.x = spawn_x

                y_change = 3
        
        lvl_count = 0 
        for door in door_list:

            if door.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                if lvl_count == 0:
                    lvl_count += 1
                elif lvl_count == 1:    
                    lvl_count -= 1
        
        return lvl_count
            

        # update player locations
        self.rect.x += x_change
        self.rect.y += y_change


class Brick():
    def __init__(self, x, y, width, height, color, display, image):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.display = display
        
        
    def draw_brick(self):
        self.display.blit(self.image, self.rect)
        
class Ground():
    def __init__(self, x, y, width, height, color, display, image):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.display = display
        
        
    def draw_ground(self):
        self.display.blit(self.image, self.rect)

class Spike():
    def __init__(self, x, y, width, height, color, display, image):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.display = display
        
        
    def draw_spike(self):
        self.display.blit(self.image, self.rect)
    
class Door():
    def __init__(self, x, y, width, height, color, display, image):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.display = display
        
        
    def draw_door(self):
        self.display.blit(self.image, self.rect)

class Barrier():
    def __init__(self, x, y, width, height, color, display):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color 
        self.display = display
        

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_barrier(self):
        pygame.draw.rect(self.display, self.color, self.rect)

class Enemy():
    def __init__(self, x_loc, y_loc, width, height, color, display, image):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc

        self.x_loc = x_loc
        self.y_loc = y_loc
        self.width = width
        self.height = height
        self.color = color 
        self.display = display
        self.velo = -5
        self.x_change = self.velo
        

        self.on_platform = True
        self.off_platform = False



    def draw_enemy(self):
        self.display.blit(self.image, self.rect)


    def enemy_update(self, surface_list,invis_list):


        for surface in surface_list:

            #horizontal collision
            if surface.rect.colliderect(self.rect.x + self.x_change, self.rect.y, self.rect.width, self.rect.height):
                
                x_change = 0

        # back and forth across platform
        
        for barrier in invis_list:
            
            if barrier.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                
                self.x_change = self.x_change * -1




        self.rect.x += self.x_change






        