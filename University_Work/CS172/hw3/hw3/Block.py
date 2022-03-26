import pygame
from Drawable import *
class Block(Drawable):
    def __init__(self, x, y, width, height):
        super().__init__(x,y)
        self.__width = width
        self.__height = height
        self.__color = (0,0,250)

    def draw(self, surface):
        if self.getVisible():
            pygame.draw.rect(surface, (0,0,0), (self.getX(), self.getY(), self.__width, self.__height))
            pygame.draw.rect(surface, self.__color, (self.getX()+1, self.getY()+1, self.__width-2, self.__height-2))

    def get_rect(self):
        return pygame.Rect(self.getX(),self.getY(),self.__width, self.__height)
