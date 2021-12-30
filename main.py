import pygame, sys
from pygame.locals import *
from fields import *
from drawing import *
from players import *
from constants import *

pygame.init()
#15*12
x = 64
DISPLAYSURF = pygame.display.set_mode((15*x,12*x))
pygame.display.set_caption('Mito Super Bomberman!')
clock = pygame.time.Clock()
gameLoop = True
place = Field()
player = Player()
n = 0
while gameLoop:
    print(f'\n\n\n\nEl valor de n: {n}\n\n\n\n')
    n += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # if event.type == pygame.KEYDOWN:
    #     print('\n\n\n\n\n\n\n\n\n\n\n\nSe presionó una tecla\n\n\n\n')
    #     player.action(event)
    player.action(event)

    drawing(DISPLAYSURF, place, player)
    pygame.display.update()
    clock.tick(FPS)