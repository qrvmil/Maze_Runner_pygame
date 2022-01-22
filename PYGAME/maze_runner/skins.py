import pygame
from constants import ALL_LINES_V, ALL_LINES_G, color, color2, hsv, hsv2, COLORS

SKINS = ['joda_neew.png',
         'enem_green2.png',
         'dart_veder.png',
         'chubaka.png',
         'r2d2.png',
         'mnstr.png']  #


def draw_skin(screen, skin):
    screen.fill((25, 33, 32))
    # отрисовка задних линий фона

    for i in range(8):
        pygame.draw.line(screen, COLORS[i], ALL_LINES_V[i][0], ALL_LINES_V[i][1])
        pygame.draw.line(screen, COLORS[i], ALL_LINES_G[i][0], ALL_LINES_G[i][1])

    pygame.draw.rect(screen, (25, 33, 32), (80, 80, 540, 540), 0)
    pygame.draw.rect(screen, COLORS[0], (80, 80, 540, 540), 1)

    all_creatures = pygame.sprite.Group()
    creature = pygame.sprite.Sprite()
    creature.image = pygame.image.load(skin)
    creature.rect = creature.image.get_rect()
    all_creatures.add(creature)

    creature.rect.x = 300
    creature.rect.y = 200

    all_creatures.draw(screen)


def skin():
    pygame.init()
    pygame.display.set_caption('зомбак всё равно топ')
    size = width, height = 700, 700
    screen2 = pygame.display.set_mode(size)

    sound1 = pygame.mixer.Sound('button_click.mp3')

    draw_skin(screen2, 'dart_veder.png')
    i = 2

    skip1 = pygame.draw.rect(screen2, color, (420, 250, 50, 35), 0)
    skip2 = pygame.draw.rect(screen2, color2, (415, 245, 50, 35), 0)
    font = pygame.font.SysFont('cmmi10', 50)
    text = font.render("->", True, (3, 3, 68))
    text_xy = (425, 246)
    screen2.blit(text, text_xy)

    skip3 = pygame.draw.rect(screen2, color, (200, 250, 50, 35), 0)
    skip4 = pygame.draw.rect(screen2, color2, (195, 245, 50, 35), 0)
    font = pygame.font.SysFont('cmmi10', 50)
    text = font.render("<-", True, (3, 3, 68))
    text_xy = (200, 246)
    screen2.blit(text, text_xy)

    back_to_menu1 = pygame.draw.rect(screen2, color, (200, 470, 300, 70), 0)
    back_to_menu2 = pygame.draw.rect(screen2, color2, (195, 465, 300, 70), 0)
    font = pygame.font.SysFont('cmmi10', 50)
    text = font.render("BACK TO MENU", True, (3, 3, 68))
    text_xy = (220, 480)
    screen2.blit(text, text_xy)

    pygame.display.flip()

    running = True

    while running:

        draw_skin(screen2, SKINS[i])

        # кнопочки всякие

        skip1 = pygame.draw.rect(screen2, color, (420, 250, 50, 35), 0)
        skip2 = pygame.draw.rect(screen2, color2, (415, 245, 50, 35), 0)
        font = pygame.font.SysFont('cmmi10', 50)
        text = font.render("->", True, (3, 3, 68))
        text_xy = (425, 246)
        screen2.blit(text, text_xy)

        skip3 = pygame.draw.rect(screen2, color, (200, 250, 50, 35), 0)
        skip4 = pygame.draw.rect(screen2, color2, (195, 245, 50, 35), 0)
        font = pygame.font.SysFont('cmmi10', 50)
        text = font.render("<-", True, (3, 3, 68))
        text_xy = (200, 246)
        screen2.blit(text, text_xy)

        back_to_menu1 = pygame.draw.rect(screen2, color, (200, 470, 300, 70), 0)
        back_to_menu2 = pygame.draw.rect(screen2, color2, (195, 465, 300, 70), 0)
        font = pygame.font.SysFont('cmmi10', 50)
        text = font.render("BACK TO MENU", True, (3, 3, 68))
        text_xy = (220, 480)
        screen2.blit(text, text_xy)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if back_to_menu1.collidepoint(mouse_pos):
                    sound1.play(0)
                    with open("skins.txt", "w") as file:
                        file.write(SKINS[i])  # запоминаем выбранный скин
                    return

                if skip1.collidepoint(mouse_pos):  # листаем
                    sound1.play(0)

                    i += 1
                    if i > 5: i = 0

                if skip3.collidepoint(mouse_pos):  # снова листаем (в другую сторону на этот раз)
                    sound1.play()
                    i -= 1
                    if i < 0: i = 5

    pygame.quit()
