import pygame, sys
from pygame.locals import *
# from fields import *
# from main import *

def drawing(DISPLAYSURF, place, player, walls, bombs, monsters):
    DISPLAYSURF.fill((225,255,255))
    pygame.draw.rect(DISPLAYSURF, (0,255,0), place.ground)
    # for i in walls:
    #     pygame.draw.rect(DISPLAYSURF, (255,0,0), (i))
    for i in place.wall:
        pygame.draw.rect(DISPLAYSURF, (255,0,0), (i))
    for b in bombs:
        if len(b) == 3:
            # pygame.draw.polygon(DISPLAYSURF, (0,255,255), b[2], 5)#explosión
            for i in b[2]:
                # pygame.draw.line(DISPLAYSURF, (0,255,255), i[0], i[1], 5)
                pygame.draw.rect(DISPLAYSURF, (0,255,255), (i))
        else:
            pygame.draw.circle(DISPLAYSURF, (125, 0, 62), (b[0][0], b[0][1]), 32)
        print('bombini')
    for i in place.brick:
        pygame.draw.rect(DISPLAYSURF, (25,25,25), (i))
    for i in monsters:
        pygame.draw.rect(DISPLAYSURF, i.currently_sprite, (i.rect))
    pygame.draw.rect(DISPLAYSURF, player.currently_sprite, (player.rect))#.position[0], player.position[1], 64,64))