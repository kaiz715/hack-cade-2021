import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pacman Game')

#define game variables
tile_size = 50

#load images
bg_img = pygame.image.load('black.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))


class Player():
    def __init__(self, x, y):
        img = pygame.image.load('pacmanyellow.png')
        self.image = pygame.transform.scale(img, (40,40))
        
        self.right = self.image
        self.left = pygame.transform.rotate(self.image, 180)
        self.up = pygame.transform.rotate(self.image, 90)
        self.down = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = 1

    def update(self):
        
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 5
            self.image = self.left
        if key[pygame.K_RIGHT]:
            dx += 5
            self.image = self.right
        if key[pygame.K_UP]:
            dy -= 5
            self.image = self.up
        if key[pygame.K_DOWN]:
            dy += 5
            self.image = self.down
        
        #check for collision
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0

        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy


        screen.blit(self.image, self.rect)


class World():
    def __init__(self, data):

        self.tile_list = []

        wall_img = pygame.image.load('blue.png')
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
            

world_data = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
[1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1],
[1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1],
[1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1],
[1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1],
[1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1],
[1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1],
[1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1],
[1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,1],
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
[1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,1,0,1],
[1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1],
[1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1],
[1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1],
[1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1],
[1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1],
[1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1],
[1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

world = World(world_data)
player = Player(55,55)

run = True
while run:
    
    screen.blit(bg_img, (0,0))

    world.draw()
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()