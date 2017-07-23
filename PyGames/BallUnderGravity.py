import pygame, sys
from pygame import *
import random


pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ball Under Gravity')

BALL_RADIUS = 10
GRAVITY = [0, 7]
ballrect = pygame.Rect(SCREEN_WIDTH/2, 10, BALL_RADIUS, BALL_RADIUS)


while True:

    # make screen black
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ballrect = ballrect.move(GRAVITY)

    if ballrect.bottom > SCREEN_HEIGHT-BALL_RADIUS:
        ballrect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

    pygame.draw.circle(screen, (0, 10, 255), ballrect.center, BALL_RADIUS)
    pygame.display.update()
