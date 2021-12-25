import pygame, sys
from pygame.locals import *
from fields import *
from drawing import *

pygame.init()
#15*12
x = 64
DISPLAYSURF = pygame.display.set_mode((15*x,12*x))
pygame.display.set_caption('Mito Super Bomberman!')
clock = pygame.time.Clock()
gameLoop = True
place = Field()
while gameLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        drawing(DISPLAYSURF, place)
        # DISPLAYSURF.fill((225,255,255))
        # pygame.draw.rect(DISPLAYSURF, (0,255,0), place.ground)
        # for i in place.all_bricks_x:
        #     for e in place.all_bricks_y:
        #         pygame.draw.rect(DISPLAYSURF, (255,0,0), (i, e, 64, 64))
        #         print(i,e)
        pygame.display.update()
        clock.tick(60)