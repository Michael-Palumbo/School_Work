import pygame as pg
from Drawable import Drawable

class Snowflake(Drawable):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def draw(self, surface):
        WHITE = (255, 255, 255)
        pg.draw.line(surface, WHITE, (self.__x-5, self.__y), (self.__x+5, self.__y))
        pg.draw.line(surface, WHITE, (self.__x, self.__y-5), (self.__x, self.__y+5))
        pg.draw.line(surface, WHITE, (self.__x-5, self.__y-5), (self.__x+5, self.__y+5))
        pg.draw.line(surface, WHITE, (self.__x-5, self.__y+5), (self.__x+5, self.__y-5))
    
    def setY(self, y):
        self.__y = y
    def getY(self):
        return self.__y
        
