from Drawable import Drawable
from Ball import Ball
from Block import Block
from text import Text
import pygame

# Thanks for the method
def intersect(rect1, rect2):
    return (rect1.x < rect2.x + rect2.width) and(rect1.x + rect1.width > rect2.x) and(rect1.y < rect2.y + rect2.height) and(rect1.height + rect1.y > rect2.y)

if __name__ == "__main__":

    # Some references to remember
    WIDTH, HEIGHT, HORIZON = 500,500,400

    # Initialize Pygames, along with graphics and items
    pygame.init()
    surface = pygame.display.set_mode((500,500))
    clock = pygame.time.Clock()
    text = Text(0,0)
    ball = Ball(50,385,15)
    blocks = []
    for row in range(3):
        for col in range(3):
            blocks.append(Block(400+row*25,325+col*25,25,25))

    # To remember mouse presses
    loc1 = None
    loc2 = None

    score = 0

    while True:

        # Drawing the jawns
        surface.fill((0, 240, 20))

        pygame.draw.line(surface,(0,0,0),(0,HORIZON),(WIDTH,HORIZON))
        ball.draw(surface)
        for block in blocks:
            block.draw(surface)
        text.draw(surface,score)

        # Check Collisions with the ground, reflect dy if ball is under line
        if ball.getY()+ball.get_r()+ball.get_dy()*ball.get_dt() > HORIZON:
            ball.bounce()
            ball.friction()

        # Check collision if ball it's box
        for block in blocks:
            if block.getVisible():
                if intersect(ball.get_rect(), block.get_rect()):
                    block.setVisible(False)
                    score += 1

        # Updates Ball's position
        ball.update()

        #Stalls Game so it isn't super fast
        clock.tick(30)

        # Button Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                loc1 = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                loc2 = pygame.mouse.get_pos()
                ball.set_dx(loc2[0]-loc1[0])
                ball.set_dy(loc2[1]-loc1[1])
                ball.set_falling(True)

        # Redraws the screen
        pygame.display.update()
