# Name: Michael Palumbo
# Section:
# Purpose: Create a game with a ball capable of moving and colliding with blocks

import pygame
from drawables import *

# Simple Intersection, used to test if ball hit a block
def intersect(rect1, rect2) :
    return (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y)

# Reset the game on press
def resetGame():
    for block in blocks:
        block.setVisible(True)
    ball.setX(ballPosition[0])
    ball.setY(ballPosition[1])
    ball.setDx(0)
    ball.setDy(0)

# Some Varibales to remember
WIDTH, HEIGHT = 500, 500
HORIZON = HEIGHT*4//5
BALLRADUIS = 10

pos1 = None
pos2 = None

# Just the simple Pygame Initialized stuff
pygame.init()
text = Text("Comic Sans",30,(0,0))
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Assignment 3")
clock = pygame.time.Clock()

ballPosition = (50, HORIZON-BALLRADUIS)

ball = Ball(50, HORIZON-BALLRADUIS, BALLRADUIS)

score = 0

blocks = []

for r in range(3):
    for c in range(3):
        blocks.append( Rectangle((0,0,255),WIDTH-100 + 20*r,HORIZON-60 + 20*c,20,20) )


#<=================== Game Loop =======================>
while True:

    #<----Key Input---->
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
        elif(event.type == pygame.KEYDOWN and (event.__dict__['key'] == pygame.K_SPACE or event.__dict__['key'] == pygame.K_r)):
            resetGame()
            score = 0
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            pos1 = pygame.mouse.get_pos()
        elif (event.type == pygame.MOUSEBUTTONUP):
            pos2 = pygame.mouse.get_pos()
            ball.setDx(pos1[0]-pos2[0])
            ball.setDy(pos1[1]-pos2[1])
            ball.setFalling(True)


    surface.fill((255,255,255))

    #<----Drawing---->

    # Horizon Block
    pygame.draw.line(surface,(0,0,0),(0,HORIZON),(WIDTH,HORIZON))

    for block in blocks:
        block.draw(surface)

    ball.draw(surface)

    #<----Text---->

    text.draw(surface,score)

    #<----Collsions---->

    if ball.getY() + ball.getRadius() - ball.getDy() > HORIZON:
        ball.bounce(False)
        ball.Friction()

    for block in blocks:
        # Don't loop through blocks that arn't visible
        if block.getVisible():
            if(intersect(ball.getRect(), block.getRect())):
                score += 1
                block.setVisible(False)


    #<----Updates---->

    ball.tick()

    pygame.display.update()
    clock.tick(30)
#<================== End of Loop ======================>
