import pygame
import random
from rectangle import Rectangle
from snowflake import Snowflake
from snowman import Snowman

pygame.init()
surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Lab 5')

snowflakes = []

grass = Rectangle(0, 200, 400, 200, (0, 255, 0))
snowman = Snowman(300, 100)

while True: 
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
    newSnowflake = Snowflake(random.randint(0, 400), 0)        
    snowflakes.append(newSnowflake)
    
    surface.fill((204, 229, 255))
    grass.draw(surface)
    snowman.draw(surface)
    for snowflake in snowflakes:
        snowflake.draw(surface)
        snowflake.setY(snowflake.getY()+random.randint(0,2))
        
    pygame.display.update()