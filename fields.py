import pygame, sys
from pygame.locals import *
from constants import *
import random

x = 64
class Field():
    def __init__(self):
        self.ground = Rect((x,x/2), (x*13, x*11))
        # wall = (x, x) #walls' w,h
        self.all_walls_x = [2*i*64 for i in range(1,7)]
        self.all_walls_y = [32+(i*2-1)*64 for i in range(1,6)]
        self.wall = self.walls()
        self.brick = self.bricks('bricks')
        self.monsters = self.bricks('monsters')
    
    def walls(self):
        walls = []
        for i in self.all_walls_x:
            for e in self.all_walls_y:
                walls.append(Rect(i, e, 64, 64))
        
        return walls
    
    def bricks(self, thing):
        """
        1. Create posible position (x and y)
        2. Chose a specific number of them
        3. Place bricks
        """
        q = None
        if thing == 'bricks':
            q = 20
        elif thing == 'monsters':
            q = 5
        
        bricks = []
        x = [(i*2+1)*64 for i in range(1,6)] # 3-11
        y = [(i)*64+32 for i in range(11)] # 1-11
        for i in x:
            for e in y:
                # bricks.append(Rect(i, e, 64, 64))
                bricks.append((i, e, 64, 64))
        x2 = [(i)*64 for i in range(1,14)] # 3-11
        y2 = [(i*2)*64+32 for i in range(1,5)] # 1-11
        for i in x2:
            for e in y2:
                # bricks.append(Rect(i, e, 64, 64))
                bricks.append((i, e, 64, 64))
        x3 = [1*64,13*64] # 1,13
        y3 = [(i*2+1)*64+32 for i in range(1,4)] # 3,5,7
        for i in x3:
            for e in y3:
                # bricks.append(Rect(i, e, 64, 64))
                bricks.append((i, e, 64, 64))
        x4 = [(i*2)*64 for i in range(2,6)] # 4,6,8,10
        y4 = [0*64+32,10*64+32] # 0,10
        for i in x4:
            for e in y4:
                # bricks.append(Rect(i, e, 64, 64))
                bricks.append((i, e, 64, 64))

        
        bricks = list(set(bricks))
        if thing == 'monsters':
            for i in self.brick:
                bricks.remove(i)
        final_bricks = []
        while len(final_bricks) < q:
            final_bricks.append(random.choice(bricks))
            final_bricks = list(set(final_bricks))
        return final_bricks