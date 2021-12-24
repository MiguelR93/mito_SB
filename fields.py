import pygame, sys
from pygame.locals import *
x = 64
class Field():
    def __init__(self):
        self.ground = Rect((x,x/2), (x*13, x*11))
        # brick = (x, x) #bricks' w,h
        self.all_bricks_x = [2*i*64 for i in range(1,7)]
        self.all_bricks_y = [32+(i*2-1)*64 for i in range(1,6)]