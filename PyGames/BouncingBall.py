import pygame, sys
from pygame import *

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bouncing Ball')

BALL_RADIUS = 20
ball_speed = [2, 3]
ballrect = pygame.Rect(0, 0, BALL_RADIUS, BALL_RADIUS)


while True:

    # make screen black
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ballrect = ballrect.move(ball_speed)
    if ballrect.left < 0 or ballrect.right > SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ballrect.top < 0 or ballrect.bottom > SCREEN_HEIGHT:
        ball_speed[1] = -ball_speed[1]

    pygame.draw.circle(screen, (255, 0, 0), ballrect.center, BALL_RADIUS)
    pygame.display.update()
