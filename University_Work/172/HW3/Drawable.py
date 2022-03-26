'''
Kyle Cook
KTC53
the Base Class for Drawable objects object
'''


import abc
import pygame as pg

class Drawable(metaclass = abc.ABCMeta):
	def __init__(self, x = 0, y = 0, visible=True):
		self.__x = x
		self.__y = y
		self.__visible = visible

	def set_visible(self, v):
		self.__visible = values
		
	def get_visible(self):
		return self.__visible
		
	def get_position(self):
		return (self.__x, self.__y)

	def set_position(self, point):
		self.__x = point[0]
		self.__y = point[1]

	@abc.abstractmethod
	def draw(self, surface):
		pass

	@abc.abstractmethod
	def get_rect(self):
		pass