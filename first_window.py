import pygame
import random
from test030 import start


if __name__ == '__main__':

    pygame.init()

    size = width, height = 700, 700

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('test 0.0.0')


    # отрисовка

    # настройка цвета

    color = pygame.Color(165, 176, 65)
    color2 = pygame.Color(165, 176, 65)

    buttons_color1 = pygame.Color(165, 176, 65)
    buttons_color2 = pygame.Color(165, 176, 65)

    # lines_color = pygame.Color(63, 166, 157) blue
    # lines_color =  pygame.Color(130, 62, 128) pink
    # lines_color = pygame.Color(165, 176, 65) yellow
    # lines_color = pygame.Color(176, 169, 33) yellow bright
    # lines_color = pygame.Color(94, 171, 117) green

    lines_color = pygame.Color(165, 176, 65)

    hsv = color.hsva
    hsv2 = color2.hsva

    color.hsva = (hsv[0], hsv[1], hsv[2], hsv[3])
    color2.hsva = (hsv2[0], hsv2[1], hsv2[2] + 30, hsv2[3])
    buttons_color1.hsva = (hsv[0], hsv[1], hsv[2] - 30, hsv[3])
    buttons_color2.hsva = (hsv2[0], hsv2[1], hsv2[2], hsv2[3])

    screen.fill((25, 33, 32))

    # отрисовка задних линий фона

    top_coords = [(0, 0), (100, 0), (200, 0), (300, 0), (400, 0), (500, 0), (600, 0), (700, 0), (150, 0),
                  (250, 0), (350, 0), (450, 0), (550, 0), (650, 0), (120, 0), (380, 0)]

    low_coords = [(0, 700), (100, 700), (200, 700), (300, 700), (400, 700), (500, 700),
                  (600, 700), (700, 700), (150, 700), (250, 700), (350, 700), (450, 700),
                  (550, 700), (650, 700), (180, 700), (320, 700)]

    right_coords = [(700, 0), (700, 100), (700, 200), (700, 300), (700, 400), (700, 500),
                    (700, 600), (700, 700), (700, 150), (700, 250), (700, 350), (700, 450), (700, 550), (700, 650)]

    left_coords = [(0, 0), (0, 100), (0, 200), (0, 300), (0, 400), (0, 500),
                   (0, 600), (0, 700), (0, 150), (0, 250), (0, 350), (0, 450), (0, 550), (0, 650)]

    for i in range(8):
        lines_color.hsva = (hsv[0], hsv[1], hsv[2] + random.randint(-40, 10), hsv[3])
        pygame.draw.line(screen, lines_color, random.choice(top_coords), random.choice(low_coords))
        pygame.draw.line(screen, lines_color, random.choice(left_coords), random.choice(right_coords))

    # отрисовка кнопок

    # кнопка настройки
    settings1 = pygame.draw.rect(screen, buttons_color1, (80, 100, 200, 70), 0)
    settings2 = pygame.draw.rect(screen, buttons_color2, (75, 95, 200, 70), 0)

    font1 = pygame.font.SysFont('cmmi10', 40)
    text1 = font1.render("settings", True, (3, 3, 68))
    text1_xy = (110, 115)
    screen.blit(text1, text1_xy)

    # кнопка карта
    map1 = pygame.draw.rect(screen, buttons_color1, (400, 100, 200, 70), 0)
    map2 = pygame.draw.rect(screen, buttons_color2, (395, 95, 200, 70), 0)

    font2 = pygame.font.SysFont('cmmi10', 40)
    text2 = font2.render("map/levels", True, (3, 3, 68))
    text2_xy = (420, 115)
    screen.blit(text2, text2_xy)

    # кнопка help
    help1 = pygame.draw.rect(screen, buttons_color1, (60, 600, 200, 70), 0)
    help2 = pygame.draw.rect(screen, buttons_color2, (55, 595, 200, 70), 0)

    font3 = pygame.font.SysFont('cmmi10', 40)
    text3 = font3.render("help", True, (3, 3, 68))
    text3_xy = (110, 615)
    screen.blit(text3, text3_xy)

    '''# кнопка top secret
    pygame.draw.rect(screen, color, (250, 250, 200, 70), 0)
    pygame.draw.rect(screen, color2, (245, 245, 200, 70), 0)

    # кнопка выбрать тему? -------> можно убрать)
    pygame.draw.rect(screen, color, (250, 250, 200, 70), 0)
    pygame.draw.rect(screen, color2, (245, 245, 200, 70), 0)'''

    # режим Night Fury -----> что?!
    night_fury1 = pygame.draw.rect(screen, buttons_color1, (450, 600, 200, 70), 0)
    night_fury2 = pygame.draw.rect(screen, buttons_color2, (445, 595, 200, 70), 0)

    font4 = pygame.font.SysFont('cmmi10', 40)
    text4 = font4.render("record", True, (3, 3, 68))
    text4_xy = (490, 615)
    screen.blit(text4, text4_xy)

    # самая главная кнопка старт
    start1 = pygame.draw.rect(screen, color, (250, 250, 200, 70), 0)
    start2 = pygame.draw.rect(screen, color2, (245, 245, 200, 70), 0)

    font = pygame.font.SysFont('cmmi10', 50)
    text = font.render("START", True, (3, 3, 68))
    text_xy = (285, 265)
    screen.blit(text, text_xy)

    pygame.display.flip()

    running = True


    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if start1.collidepoint(mouse_pos):
                    start()




    pygame.quit()
