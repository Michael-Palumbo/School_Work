'''
Kyle Cook
KTC53
The main class for running the game
'''


import pygame
import random
from Text import Text
from Block import Block
from Ball import Ball

	
def intersect(rect1, rect2) :
	if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y) :
		return True
	return False


pygame.init()
surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Homework 3')

score = 0

blocks = []

floor = Block(400, 200, 0, 200)

blocks.append(Block(15, 15, 40, 186))
blocks.append(Block(15, 15, 60, 186))
blocks.append(Block(15, 15, 80, 186))
blocks.append(Block(15, 15, 100, 186))
blocks.append(Block(15, 15, 120, 186))
blocks.append(Block(15, 15, 140, 186))

ball = Ball(5, 50, 195)

myfont = pygame.font.SysFont('monospace', 32)
text = Text('Score:' +str(score), myfont)

dt = 0.1
g = 6.67
R = 0.7
eta = 0.5
yv = 0
xv = 0
xi = 0
yi = 0
xf = 0
yf = 0

while True: 
	for event in pygame.event.get():
		if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
			pygame.quit()
			exit()
		elif(event.type == pygame.MOUSEBUTTONDOWN):
			#gets x and y from position set to x initial and y initial
			xi = pygame.mouse.get_pos()[0]
			yi = pygame.mouse.get_pos()[1]
		elif (event.type == pygame.MOUSEBUTTONUP):
			#gets x and y from position set to x final and y final
			xf = pygame.mouse.get_pos()[0]
			yf = pygame.mouse.get_pos()[1]
			#find x and y velocities from difference between xf/xi and yf/yi
			xv = (xf-xi)
			yv = (yf-yi)
			

	yv = -R * yv
	xv = eta * xv
	
	ball.setX(int(xi+(dt*xv)))
	ball.setY(int(yi+(dt*yv)))
	
	surface.fill((204, 229, 255))
	floor.draw(surface)
	ball.draw(surface)
	text.draw(surface)
	
	for block in blocks:
		block.draw(surface)
		if intersect(ball.get_rect(), block.get_rect()):
			score += 1
			text.set_text('Score:' +str(score))
			blocks.remove(block)
		
	pygame.display.update()