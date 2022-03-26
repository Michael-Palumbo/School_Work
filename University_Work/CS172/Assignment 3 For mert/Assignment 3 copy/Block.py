from drawables import *
import pygame

class Block(drawables):

    def __init__(self, color, x, y, width, height):
        super().__init__(x,y)
        self.__width = width
        self.__height = height
        self.__color = color

    def getWidth(self):
        return self.__width

    def draw(self, surface):
        if self.getVisible():
            # Draws a big black square and then a slightly smaller on inside
            pygame.draw.rect(surface, (0,0,0), [self.getX(),self.getY(), self.__width, self.__height])
            pygame.draw.rect(surface, self.__color, [self.getX()+1,self.getY()+1, self.__width-2, self.__height-2])

    def getRect(self):
        return pygame.Rect(self.getX(),self.getY(),self.__width,self.__height)
