import pygame
import sys
import random
from pygame.math import Vector2

#definiton of classes 
class SNAKE: 
    def __init__(self):
        self.body = [Vector2(5, 10), 
                     Vector2(4, 10), 
                     Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        
    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (51, 153, 255), snake_rect)

    def move_snake(self):

        if self.new_block: 
            body_copy = self.body[:] 
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self): 
        self.new_block = True


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 102, 102), fruit_rect)

    def randomize(self):

        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:

    def __init__(self):
        self.snake = SNAKE() 
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_colission()
        self.check_fail()
    
    def draw_elements(self): 
        self.fruit.draw_fruit()
        self.snake.draw_snake() 
    
    def check_colission(self): 
        if self.fruit.pos == self.snake.body[0]:
            #reposition the fruit 
            self.fruit.randomize()
            #add another block to the snake
            self.snake.add_block()
    
    def check_fail(self):

        # did the snake hit the walls?
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        # did the snake hit itself? 
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        pygame.quit()
        sys.exit()




    
#initialize pygame modules 
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

#create the main game object
main_game = MAIN()

#game loop
while True: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)            


    screen.fill(mainColor)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(framerate)
    