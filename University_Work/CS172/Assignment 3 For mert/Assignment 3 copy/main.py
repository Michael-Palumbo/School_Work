import pygame
from drawables import *
from Block import *
from Ball import *
from Text import *

# Given code, just checks the boundaries to see if they collide
def intersect(rect1, rect2) :
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False

# Create Some constants we can reference
WIDTH = 500
HEIGHT = 500
HORIZON = HEIGHT*4//5
BALLRADUIS = 10

pos1 = [0,0]
pos2 = [0,0]

#Initialize Pygame along with some others entities that we will use
pygame.init()
text = Text("Times New Roman",30,(0,0))
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Assignment 3")
clock = pygame.time.Clock()

ballPosition = (50, HORIZON-BALLRADUIS)

ball = Ball(50, HORIZON-BALLRADUIS, BALLRADUIS)

#Treat the ground like a block
horzBlock = Block((255,255,255),0,HORIZON,WIDTH,HEIGHT-HORIZON)

score = 0

blocks = []

# Create 9 blocks all stacked on each other
for r in range(3):
    for c in range(3):
        blocks.append( Block((0,0,255),WIDTH-100 + 20*r,HORIZON-60 + 20*c,20,20) )


#=================== Game Loop =======================#
while True:

    #Key Inputs >...
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            pos1 = pygame.mouse.get_pos()
        elif (event.type == pygame.MOUSEBUTTONUP):
            pos2 = pygame.mouse.get_pos()
            ball.setDX(pos1[0]-pos2[0])
            ball.setDY(pos1[1]-pos2[1])
            ball.forceFalling(True)


    surface.fill((255,255,255))

    #Drawing >...

    horzBlock.draw(surface)

    for block in blocks:
        block.draw(surface)

    ball.draw(surface)

    #Text >...

    text.draw(surface,score)

    #Collsions >...

    # If we collide with teh ground, bounce the ball, and do a bit of friction
    if(intersect(ball.getRect(), horzBlock.getRect())):
        ball.setFalling(False)
        ball.enactFriction()

    # If the ball is on the ground, cause friction
    if not ball.getFalling():
        ball.enactFriction()

    # Loop through the blcoks, if we collide with them, make them invisible and add score
    for block in blocks:
        if(intersect(ball.getRect(), block.getRect())):
            if block.getVisible():
                score += 1
                block.setVisible(False)


    #Updates >...

    ball.tick()

    #Redraw the screen
    pygame.display.update()

    #Stall Program
    clock.tick(30)
#================== End of Loop ======================#
