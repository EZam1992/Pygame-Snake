import pygame
import sys

#variables used in the game 
WINDOWHEIGHT, WINDOWLENGTH = 1000, 1000
framerate = 60
mainColor = (175, 215, 70)

#creating objects for the game 
screen = pygame.display.set_mode((WINDOWHEIGHT, WINDOWLENGTH))
clock = pygame.time.Clock() 
test_screen = pygame.Surface((200, 200))

test_screen.fill(pygame.Color('blue'))


while True: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(mainColor)
    screen.blit(test_screen, (200, 300))
    clock.tick(framerate)
    pygame.display.update()