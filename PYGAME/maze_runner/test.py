import pygame
from math import cos
import random
import sys
from sw import game_over

# настройка констант
size = width, height = 700, 700
COLORS = [(252, 252, 238), (138, 127, 142), (120, 162, 183),
          (0, 191, 255), (0, 166, 147), (62, 180, 137),
          (127, 255, 212), (236, 235, 189), (239, 205, 184),
          (170, 152, 169), (0, 149, 182), (23, 128, 109),
          (23, 144, 69), (0, 102, 51), (205, 133, 63),
          (241, 58, 19), (202, 58, 39), (255, 146, 24)]
COLOR = (108, 241, 246)
FIRST = [330, 330, 40, 40]
SECOND = (321, 321)


class Draw:  # основная функция прорисовки

    def __init__(self, screen):
        self.screen = screen
        self.lives = 3  # жизни
        self.coll = 0
        self.back_xy = (20, 20, 100, 50)
        self.myfont = pygame.font.SysFont('cmmi10', 30)
        self.text_lives()  # печатаем жизни
        # координаты квадратов
        self.koord = [(330, 330, 40, 40), (321, 321, 57, 57), (308, 308, 83, 83),
                      (291, 291, 117, 117), (270, 270, 160, 160), (244, 244, 211, 211),
                      (214, 214, 271, 271), (180, 180, 339, 339), (142, 142, 416, 416),
                      (99, 99, 501, 501), (52, 52, 595, 595), (1, 1, 697, 697),
                      (-54, -54, 808, 808), (-114, -114, 927, 927), (-178, -178, 1055, 1055)]
        self.koord = [list(i) for i in self.koord]
        self.koord_not_change = self.koord[:]
        self.first = [330, 330, 40, 40]

        self.first_enem = [[344, 325, 10, 10], [364, 344, 10, 10], [344, 364, 10, 10], [325, 344, 10, 10]]
        self.good_first_enem = [[346, 325, 5, 5], [369, 346, 5, 5], [346, 369, 5, 5], [325, 346, 5, 5]]

        self.map = [[0, 0, 0, 0] for _ in range(15)]  # часть карты (карты врагов)
        self.map_good_enemies = [[0, 0, 0, 0] for _ in range(15)]  # тоже часть карты (карты монет)

        for i in range(5):
            for j in range(4):
                if random.randint(1, 10) == 8:
                    self.map[i][j] = 1  # ставим препятствие
                if random.randint(1, 20) == 8:
                    self.map_good_enemies[i][j] = 1  # ставим монету

                # проверка на непрохоимые препятствия

                if self.map[i][0] == 1 and self.map[i][1] == 1 and self.map[i][2] == 1 and self.map[i][3] == 1:
                    self.map[i][0] = 1
                    self.map[i][1] = 0
                    self.map[i][2] = 1
                    self.map[i][3] = 0
        # коорды врагов

        self.enemies = [[[344, 325, 10, 10], [364, 344, 10, 10], [344, 364, 10, 10], [325, 344, 10, 10]],
                        [[341, 314, 15, 15], [369, 341, 15, 15], [341, 369, 15, 15], [314, 341, 15, 15]],
                        [[338, 299, 21, 21], [378, 338, 21, 21], [338, 378, 21, 21], [299, 338, 21, 21]],
                        [[335, 280, 28, 28], [391, 335, 28, 28], [335, 391, 28, 28], [280, 335, 28, 28]],
                        [[331, 257, 35, 35], [406, 331, 35, 35], [331, 406, 35, 35], [257, 331, 35, 35]],
                        [[327, 229, 43, 43], [426, 327, 43, 43], [327, 426, 43, 43], [229, 327, 43, 43]],
                        [[323, 197, 52, 52], [449, 323, 52, 52], [323, 449, 52, 52], [197, 323, 52, 52]],
                        [[318, 161, 61, 61], [477, 318, 61, 61], [318, 477, 61, 61], [161, 318, 61, 61]],
                        [[313, 120, 71, 71], [507, 313, 71, 71], [313, 507, 71, 71], [120, 313, 71, 71]],
                        [[308, 75, 81, 81], [542, 308, 81, 81], [308, 542, 81, 81], [75, 308, 81, 81]],
                        [[303, 26, 92, 92], [580, 303, 92, 92], [303, 580, 92, 92], [26, 303, 92, 92]],
                        [[297, -27, 104, 104], [622, 297, 104, 104], [297, 622, 104, 104], [-27, 297, 104, 104]],
                        [[297, -27, 104, 104], [622, 297, 104, 104], [297, 622, 104, 104], [-27, 297, 104, 104]],
                        [[297, -27, 104, 104], [622, 297, 104, 104], [297, 622, 104, 104], [-27, 297, 104, 104]],
                        [[297, -27, 104, 104], [622, 297, 104, 104], [297, 622, 104, 104], [-27, 297, 104, 104]],
                        [[297, -27, 104, 104], [622, 297, 104, 104], [297, 622, 104, 104], [-27, 297, 104, 104]]]

        # коорды монет

        self.good_enemies = [[[346, 325, 5, 5], [369, 346, 5, 5], [346, 369, 5, 5], [325, 346, 5, 5]],
                             [[346, 314, 7, 7], [378, 346, 7, 7], [346, 378, 7, 7], [314, 346, 7, 7]],
                             [[345, 299, 9, 9], [391, 345, 9, 9], [345, 391, 9, 9], [299, 345, 9, 9]],
                             [[344, 280, 11, 11], [409, 344, 11, 11], [344, 409, 11, 11], [280, 344, 11, 11]],
                             [[342, 257, 13, 13], [429, 342, 13, 13], [342, 429, 13, 13], [257, 342, 13, 13]],
                             [[342, 229, 15, 15], [455, 342, 15, 15], [342, 455, 15, 15], [229, 342, 15, 15]],
                             [[341, 197, 17, 17], [485, 341, 17, 17], [341, 485, 17, 17], [197, 341, 17, 17]],
                             [[340, 161, 19, 19], [520, 340, 19, 19], [340, 520, 19, 19], [161, 340, 19, 19]],
                             [[338, 120, 21, 21], [558, 338, 21, 21], [338, 558, 21, 21], [120, 338, 21, 21]],
                             [[338, 75, 23, 23], [601, 338, 23, 23], [338, 601, 23, 23], [75, 338, 23, 23]],
                             [[337, 26, 25, 25], [648, 337, 25, 25], [337, 648, 25, 25], [26, 337, 25, 25]],
                             [[336, -27, 27, 27], [700, 336, 27, 27], [336, 700, 27, 27], [-27, 336, 27, 27]],
                             [[334, -84, 29, 29], [754, 334, 29, 29], [334, 754, 29, 29], [-84, 334, 29, 29]],
                             [[334, -146, 31, 31], [814, 334, 31, 31], [334, 814, 31, 31], [-146, 334, 31, 31]],
                             [[348, 76, 3, 3], [621, 348, 3, 3], [348, 621, 3, 3], [76, 348, 3, 3]]]

        for i in range(12):
            for j in range(4):
                self.enemies[i][j] = [int(i) for i in self.enemies[i][j]]

        for i in range(15):
            pygame.draw.rect(self.screen, COLOR, self.koord[i], 1)  # рисуем квадрат

        side_small = self.koord[0][2]
        side_big = self.koord[-1][2]

        pygame.draw.line(self.screen, COLOR, (self.koord[-1][0], self.koord[-1][1]),
                         (self.koord[0][0], self.koord[0][1]))
        pygame.draw.line(self.screen, COLOR, (self.koord[-1][0] + side_big, self.koord[-1][1]),
                         (self.koord[0][0] + side_small, self.koord[0][1]))
        pygame.draw.line(self.screen, COLOR, (self.koord[-1][0] + side_big, self.koord[-1][1] + side_big),
                         (self.koord[0][0] + side_small, self.koord[0][1] + side_small))
        pygame.draw.line(self.screen, COLOR, (self.koord[-1][0], self.koord[-1][1] + side_big),
                         (self.koord[0][0], self.koord[0][1] + side_small))

        for i in range(12):
            for j in range(4):

                if self.map[i][j] == 1:  # рисуем врагов
                    pygame.draw.rect(self.screen, (255, 0, 0), self.enemies[i][j], 2)

        for i in range(12):
            for j in range(4):

                if self.map_good_enemies[i][j] == 1:  # рисуем монеты
                    pygame.draw.rect(self.screen, (0, 255, 0), self.good_enemies[i][j], 0)

    def grow(self, score):  # двигаем всю штуку (туннель и прочее)
        k = 0.5
        side = 10
        side_good = 5

        self.score1 = score
        self.text_lives()
        self.score(self.score1)

        if self.koord[0][0] <= SECOND[0]:  # проверка на отрисовку нового квадрата

            self.koord = [self.first] + self.koord[:-1]
            self.first = [330, 330, 40, 40]

            self.enemies = [self.first_enem] + self.enemies[:-1]
            self.first_enem = [[344, 325, 10, 10], [364, 344, 10, 10], [344, 364, 10, 10], [325, 344, 10, 10]]

            self.good_enemies = [self.good_first_enem] + self.good_enemies[:-1]
            self.good_first_enem = [[346, 325, 5, 5], [369, 346, 5, 5], [346, 369, 5, 5], [325, 346, 5, 5]]

            new = [0, 0, 0, 0]
            new_good = [0, 0, 0, 0]

            for i in range(4):  # новый ряд прпятствий и монет
                if random.randint(1, 10) == 10:
                    new[i] = 1

                if random.randint(1, 20) == 10:
                    new_good[i] = 1

            if new == [1, 1, 1, 1]: new = [1, 0, 1, 0]

            self.map = [new] + self.map[:-1]  # обновляем карту
            self.map_good_enemies = [new_good] + self.map_good_enemies[:-1]  # обновляем карту (другую)
            self.coll = 0

        for i in range(15):
            pygame.draw.rect(self.screen, COLOR, self.koord[i], 1)

        side_small = self.koord[0][2]
        side_big = self.koord[-1][2]

        pygame.draw.line(self.screen, COLOR, (self.koord[-1][0], self.koord[-1][1]),
                         (self.koord[0][0], self.koord[0][1]))
        pygame.draw.line(self.screen, COLOR, (self.koord[-1][0] + side_big, self.koord[-1][1]),
                         (self.koord[0][0] + side_small, self.koord[0][1]))
        pygame.draw.line(self.screen, COLOR, (self.koord[-1][0] + side_big, self.koord[-1][1] + side_big),
                         (self.koord[0][0] + side_small, self.koord[0][1] + side_small))
        pygame.draw.line(self.screen, COLOR, (self.koord[-1][0], self.koord[-1][1] + side_big),
                         (self.koord[0][0], self.koord[0][1] + side_small))

        for i in range(12):  # рисуем врагов
            for j in range(4):

                if self.map[i][j] == 1:
                    pygame.draw.rect(self.screen, (255, 0, 0), self.enemies[i][j], 2)

                if self.map_good_enemies[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 255, 0), self.good_enemies[i][j], 0)

        for i in range(15):  # увеличиваем всё

            self.koord[i][0] -= k * cos(45)  #
            self.koord[i][1] -= k * cos(45)  #
            self.koord[i][2] += k * 2 * cos(45)  #
            self.koord[i][3] += k * 2 * cos(45)  #

            for j in range(4):  # двигаем прпятствия

                differ_middle = (self.koord[i - 1][1] - self.koord[i][1])

                differ_big = (self.koord[i][2] - self.koord[i - 1][2]) // 2
                differ_small = (self.koord[i - 1][2] - side) // 2
                differ_small_good = (self.koord[i - 1][2] - side_good) // 2

                self.enemies[i - 1][j][2] = side
                self.enemies[i - 1][j][3] = side

                self.good_enemies[i - 1][j][2] = side_good
                self.good_enemies[i - 1][j][3] = side_good

                if j == 0:
                    self.enemies[i - 1][j][0] = self.koord[i][0] + differ_big + differ_small
                    self.enemies[i - 1][j][1] = self.koord[i][1] + differ_middle // 2

                    self.good_enemies[i - 1][j][0] = self.koord[i][0] + differ_big + differ_small_good
                    self.good_enemies[i - 1][j][1] = self.koord[i][1] + differ_middle // 2
                elif j == 1:
                    self.enemies[i - 1][j][0] = self.koord[i][0] + self.koord[i][2] - differ_middle // 2 - side
                    self.enemies[i - 1][j][1] = self.koord[i][1] + differ_big + differ_small

                    self.good_enemies[i - 1][j][0] = self.koord[i][0] + self.koord[i][
                        2] - differ_middle // 2 - side_good
                    self.good_enemies[i - 1][j][1] = self.koord[i][1] + differ_big + differ_small_good
                elif j == 2:
                    self.enemies[i - 1][j][0] = self.koord[i][0] + differ_big + differ_small
                    self.enemies[i - 1][j][1] = self.koord[i][1] + self.koord[i][2] - differ_middle // 2 - side

                    self.good_enemies[i - 1][j][0] = self.koord[i][0] + differ_big + differ_small_good
                    self.good_enemies[i - 1][j][1] = self.koord[i][1] + self.koord[i][
                        2] - differ_middle // 2 - side_good

                else:
                    self.enemies[i - 1][j][0] = self.koord[i][0] + differ_middle // 2
                    self.enemies[i - 1][j][1] = self.koord[i][1] + differ_big + differ_small

                    self.good_enemies[i - 1][j][0] = self.koord[i][0] + differ_middle // 2
                    self.good_enemies[i - 1][j][1] = self.koord[i][1] + differ_big + differ_small_good

            k += 0.5
            side += 7
            side_good += 2

    def rotate_right(self):  # поворот влево)
        for i in range(15):
            self.map[i] = self.map[i][1:] + [self.map[i][0]]
            self.map_good_enemies[i] = self.map_good_enemies[i][1:] + [self.map_good_enemies[i][0]]

    def rotate_left(self):  # поворот вправо))
        for i in range(15):
            self.map[i] = [self.map[i][-1]] + self.map[i][:-1]
            self.map_good_enemies[i] = [self.map_good_enemies[i][-1]] + self.map_good_enemies[i][:-1]

    def text_lives(self):

        text = self.myfont.render('Жизней: ' + str(self.lives), False, COLOR)
        self.screen.blit(text, (500, 20))

    def score(self, score):
        self.screen.fill(COLOR,
                         (20, 70, 100, 50))
        text = self.myfont.render(f'{score}', False, 'black')
        self.screen.blit(text, (40, 80))


