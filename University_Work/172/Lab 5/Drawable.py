import pygame
import abc

class Drawable(metaclass = abc.ABCMeta):
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y
		
	def getLoc(self):
		return (self.__x, self.__y)
		
	def setLoc(self,p):
		self.__x = p[0]
		self.__y = p[1]

	@abc.abstractmethod
	def draw(self,surface):
		pass


