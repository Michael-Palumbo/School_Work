from Drawable import Drawable
from Ball import Ball
from Block import Block
from text import Text
import pygame

def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and(rect1.x + rect1.width > rect2.x) and(rect1.y < rect2.y + rect2.height) and(rect1.height + rect1.y > rect2.y) :
        return True
    return False

if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((500,500))
    clock = pygame.time.Clock()
    ball = Ball(50,385,15)
    blocks = []
    for row in range(3):
        for col in range(3):
            blocks.append(Block(400+row*25,325+col*25,25,25))

    loc1 = (0,0)
    loc2 = (0,0)
    text = Text(0,0)
    score = 0
    while True:
        surface.fill((255, 192, 203))
        pygame.draw.line(surface,(0,0,0),(0,400),(500,400))
        ball.draw(surface)
        for block in blocks:
            block.draw(surface)
        text.draw(surface,score)
        pygame.display.update()

        if ball.getY()+ball.get_r()+ball.get_dy()*ball.get_dt() > 400:
            ball.bounce()
            ball.friction()

        if not ball.get_falling():
            ball.friction()

        for block in blocks:
            if block.getVisible():
                if intersect(ball.get_rect(), block.get_rect()):
                    block.setVisible(False)
                    score += 1

        ball.update()
        clock.tick(30)

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
