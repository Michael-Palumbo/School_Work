'''
Kyle Cook
KTC53
the Ball object
'''


from Drawable import Drawable
import pygame as pg
from pygame import Rect

class Ball(Drawable):
	def __init__(self, r, x = 0, y = 0, visible=True):
		super().__init__(x, y, visible)
		self.__r = r
	
	def get_r(self):
		return self.__r
		
	def set_r(self, r):
		self.__r = r
	
	def get_rect(self):
		x, y = super().get_position()
		return Rect((x-self.__r, y-self.__r), (self.__r*2, self.__r*2))
	
	def setX(self, x):
		xo, y = super().get_position()
		super().set_position((x, y))
		
	def setY(self, y):
		x, yo = super().get_position()
		super().set_position((x, yo))
	
	def getX(self):
		x, yo = super().get_position()
		return x
		
	def getY(self):
		xo, y = super().get_position()
		return y
	
	def draw(self, surface):
		x, y = super().get_position()
		pg.draw.circle(surface, (255, 0, 0), (x, y), self.__r)