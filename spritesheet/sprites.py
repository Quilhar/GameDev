import pygame

class SpriteSheet():
    
    def __init__(self, filename):
        self.SpriteSheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height, scale_x = None, scale_y = None):

        #Get the image at (x, y) on the spritesheet
        image = pygame.Surface((width, height))
        image.blit(self.SpriteSheet, (0, 0), (x, y, width, height))

        if scale_x and scale_y:
            image = pygame.transform.scale(image, (width * scale_x, height * scale_y))

        return image

class Player():

    def __init__(self, screen, image_list):
        self.image_list = image_list
        self.player_speed = 10
        self.display = screen
        self.x = 0
        self.y = 0
        self.vy = 0
        self.vx = 0

    def get_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vx = -self.player_speed
            self.img = self.image_list[2]
        if keys[pygame.K_d]:
            self.vx = self.player_speed
            self.img = self.image_list[0]
        if keys[pygame.K_w]:
            self.vy = -self.player_speed
            self.img = self.image_list[1]
        if keys[pygame.K_s]:
            self.vy = self.player_speed
            self.img = self.image_list[3]
        
    def update(self):
        self.get_keys()

        self.x += self.vx
        self.y += self.vy

    def draw(self):

        self.display.blit(self.img, (self.x, self.y))



