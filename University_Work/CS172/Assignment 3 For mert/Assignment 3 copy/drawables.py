import pygame
import abc

class drawables(metaclass = abc.ABCMeta):

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__visible = True

    def setVisible(self, change):
        self.__visible = change

    def getVisible(self):
        return self.__visible

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def getRect(self):
        pass
