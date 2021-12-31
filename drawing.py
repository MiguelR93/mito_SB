import pygame, sys
from pygame.locals import *
# from fields import *
# from main import *

def drawing(DISPLAYSURF, place, player, bricks):
    DISPLAYSURF.fill((225,255,255))
    pygame.draw.rect(DISPLAYSURF, (0,255,0), place.ground)
    for i in bricks:
        pygame.draw.rect(DISPLAYSURF, (255,0,0), (i))
    pygame.draw.rect(DISPLAYSURF, player.currently_sprite, (player.position[0], player.position[1], 64,64))