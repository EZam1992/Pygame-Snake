import pygame
import sys
import random
from pygame.math import Vector2

#definiton of classes 
class SNAKE: 
    def __init__(self):
        self.body = [Vector2(5, 10), 
                     Vector2(6, 10), 
                     Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        
    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (51, 153, 255), snake_rect)

    def move_snake(self): 
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 102, 102), fruit_rect)

pygame.init()

# variables used in the game 
cell_size = 40 
cell_number = 20
framerate = 60
mainColor = (175, 215, 70)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# creating objects for the game 
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock() 

#create the objects 
fruit = FRUIT()
snake = SNAKE()

#game loop
while True: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)            


    screen.fill(mainColor)
    snake.draw_snake()
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(framerate)
    