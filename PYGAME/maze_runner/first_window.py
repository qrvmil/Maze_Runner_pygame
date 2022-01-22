import pygame
import random
from test import start
from black1 import start_color
from skins import skin
from constants import ALL_LINES_V, ALL_LINES_G, color, color2, hsv, hsv2, COLORS

# настраиваем основные константы для цвета в hsv

buttons_color1 = pygame.Color(165, 176, 65)
buttons_color2 = pygame.Color(165, 176, 65)

# lines_color = pygame.Color(63, 166, 157) blue
# lines_color =  pygame.Color(130, 62, 128) pink
# lines_color = pygame.Color(165, 176, 65) yellow
# lines_color = pygame.Color(176, 169, 33) yellow bright
# lines_color = pygame.Color(94, 171, 117) green

lines_color = pygame.Color(165, 176, 65)

buttons_color1.hsva = (hsv[0], hsv[1], hsv[2] - 30, hsv[3])
buttons_color2.hsva = (hsv2[0], hsv2[1], hsv2[2], hsv2[3])


# прорисовка линий
def draw_main(screen):
    screen.fill((25, 33, 32))

    # отрисовка задних линий фона

    for i in range(8):
        pygame.draw.line(screen, COLORS[i], ALL_LINES_V[i][0], ALL_LINES_V[i][1])
        pygame.draw.line(screen, COLORS[i], ALL_LINES_G[i][0], ALL_LINES_G[i][1])


def start_window():
    pygame.init()

    size = width, height = 700, 700

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('вроде как старт')

    sound1 = pygame.mixer.Sound('button_click.mp3')

    pygame.mixer.music.load('star_wars2.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)

    draw_main(screen)
    # отрисовка кнопок

    start1 = pygame.draw.rect(screen, color, (250, 100, 200, 70), 0)
    start2 = pygame.draw.rect(screen, color2, (245, 95, 200, 70), 0)

    font = pygame.font.SysFont('cmmi10', 50)
    text = font.render("START", True, (3, 3, 68))
    text_xy = (285, 117)
    screen.blit(text, text_xy)

    record1 = pygame.draw.rect(screen, color, (250, 300, 200, 300), 0)
    record2 = pygame.draw.rect(screen, color2, (245, 295, 200, 300), 0)

    font = pygame.font.SysFont('cmmi10', 25)

    # выводим все рекорды

    with open("record.txt", "r") as file:
        inp = file.read().split()

    r_y = 320
    k = 0

    for i in inp:
        text_record = font.render(i, True, (3, 3, 68))
        record_xy = (340, r_y)
        r_y += 20
        screen.blit(text_record, record_xy)
        k += 1
        if k >= 13:
            print(404)
            break

    colorful1 = pygame.draw.rect(screen, buttons_color1, (20, 100, 200, 70), 0)
    colorful2 = pygame.draw.rect(screen, buttons_color2, (15, 95, 200, 70), 0)

    font1 = pygame.font.SysFont('cmmi10', 40)
    text1 = font1.render("COLOR", True, (3, 3, 68))
    text1_xy = (60, 115)
    screen.blit(text1, text1_xy)

    skin1 = pygame.draw.rect(screen, buttons_color1, (480, 100, 200, 70), 0)
    skin2 = pygame.draw.rect(screen, buttons_color2, (475, 95, 200, 70), 0)

    font1 = pygame.font.SysFont('cmmi10', 40)
    text1 = font1.render("SKIN", True, (3, 3, 68))
    text1_xy = (540, 115)
    screen.blit(text1, text1_xy)

    pygame.display.flip()

    running = True

    while running:

        draw_main(screen)

        start1 = pygame.draw.rect(screen, color, (250, 100, 200, 70), 0)
        start2 = pygame.draw.rect(screen, color2, (245, 95, 200, 70), 0)

        font = pygame.font.SysFont('cmmi10', 50)
        text = font.render("START", True, (3, 3, 68))
        text_xy = (285, 117)
        screen.blit(text, text_xy)

        record1 = pygame.draw.rect(screen, buttons_color1, (250, 300, 200, 300), 0)
        record2 = pygame.draw.rect(screen, buttons_color2, (245, 295, 200, 300), 0)

        font = pygame.font.SysFont('cmmi10', 25)

        with open("record.txt", "r") as file:
            inp = file.read().split()

        r_y = 320
        k = 0

        for i in inp:
            text_record = font.render(i, True, (3, 3, 68))
            record_xy = (340, r_y)
            r_y += 20
            screen.blit(text_record, record_xy)
            k += 1
            if k >= 13:
                break

        colorful1 = pygame.draw.rect(screen, buttons_color1, (20, 100, 200, 70), 0)
        colorful2 = pygame.draw.rect(screen, buttons_color2, (15, 95, 200, 70), 0)

        font1 = pygame.font.SysFont('cmmi10', 40)
        text1 = font1.render("COLOR", True, (3, 3, 68))
        text1_xy = (60, 115)
        screen.blit(text1, text1_xy)

        skin1 = pygame.draw.rect(screen, buttons_color1, (480, 100, 200, 70), 0)
        skin2 = pygame.draw.rect(screen, buttons_color2, (475, 95, 200, 70), 0)

        font1 = pygame.font.SysFont('cmmi10', 40)
        text1 = font1.render("SKIN", True, (3, 3, 68))
        text1_xy = (540, 115)
        screen.blit(text1, text1_xy)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # открываем туннель
                if start1.collidepoint(mouse_pos):
                    sound1.play(0)
                    start()

                # открываем скины
                if skin1.collidepoint(mouse_pos):
                    sound1.play(0)
                    skin()

                # открываем новый цветной тоннель (только если есть 15 монет...=))
                if colorful1.collidepoint(mouse_pos):
                    sound1.play(0)
                    with open("coins.txt", "r") as file:

                        inp = int(file.read())

                    if inp >= 15:
                        start_color()

    pygame.quit()


start_window()
