import pygame
from constants import ALL_LINES_V, ALL_LINES_G, color, color2, hsv, hsv2, COLORS


def draw_game_over(screen):
    screen.fill((25, 33, 32))
    # отрисовка задних линий фона
    running = True

    for i in range(8):
        pygame.draw.line(screen, COLORS[i], ALL_LINES_V[i][0], ALL_LINES_V[i][1])
        pygame.draw.line(screen, COLORS[i], ALL_LINES_G[i][0], ALL_LINES_G[i][1])

    pygame.draw.rect(screen, (25, 33, 32), (80, 80, 540, 540), 0)
    pygame.draw.rect(screen, COLORS[0], (80, 80, 540, 540), 1)

    pygame.draw.rect(screen, color, (200, 150, 300, 70), 0)
    pygame.draw.rect(screen, color2, (205, 155, 300, 70), 0)

    font = pygame.font.SysFont('cmmi10', 50)
    text = font.render("GAME OVEEER", True, (3, 3, 68))
    text_xy = (220, 168)
    screen.blit(text, text_xy)

    # рисуем грустного кота

    all_cats = pygame.sprite.Group()
    sad_cat = pygame.sprite.Sprite()
    sad_cat.image = pygame.image.load('sad_cat.png')
    sad_cat.rect = sad_cat.image.get_rect()
    all_cats.add(sad_cat)

    sad_cat.rect.x = 250
    sad_cat.rect.y = 400

    all_cats.draw(screen)


def game_over():
    pygame.init()
    pygame.display.set_caption('вы проиграли, хнык =(')  # хнык
    size = width, height = 700, 700
    screen2 = pygame.display.set_mode(size)

    sound1 = pygame.mixer.Sound('button_click.mp3')
    sound2 = pygame.mixer.Sound('end.mp3')
    sound2.play(0)

    draw_game_over(screen2)

    back_to_menu1 = pygame.draw.rect(screen2, color, (200, 300, 300, 70), 0)
    back_to_menu2 = pygame.draw.rect(screen2, color2, (205, 305, 300, 70), 0)
    font = pygame.font.SysFont('cmmi10', 50)
    text = font.render("BACK TO MENU", True, (3, 3, 68))
    text_xy = (220, 320)
    screen2.blit(text, text_xy)

    pygame.display.flip()

    running = True

    while running:

        draw_game_over(screen2)

        back_to_menu1 = pygame.draw.rect(screen2, color, (200, 300, 300, 70), 0)
        back_to_menu2 = pygame.draw.rect(screen2, color2, (205, 305, 300, 70), 0)
        font = pygame.font.SysFont('cmmi10', 50)
        text = font.render("BACK TO MENU", True, (3, 3, 68))
        text_xy = (220, 320)
        screen2.blit(text, text_xy)
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if back_to_menu1.collidepoint(mouse_pos):
                    sound1.play(0)
                    return

    pygame.quit()
