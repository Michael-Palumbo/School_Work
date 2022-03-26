'''
Kyle Cook
KTC53
the Block object
'''


from Drawable import Drawable
import pygame as pg
from pygame import Rect

class Block(Drawable):
	def __init__(self, width, height, x = 0, y = 0, visible=True):
		super().__init__(x, y, visible)
		self.__width = width
		self.__height = height
	
	def get_width(self):
		return self.__width
		
	def set_width(self, w):
		self.__width = w
	
	def get_height(self):
		return self.__h
		
	def set_height(self, h):
		self.__height = h
	
	def get_rect(self):
		return Rect(super().get_position(), (self.__width, self.__height))
		
	def draw(self, surface):
		x, y = super().get_position()
		pg.draw.rect(surface, (0,0,255), (x, y, self.__width, self.__height))