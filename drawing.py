import pygame, sys
from pygame.locals import *
# from fields import *
# from main import *

def drawing(DISPLAYSURF, place, player, walls, bombs):
    DISPLAYSURF.fill((225,255,255))
    pygame.draw.rect(DISPLAYSURF, (0,255,0), place.ground)
    # for i in walls:
    #     pygame.draw.rect(DISPLAYSURF, (255,0,0), (i))
    for i in place.wall:
        pygame.draw.rect(DISPLAYSURF, (255,0,0), (i))
    for b in bombs:
        pygame.draw.circle(DISPLAYSURF, (125, 0, 62), (b[0][0], b[0][1]), 32)
        print('bombini')
    for i in place.brick:
        pygame.draw.rect(DISPLAYSURF, (25,25,25), (i))
    pygame.draw.rect(DISPLAYSURF, player.currently_sprite, (player.position[0], player.position[1], 64,64))