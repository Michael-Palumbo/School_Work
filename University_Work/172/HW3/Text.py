'''
Kyle Cook
KTC53
the Text object
'''

from Drawable import Drawable
import pygame as pg
from pygame import Rect

class Text(Drawable):
	def __init__(self, text, font, x = 0, y = 0, visible=True):
		super().__init__(x, y, visible)
		self.__text = text
		self.__font = font
		
	def get_text(self):
		return self.__text
		
	def set_text(self, t):
		self.__text = t
	
	def get_font(self):
		return self.__font
		
	def set_font(self, f):
		self.__font = f
	
	def get_rect(self):
		width, height = pg.font.size(self.__text)
		return Rect((self.__x, self.__y), width, height)
	
	def draw(self, surface):
		pos = super().get_position()
		rendered_text = self.__font.render(self.__text, 1, ((0,0,0)))
		surface.blit(rendered_text, pos)