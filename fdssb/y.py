import pygame, os

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

win = pygame.display
d = win.set_mode((1200, 600))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 2

    def draw(self):
        pygame.draw.rect(d, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed


class Bullet:
    def __init__(self, x, y):
        self.radius = 10
        self.speed = 10
        self.x = x
        self.y = y

    def update(self):
        self.y -= self.speed#
    
    def draw(self):
        pygame.draw.circle(d, (255, 0, 0), (self.x, self.y), self.radius)


bullets = []
p = Player(600, 500, 50, 30) 

run = True
while run:
    clock.tick(100)
        
    # handel events
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            run = False
        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(p.x+p.width//2, p.y))

    # update objects
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_LEFT]:
        p.move_left()
    if keys[pygame.K_RIGHT]:
        p.move_right()
    for b in bullets:
        b.update()
        if b.y < 0:
            bullets.remove(b)

    # clear display
    d.fill((98, 98, 98))

    # draw scene
    for b in bullets:
        b.draw()
    p.draw()

    # update display
    win.update()