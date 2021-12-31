import pygame, sys
from pygame.locals import *
from constants import *

x = 64
class Field():
    def __init__(self):
        self.ground = Rect((x,x/2), (x*13, x*11))
        # brick = (x, x) #bricks' w,h
        self.all_bricks_x = [2*i*64 for i in range(1,7)]
        self.all_bricks_y = [32+(i*2-1)*64 for i in range(1,6)]
    
    def bricks(self):
        bricks = []
        for i in self.all_bricks_x:
            for e in self.all_bricks_y:
                bricks.append(Rect(i, e, 64, 64))
        
        return bricks