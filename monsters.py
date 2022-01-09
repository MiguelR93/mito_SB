import pygame, sys
from pygame.locals import *

class Monster1():
    def __init__(self, coordinate):
        # sprites:------
        self.front = (111,111,111)
        self.front_right = (118,1,31) 
        self.front_left = (1,81,31) 
        self.back = (181,181,1)
        # steps:
        self.back_right = (18,81,31)
        self.back_left = (18,8,31)
        self.right = (1,1,1)
        self.right_right = (18,81,31)
        self.right_left = (118,11,31)
        self.left = (1,1,111)
        self.left_right = (38,81,31)
        self.left_left = (118,11,31)
        self.currently_sprite = self.front
        # position:
        self.position = [coordinate[0], coordinate[1]]
        self.movement_frames = 0
        self.movement_direction = None
        self.rect = Rect(self.position[0], self.position[1], 64, 64)
        self.speed = 10
        self.bomb_power = 3

    def act_rect(self):
        self.rect[0] = self.position[0]
        self.rect[1] = self.position[1]
    
    def action(self, event, walls):
        if self.movement_frames == 0:
            # if event.type == pygame.KEYDOWN:
            #     self.movement(event, walls)
            self.movement(event, walls)
        else:
            self.movement_animation(walls)

    def movement(self, event, walls):
        # if event.key == pygame.K_LEFT:
        if event == 0:
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
        # if (event.key == pygame.K_RIGHT):
        if event == 1:
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
        # if event.key == pygame.K_DOWN:
        if event == 2:
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
        # if event.key == pygame.K_UP:
        if event == 3:
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