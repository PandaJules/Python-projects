import random
import pygame, sys
import Colours
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BALL_RADIUS = 10
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle_vel = 0

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('ShooterPong')


def initialize():
    global paddle_pos, paddle_vel
    global ball_pos, ball_vel
    paddle_pos = [SCREEN_WIDTH/2 - 40, SCREEN_HEIGHT - PADDLE_HEIGHT/2]
    ball_pos = [random.randint(20,SCREEN_WIDTH-20), SCREEN_HEIGHT / 2]
    horzontal = random.randrange(1, 2)
    vertical = random.randrange(3, 6)
    ball_vel = [horzontal, vertical]


def draw(canvas):
    global paddle_pos, ball_pos, ball_vel

    canvas.fill(Colours.BLACK)

    # constrain the paddle by the screen, update the horizontal speed
    if PADDLE_WIDTH/2 < paddle_pos[0] < SCREEN_WIDTH - PADDLE_WIDTH/2:
        paddle_pos[0] += paddle_vel
    elif paddle_pos[0] == PADDLE_WIDTH / 2 and paddle_vel > 0:
        paddle_pos[0] += paddle_vel
    elif paddle_pos[0] == SCREEN_WIDTH - PADDLE_WIDTH / 2 and paddle_vel < 0:
        paddle_pos[0] += paddle_vel

    # update ball's speed
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    # draw a ball and a paddle
    pygame.draw.circle(canvas, Colours.PURPLE, ball_pos, BALL_RADIUS)
    pygame.draw.polygon(canvas, Colours.GREEN, [[paddle_pos[0] - PADDLE_WIDTH / 2, paddle_pos[1] - PADDLE_HEIGHT / 2],
                                                [paddle_pos[0] - PADDLE_WIDTH / 2, paddle_pos[1] + PADDLE_HEIGHT / 2],
                                                [paddle_pos[0] + PADDLE_WIDTH / 2, paddle_pos[1] + PADDLE_HEIGHT / 2],
                                                [paddle_pos[0] + PADDLE_WIDTH / 2, paddle_pos[1] - PADDLE_HEIGHT / 2]])

    # ball collision with top, left and right walls
    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif int(ball_pos[0]) < BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif int(ball_pos[0]) > SCREEN_WIDTH-BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]


    # ball collision with a paddle
    if int(ball_pos[1]) >= SCREEN_HEIGHT - BALL_RADIUS - PADDLE_HEIGHT \
            and int(ball_pos[0]) in range(paddle_pos[0] - PADDLE_WIDTH / 2, paddle_pos[0] + PADDLE_WIDTH / 2):
        ball_vel[1] = -ball_vel[1]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[1]) >= SCREEN_HEIGHT:
        initialize()


def key_press(event):
    global paddle_vel

    if event.key == K_LEFT:
        paddle_vel = -10
    elif event.key == K_RIGHT:
        paddle_vel = 10
    # if event.key == K_SPACE:
    #     shoot()


def key_release(event):
    global paddle_vel

    if event.key not in (K_UP, K_DOWN):
        paddle_vel = 0


def play():
    initialize()

    while True:

        draw(window)

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                key_press(event)
            elif event.type == KEYUP:
                key_release(event)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()
        fps.tick(60)


play()
