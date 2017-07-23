import random
import pygame, sys
import Colours
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCALE = 60

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dots")

img1 = pygame.image.load("/Users/Julia/Desktop/candle.png")
i1 = pygame.transform.scale(img1, (SCALE, SCALE))
img2 = pygame.image.load("/Users/Julia/Desktop/milk.png")
i2 = pygame.transform.scale(img2, (SCALE, SCALE))
img3 = pygame.image.load("/Users/Julia/Desktop/cheese.png")
i3 = pygame.transform.scale(img3, (SCALE, SCALE))
img4 = pygame.image.load("/Users/Julia/Desktop/eye.png")
i4 = pygame.transform.scale(img4, (SCALE, SCALE))



def randomXY():
    randomX = random.randint(0, SCREEN_WIDTH - SCALE)
    randomY = random.randint(0, SCREEN_HEIGHT - SCALE)
    return randomX, randomY


def displaySymbols():
    window.blit(i1, randomXY())
    window.blit(i2, randomXY())
    window.blit(i3, randomXY())
    window.blit(i4, randomXY())



def draw(X):
    window.fill(X)



def key_press(event):
    if event.key == K_LEFT:
        displaySymbols()
    elif event.key == K_SPACE:
        draw(Colours.RED)


def play():
    draw(Colours.WHITE)
    while True:

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                key_press(event)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

play()
