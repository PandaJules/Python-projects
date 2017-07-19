import random
import pygame, sys
import Colours
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
DOT_RADIUS = 10
reds = 5
blues = 10

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dots")


def randomXY():
    randomX = random.randint(0, SCREEN_WIDTH)
    randomY = random.randint(0, SCREEN_HEIGHT)
    return randomX, randomY


def displayDots(canvas):
    global reds, blues
    for i in range(0, reds):
        pygame.draw.circle(canvas, Colours.RED, randomXY(), DOT_RADIUS)
    for i in range(0, blues):
        pygame.draw.circle(canvas, Colours.BLUE, randomXY(), DOT_RADIUS)


def draw(canvas):
    canvas.fill(Colours.BLACK)


def key_press(event):
    if event.key == K_LEFT:
        displayDots(window)
    elif event.key == K_SPACE:
        draw(window)


def play():
    while True:

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                key_press(event)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

play()
