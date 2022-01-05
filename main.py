import pygame, sys
from pygame.locals import *
from fields import *
from drawing import *
from monsters import *
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
monsters = []

for a,i in enumerate(place.monsters):
    b = Monster1(i)
    # i.initial_position(place.brick)
    monsters.append(b)
walls = place.walls()

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

    # detect explotion with bricks:
    for i in bombs:
        for b in place.brick:
            if (len(i) == 3) and (Rect(b).colliderect(i[2][0])):
                print("abajo!")
                place.brick.remove(b)
            elif (len(i) == 3) and (Rect(b).colliderect(i[2][1])):
                print("abajo!")
                place.brick.remove(b)
        for b in monsters:
            if (len(i) == 3) and (Rect(b).colliderect(i[2][0])):
                print("abajo!")
                monsters.remove(b)
            elif (len(i) == 3) and (Rect(b).colliderect(i[2][1])):
                print("abajo!")
                monsters.remove(b)

    for i in bombs:
        if (len(i) == 3) and (n - i[1] == 2.8*FPS):
            # player.bomb_explode(i, n, FPS)
            bombs.remove(i)
        elif (len(i) == 2) and (n - i[1] == 2.5*FPS):# probar dejando esta opción y eliminando la otra
            player.bomb_explode(i, n, FPS)

    drawing(DISPLAYSURF, place, player, place, bombs, monsters)
    pygame.display.update()
    clock.tick(FPS)