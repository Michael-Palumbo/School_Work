import pygame
import abc
import random

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

class Rectangle(Drawable):

	def __init__(self, color = (0,0,0), x = 0, y = 0, width=0, height=0):
		super().__init__(x,y)
		self.__color = color
		self.__width = width
		self.__height = height
		self.__rate = 0

	def draw(self, surface):
		x, y = super().getLoc()
		pygame.draw.rect(surface,self.__color,[x,y,self.__width,self.__height])

	# Just for fun, not needed
	def update(self):
		self.__color = ( (self.__rate % 256), (self.__rate+85) % 256, (self.__rate+175) %256 )
		self.__rate += 1

class SnowFlake(Drawable):

	def __init__(self, x=0,y=0, max_y=10000):
		super().__init__(x,y)
		self.__dy = random.randint(1,4)
		self.__max_y = max_y
		self.__color = (255,255,255)

	def draw(self,surface):
		x, y = super().getLoc()
		pygame.draw.line(surface, self.__color, [x-5,y], [x+5,y])
		pygame.draw.line(surface, self.__color, [x,y-5], [x,y+5])
		pygame.draw.line(surface, self.__color, [x-5,y-5], [x+5,y+5])
		pygame.draw.line(surface, self.__color, [x-5,y+5], [x+5,y-5])

	def update(self):
		x, y = super().getLoc()
		if(y+self.__dy > self.__max_y):
			return
		super().setLoc([x,y+self.__dy])