def start():
    pygame.init()
    pygame.font.init()

    pygame.display.set_caption('tunnel?')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)

    sound1 = pygame.mixer.Sound('click3.mp3')
    sound2 = pygame.mixer.Sound('button_click.mp3')

    screen.fill((25, 33, 32))
    fig = Draw(screen)

    running = True
    start = False

    with open("skins.txt", "r") as file:  #
        inp = file.readline()

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load(inp)
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    sprite.rect.x = 310
    sprite.rect.y = 580

    all_sprites.draw(screen)

    back_xy = (20, 20, 100, 50)
    back = pygame.draw.rect(screen, COLOR, back_xy, 0)
    font = pygame.font.SysFont('cmmi10', 25)
    text = font.render('BACK', False, 'black')
    screen.blit(text, (back_xy[0] + 20, back_xy[1] + 15))

    pygame.display.flip()

    score = 0
    coins = 0

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back.collidepoint(mouse_pos):
                    sound2.play(0)
                    return

                else:
                    start = not start

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    fig.rotate_right()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    fig.rotate_left()

        screen.fill((0, 0, 0))

        if start:
            screen.fill((25, 33, 32))

            clock.tick(60)

            fig.grow(score)  # двигаем всю систему
            back = pygame.draw.rect(screen, COLOR, back_xy, 0)
            font = pygame.font.SysFont('cmmi10', 25)
            text = font.render('BACK', False, 'black')
            screen.blit(text, (back_xy[0] + 20, back_xy[1] + 15))
            score += 1  # рекорд
            # прверка монет на столкновение

            if fig.good_enemies[7][2][1] + fig.good_enemies[7][2][1] >= 650 and fig.map_good_enemies[7][2] == 1:
                sound1.play(0)
                fig.map_good_enemies[7][2] = 0
                coins += 1

            # прверка враггов на столкновение

            if fig.enemies[7][2][1] + fig.enemies[7][2][1] >= 690 and fig.map[7][2] == 1:

                if not fig.coll:
                    fig.lives -= 1
                fig.coll = 1
                fig.text_lives()
                if fig.lives == 0:

                    start = False

                    pygame.time.wait(1000)

                    # рекордик вписываем в общий файлик

                    with open("record.txt", "r") as file:

                        inp = file.read().split()

                        inp2 = list(map(int, inp))
                        inp2.append(score)
                        inp2.sort(reverse=True)
                        inp3 = [str(i) + ' ' for i in inp2]

                    with open("record.txt", "w") as file:
                        for i in inp3:
                            file.write(i)

                    pygame.draw.rect(screen, (255, 0, 0), (250, 100, 190, 70), 0)

                    font = pygame.font.SysFont('cmmi10', 25)
                    text = font.render("GAME OVER =(", True, (3, 3, 68))
                    text_xy = (280, 110)
                    screen.blit(text, text_xy)

                    pygame.time.wait(2000)

                    # монетки тоже добавляем

                    with open("coins.txt", "r") as file:

                        inp = int(file.read())

                        coins += inp

                    with open("coins.txt", "w") as file:
                        file.write(str(coins))

                    game_over()

                    return

            all_sprites.draw(screen)

            pygame.display.flip()

    pygame.quit()
    sys.exit()
