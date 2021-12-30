import pygame, sys
from pygame.locals import *
from fields import *
from drawing import *
from players import *
from constants import *

pygame.init()
#15*12
x = 64
DISPLAYSURF = pygame.display.set_mode((15*x,12*x))
pygame.display.set_caption('Mito Super Bomberman!')
clock = pygame.time.Clock()
gameLoop = True
place = Field()
player = Player()
n = 0
while gameLoop:
    print(f'\n\n\n\nEl valor de n: {n}\n\n\n\n')
    n += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        print('\n\n\n\n\n\n\n\n\n\n\n\nSe presionó una tecla\n\n\n\n')
        player.action(event)
        # if event.key == pygame.K_LEFT:
        #     # player.position[0] -= 64
        #     if player.currently_sprite != player.left:
        #         player.currently_sprite = player.left
        #     elif player.position[0] == 64:
        #         pass
        #     else: #aquí debería acceder a una animación
        #         player.position[0] -= 64
        # if event.key == pygame.K_RIGHT:
        #     if player.currently_sprite != player.right:
        #         player.currently_sprite = player.right
        #         print("\n\n\nEran diferentes")
        #     # player.position[0] += 64
        #     elif player.position[0] == 64*13:
        #         pass
        #     else: #aquí debería acceder a una animación
        #         player.position[0] += 64
        # if event.key == pygame.K_DOWN:
        #     # player.position[0] -= 64
        #     if player.currently_sprite != player.front:
        #         player.currently_sprite = player.front
        #     elif player.position[1] == 64*10+32:
        #         pass
        #     else: #aquí debería acceder a una animación
        #         player.position[1] += 64
        # if event.key == pygame.K_UP:
        #     if player.currently_sprite != player.back:
        #         player.currently_sprite = player.back
        #         print("\n\n\nEran diferentes")
        #     # player.position[0] += 64
        #     elif player.position[1] == 32:
        #         pass
        #     else: #aquí debería acceder a una animación
        #         player.position[1] -= 64
    # player.action()
    drawing(DISPLAYSURF, place, player)
    pygame.display.update()
    clock.tick(FPS)