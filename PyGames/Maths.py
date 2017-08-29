from random import randint
from random import choice

import pygame, pygame.font, pygame.event, pygame.draw
import sys
from pygame.locals import *


def get_key():
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                return event.key


def display_box(screen, message):
    fontobject = pygame.font.Font(None, 30)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 100,
                      (screen.get_height() / 2) - 10,
                      200, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                     ((screen.get_width() / 2) - 102,
                      (screen.get_height() / 2) - 12,
                      204, 24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                    ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()


def ask(screen, question):
    current_string = []
    display_box(screen, question + "".join(current_string))
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_SPACE:
            pygame.quit()
            sys.exit()
        elif inkey == K_RETURN:
            return "".join(current_string)
        elif inkey <= 127:
            current_string.append(chr(inkey))

        display_box(screen, question + "".join(current_string))


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    operators = ["+", "-", "*", "//"]
    while 1:
        x = randint(1, 5)
        y = randint(10, 20)
        op = choice(operators)
        answer = ask(screen, "{}{}{}=".format(x, op, y))
        correct = int(eval(str(x)+op+str(y)))
        if int(answer) == correct:
            print("Correct!")
        else:
            print("Your answer is", answer, "but should be", correct)


if __name__ == '__main__':
    main()
