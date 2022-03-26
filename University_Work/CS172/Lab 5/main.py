import pygame
import random

from Drawable import *

WIDTH, HEIGHT = 1000, 600
Horizon = HEIGHT*5/8

pygame.init()
surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Winter as Came and Went")
fpsclock = pygame.time.Clock()

Sky = Rectangle( (0,0,255), 0, 0, WIDTH, HEIGHT)
Grass = Rectangle( (0,255,0), 0, Horizon, WIDTH, HEIGHT*3/8)

snow_flakes = []

is_pause = False

while True:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
        elif(event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE):
            is_pause = not is_pause


    surface.fill( (0,0,0) )

    Sky.draw(surface)
    Grass.draw(surface)

    if not is_pause:
        x = random.randint(0,WIDTH)
        max_y = random.randint(HEIGHT*5/8,HEIGHT)
        snow_flakes.append(SnowFlake(x,0,max_y))

    for sn in snow_flakes:
        sn.draw(surface)

    if not is_pause:
        for sn in snow_flakes:
            sn.update()

    Sky.update()

    pygame.display.update()
    fpsclock.tick(30)
