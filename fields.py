import pygame, sys
from pygame.locals import *
from constants import *

x = 64
class Field():
    def __init__(self):
        self.ground = Rect((x,x/2), (x*13, x*11))
        # wall = (x, x) #walls' w,h
        self.all_walls_x = [2*i*64 for i in range(1,7)]
        self.all_walls_y = [32+(i*2-1)*64 for i in range(1,6)]
    
    def walls(self):
        walls = []
        for i in self.all_walls_x:
            for e in self.all_walls_y:
                walls.append(Rect(i, e, 64, 64))
        
        return walls