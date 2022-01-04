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
FIRST = [330, 330, 40, 40]
SECOND = (321, 321)






class Draw:

    def __init__(self, screen):
        self.screen = screen
        self.koord = [(330, 330, 40, 40), (321, 321, 57, 57), (308, 308, 83, 83),
                      (291, 291, 117, 117), (270, 270, 160, 160), (244, 244, 211, 211),
                      (214, 214, 271, 271), (180, 180, 339, 339), (142, 142, 416, 416),
                      (99, 99, 501, 501), (52, 52, 595, 595), (1, 1, 697, 697),
                      (-54, -54, 808, 808), (-114, -114, 927, 927), (-178, -178, 1055, 1055)]
        self.koord = [list(i) for i in self.koord]
        self.koord_not_change = self.koord[:]
        self.first = [330, 330, 40, 40]

        for i in range(15):
            pygame.draw.rect(self.screen, COLOR, self.koord[i], 1)


    def grow(self):
        k = 0.5


        if (self.koord[0][0], self.koord[0][1]) == SECOND:

            self.koord = [self.first] + self.koord[:-1]
            self.first = [330, 330, 40, 40]





        for i in range(15):
            pygame.draw.rect(self.screen, COLOR, self.koord[i], 1)


        for i in range(15):
            self.koord[i][0] -= k
            self.koord[i][1] -= k
            self.koord[i][2] += k * 2
            self.koord[i][3] += k * 2
            k += 0.5



def start():

    pygame.init()
    pygame.display.set_caption('test 0.1.0')
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

