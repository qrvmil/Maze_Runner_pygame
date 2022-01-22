import pygame
from math import sin, cos
import random

size = width, height = 700, 700
COLORS = [(252, 252, 238), (138, 127, 142), (120, 162, 183),
          (0, 191, 255), (0, 166, 147), (62, 180, 137),
          (127, 255, 212), (236, 235, 189), (239, 205, 184),
          (170, 152, 169), (0, 149, 182), (23, 128, 109),
          (23, 144, 69), (0, 102, 51), (205, 133, 63),
          (241, 58, 19), (202, 58, 39), (255, 146, 24)]
COLOR = (0, 149, 182)
FIRST = [(345, 337), (355, 337), (363, 345), (363, 355), (355, 363), (345, 363), (337, 355), (337, 345)]
SECOND = 342


class Tunnel:
    def __init__(self, screen):
        self.board = [[0] * 8 for _ in range(15)]
        self.sprite_g = pygame.sprite.Group()
        self.screen = screen

    def add_enem(self):
        for i in range(8):
            if random.randint(1, 10) > 7:
                self.board[0][i] = Square(0, i, "red")
        self.draw_sprites()

    def transpose(self, enemy, i):
        enemy.sprite.rect.w *= (i * 1.2)
        enemy.sprite.rect.h *= (i * 1.2)

    def place(self, enemy, i, j):
        enemy.sprite.rect.x *= (i * 1.2)
        pass

        # enemy.sprite

    def draw_sprites(self):
        self.sprite_g.empty()
        for i in range(15):
            for j in range(8):
                if self.board[i][j] != 0:
                    self.place(self.board[i][j], i, j)
                    self.transpose(self.board[i][j], i, j)
                    self.sprite_g.add(self.board[i][j])
        self.sprite_g.draw(self.screen)


class Enemies:
    def __init(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Square(Enemies):
    def __init__(self, x, y, color):
        super().__init__(self, x, y, color)
        self.image = pygame.image.load("tank.png")
        self.image = pygame.image.transform(self.image, (30, 30))
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.image
        self.sprite.rect = self.sprite.image.get_rect()


class Draw:

    def __init__(self, screen):
        self.screen = screen
        self.koord = [[(345, 336), (356, 336), (365, 345), (365, 356), (356, 365), (345, 365), (336, 356), (336, 345)],
                      [(342, 328), (359, 328), (373, 342), (373, 359), (359, 373), (342, 373), (328, 359), (328, 342)],
                      [(337, 314), (365, 314), (388, 337), (388, 365), (365, 388), (337, 388), (314, 365), (314, 337)],
                      [(329, 292), (373, 292), (410, 329), (410, 373), (373, 410), (329, 410), (292, 373), (292, 329)],
                      [(319, 264), (384, 264), (439, 319), (439, 384), (384, 439), (319, 439), (264, 384), (264, 319)],
                      [(306, 229), (397, 229), (474, 306), (474, 397), (397, 474), (306, 474), (229, 397), (229, 306)],
                      [(291, 188), (413, 188), (516, 291), (516, 413), (413, 516), (291, 516), (188, 413), (188, 291)],
                      [(273, 139), (431, 139), (565, 273), (565, 431), (431, 565), (273, 565), (139, 431), (139, 273)],
                      [(253, 84), (452, 84), (621, 253), (621, 452), (452, 621), (253, 621), (84, 452), (84, 253)],
                      [(230, 22), (475, 22), (683, 230), (683, 475), (475, 683), (230, 683), (22, 475), (22, 230)],
                      [(205, -46), (501, -46), (752, 205), (752, 501), (501, 752), (205, 752), (-46, 501), (-46, 205)],
                      [(177, -122), (529, -122), (828, 177), (828, 529), (529, 828), (177, 828), (-122, 529),
                       (-122, 177)],
                      [(147, -204), (560, -204), (911, 147), (911, 560), (560, 911), (147, 911), (-204, 560),
                       (-204, 147)],
                      [(114, -293), (593, -293), (1000, 114), (1000, 593), (593, 1000), (114, 1000), (-293, 593),
                       (-293, 114)],
                      [(79, -388), (629, -388), (1096, 79), (1096, 629), (629, 1096), (79, 1096), (-388, 629),
                       (-388, 79)],
                      [(41, -491), (667, -491), (1199, 41), (1199, 667), (667, 1199), (41, 1199), (-491, 667),
                       (-491, 41)]]

        self.koord = [[list(j) for j in i] for i in self.koord]

        self.first = [[345, 336], [356, 336], [365, 345], [365, 356], [356, 365], [345, 365], [336, 356], [336, 345]]

        self.lines = [[(41, -491), (345, 336)], [(667, -491), (356, 336)], [(1199, 41), (365, 345)],
                      [(1199, 667), (365, 356)], [(667, 1199), (356, 365)], [(41, 1199), (345, 365)],
                      [(-491, 667), (336, 356)], [(-491, 41), (336, 345)]]

        for i in range(15):
            pygame.draw.polygon(self.screen, COLOR, self.koord[i], 1)

        for i in range(8):
            pygame.draw.line(self.screen, COLOR, self.lines[i][0], self.lines[i][1])


    def grow(self):

        k = 0.2

        if self.koord[0][0][0] <= SECOND:
            self.koord = [self.first] + self.koord[:-1]
            self.first = [[345, 336], [356, 336], [365, 345], [365, 356], [356, 365], [345, 365], [336, 356],
                          [336, 345]]

        for i in range(15):
            pygame.draw.polygon(self.screen, COLOR, self.koord[i], 1)

        for i in range(8):
            self.lines[i] = self.koord[9][i], self.koord[0][i] # если подправить 9 на 8 линии быстрее выстраиваются

        for i in range(8):
            pygame.draw.line(self.screen, COLOR, self.lines[i][0], self.lines[i][1])

        for i in range(15):
            self.koord[i][0][0] -= k * cos(45)
            self.koord[i][0][1] -= k * sin(45)

            self.koord[i][1][0] += k * cos(45)
            self.koord[i][1][1] -= k * sin(45)

            self.koord[i][2][0] += k * sin(45)
            self.koord[i][2][1] -= k * cos(45)

            self.koord[i][3][0] += k * sin(45)
            self.koord[i][3][1] += k * cos(45)

            self.koord[i][4][0] += k * cos(45)
            self.koord[i][4][1] += k * sin(45)

            self.koord[i][5][0] -= k * cos(45)
            self.koord[i][5][1] += k * sin(45)

            self.koord[i][6][0] -= k * sin(45)
            self.koord[i][6][1] += k * cos(45)

            self.koord[i][7][0] -= k * sin(45)
            self.koord[i][7][1] -= k * cos(45)

            k += 0.5


def start():
    pygame.init()
    pygame.display.set_caption('test 030')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)
    fig = Draw(screen)
    tunnel = Tunnel(screen)

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
            tunnel.draw_sprites()

            pygame.display.flip()

    pygame.quit()


start()

'''
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect
    '''