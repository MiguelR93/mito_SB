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
n = 0 # cuenta frames, EXTREMADAMENTE NECESARIO
bombs = []
# walls = place.walls()

# for i in place.all_walls_x:
#     for e in place.all_walls_y:
#         walls.append(pygame.draw.rect(DISPLAYSURF, (255,0,0), (i, e, 64, 64)))

while gameLoop:
    print(f'\n\n\n\nEl valor de n: {n}\n\n\n\n')
    n += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # if event.type == pygame.KEYDOWN:
    #     print('\n\n\n\n\n\n\n\n\n\n\n\nSe presionó una tecla\n\n\n\n')
    #     player.action(event)

    if event.type == pygame.KEYDOWN:
        print("una bombita")
        if event.key == pygame.K_RETURN:
            bomb = player.place_bomb()
            if bomb == None:
                pass
            else:
                bombs.append([bomb, n])

    player.action(event, (place.wall + place.brick))

    for i in bombs:
        if (len(i) > 2) and (n - i[1] == 5*FPS + player.speed*3):
            # player.bomb_explode(i, n, FPS)
            bombs.remove(i)
        elif n - i[1] == 5*FPS:# probar dejando esta opción y eliminando la otra
            player.bomb_explode(i, n, FPS)
        elif (len(i) > 2) and (n - i[1] > 5*FPS):
            player.bomb_explode(i, n, FPS)

    drawing(DISPLAYSURF, place, player, place, bombs)
    pygame.display.update()
    clock.tick(FPS)