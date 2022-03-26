import pygame as pg
from Drawable import Drawable

class Snowman(Drawable):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def draw(self, surface):
        man = pg.image.load('snowman.png')
        surface.blit(man, (self.__x, self.__y))