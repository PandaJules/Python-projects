import pygame, sys
from pygame import *

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
paddle = pygame.Rect(10, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
PADDLE_COLOR = pygame.color.Color("orange")


while True:

    # make screen black
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        paddle.left = paddle.left - 5

    if keys[K_RIGHT]:
        paddle.left = paddle.left + 5

    screen.fill(PADDLE_COLOR, paddle);
    pygame.display.update()
