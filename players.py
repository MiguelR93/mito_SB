import pygame, sys
from pygame.locals import *
# from fields import *
# from drawing import *
# from players import *

# pygame.init()
class Player():
    # # def __init__(self, currently_sprite, front, front_right, front_left, back, back_right, back_left, right, right_right, right_left, left, left_right, left_left, pos_x, pos_y):
    #     # sprites:------
    #     self.currently_sprite = currently_sprite
    #     self.front = front
    #     self.front_right = front_right 
    #     self.front_left = front_left 
    #     self.back = back
    #     self.back_right = back_right
    #     self.back_left = back_left
    #     self.right = right
    #     self.right_right = right_right
    #     self.right_left = right_left
    #     self.left = left
    #     self.left_right = left_right
    #     self.left_left = left_left
    def __init__(self):
        # sprites:------
        self.front = (255,255,255)
        self.front_right = (158,0,45) 
        self.front_left = (0,81,45) 
        self.back = (185,185,0)
        self.back_right = (18,81,45)
        self.back_left = (18,8,45)
        self.right = (0,0,0)
        self.right_right = (58,81,45)
        self.right_left = (158,10,45)
        self.left = (0,0,255)
        self.left_right = (48,81,45)
        self.left_left = (158,11,45)
        self.currently_sprite = self.front
        # position:
        self.position = [64, 32]
        self.movement_frames = 0
        self.movement_direction = None
        self.rect = Rect(self.position[0], self.position[1], 64, 64)
        self.speed = 10
    
    def place_bomb(self):
        if self.movement_frames == 0:
            bomb = [int(self.position[0]+32), int(self.position[1]+32)]
            return bomb
        else:
            return None
    
    def act_rect(self):
        self.rect[0] = self.position[0]
        self.rect[1] = self.position[1]
    
    def action(self, event, walls):
        if self.movement_frames == 0:
            if event.type == pygame.KEYDOWN:
                self.movement(event, walls)
        else:
            self.movement_animation(walls)
    
    def movement_animation(self, walls):
        self.movement_frames += 1
        if self.movement_frames == self.speed:
            if self.movement_direction == 'right':
                self.position[0] += 32
            elif self.movement_direction == 'left':
                self.position[0] -= 32

            if self.movement_direction == 'down':
                self.position[1] += 32
            elif self.movement_direction == 'up':
                self.position[1] -= 32
        elif self.movement_frames == self.speed*2:
            if self.movement_direction == 'right':
                self.position[0] += 32
            elif self.movement_direction == 'left':
                self.position[0] -= 32

            if self.movement_direction == 'down':
                self.position[1] += 32
            elif self.movement_direction == 'up':
                self.position[1] -= 32
            self.movement_frames = 0
            self.movement_direction = None
        self.act_rect()
    
    def collide(self, walls, direction):
        values = None # element, adition, subtraction
        if direction == 'right':
            values = (0, 1, -1)
        elif direction == 'left':
            values = (0, -1, 1)
        elif direction == 'up':
            values = (1, -1, 1)
        elif direction == 'down':
            values = (1, 1, -1)
        self.position[values[0]] += 64*values[1]
        self.act_rect()
        # futuro:
        for i in walls:
            if self.rect.colliderect(i):
                # self.position[0] -= 64
                self.position[values[0]] += 64*values[2]
                self.act_rect()
                return True
        # self.position[0] -= 64
        self.position[values[0]] += 64*values[2]
        self.act_rect()

    def movement(self, event, walls):
        if event.key == pygame.K_LEFT:
            if self.currently_sprite != self.left:
                self.currently_sprite = self.left
            elif self.position[0] == 64:
                pass
            elif self.collide(walls, 'left') == True:
                pass
            else: #aquí debería acceder a una animación
                # self.position[0] -= 64
                self.movement_direction = 'left'
                self.movement_animation(walls)
        if (event.key == pygame.K_RIGHT):
            if self.currently_sprite != self.right:
                self.currently_sprite = self.right
                print("\n\n\nEran diferentes")
            # self.position[0] += 64
            elif self.position[0] == 64*13:
                pass
            elif self.collide(walls, 'right') == True:
                pass
            else: #aquí debería acceder a una animación
                # self.position[0] += 64
                self.movement_direction = 'right'
                self.movement_animation(walls)
        if event.key == pygame.K_DOWN:
            # self.position[0] -= 64
            if self.currently_sprite != self.front:
                self.currently_sprite = self.front
            elif self.position[1] == 64*10+32:
                pass
            elif self.collide(walls, 'down') == True:
                pass
            else: #aquí debería acceder a una animación
                # self.position[1] += 64
                self.movement_direction = 'down'
                self.movement_animation(walls)
        if event.key == pygame.K_UP:
            if self.currently_sprite != self.back:
                self.currently_sprite = self.back
                print("\n\n\nEran diferentes")
            # self.position[0] += 64
            elif self.position[1] == 32:
                pass
            elif self.collide(walls, 'up') == True:
                pass
            else: #aquí debería acceder a una animación
                # self.position[1] -= 64
                self.movement_direction = 'up'
                self.movement_animation(walls)