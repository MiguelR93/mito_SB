import pygame, sys
from pygame.locals import *
# from fields import *
# from main import *

def drawing(DISPLAYSURF, place, player):
    DISPLAYSURF.fill((225,255,255))
    pygame.draw.rect(DISPLAYSURF, (0,255,0), place.ground)
    for i in place.all_bricks_x:
        for e in place.all_bricks_y:
            pygame.draw.rect(DISPLAYSURF, (255,0,0), (i, e, 64, 64))
            # print(i,e)
    pygame.draw.rect(DISPLAYSURF, player.currently_sprite, (player.position[0], player.position[1], 64,64))