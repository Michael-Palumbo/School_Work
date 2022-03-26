import pygame as pg
from Drawable import Drawable

class Rectangle(Drawable):
    def __init__(self, x, y, width, height, color):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
    
    def draw(self, surface):
        pg.draw.rect(surface, self.__color, (self.__x, self.__y, self.__width, self.__height))
        