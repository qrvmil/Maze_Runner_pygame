import pygame
from math import sin
import random

size = width, height = 700, 700
COLORS = [(252, 252, 238), (138, 127, 142), (120, 162, 183),
          (0, 191, 255), (0, 166, 147), (62, 180, 137),
          (127, 255, 212), (236, 235, 189), (239, 205, 184),
          (170, 152, 169), (0, 149, 182), (23, 128, 109),
          (23, 144, 69), (0, 102, 51), (205, 133, 63),
          (241, 58, 19), (202, 58, 39), (255, 146, 24)]
COLOR = (0, 149, 182)
FIRST = 20
SECOND = 30






class Draw:

    def __init__(self, screen):
        self.screen = screen
        self.koord = [20, 30, 50, 80, 120, 170, 230, 300, 380, 470, 570, 680, 800, 930, 1070]

        self.koord_not_change = self.koord[:]
        self.first = 20

        for i in range(15):
            pygame.draw.circle(self.screen, COLOR, (350, 350), self.koord[i], width=1)


    def grow(self):
        k = 0.5


        if self.koord[0] == SECOND:

            self.koord = [self.first] + self.koord[:-1]
            self.first = 20





        for i in range(15):
            pygame.draw.circle(self.screen, COLOR, (350, 350), self.koord[i], width=1)


        for i in range(15):
            self.koord[i] += k
            k += 0.5



def start():

    pygame.init()
    pygame.display.set_caption('test 0.0.2')
    clock = pygame.time.Clock()


    screen = pygame.display.set_mode(size)
    fig = Draw(screen)


    pygame.display.flip()

    running = True
    start = False

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start:
                    start = False
                else:
                    start = True

        screen.fill((0, 0, 0))

        if start:
            screen.fill((0, 0, 0))

            # l += v * clock.tick() / 60
            t = clock.tick(60) * 2

            # fig.step += 1

            fig.grow()

            pygame.display.flip()

    pygame.quit()

start()
