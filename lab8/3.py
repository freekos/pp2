import pygame

import utils

pygame.init()

# Constants
FPS = 60
WIDTH = 800
HEIGHT = 600
MENU_HEIGHT = 70
BRUSH_SIZE = 20
WHITE = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
timer = pygame.time.Clock()
painting = []

def draw_menu(color):
    screen.fill((128, 128, 128), [0, 0, WIDTH, MENU_HEIGHT])
    pygame.draw.line(screen, (0, 0, 0), (0, MENU_HEIGHT), (WIDTH, MENU_HEIGHT), 3)

    circle_brush_rect = pygame.draw.rect(screen, (0, 0, 0), [10, 10, 50, 50])
    pygame.draw.circle(screen, WHITE, (35, 35), 20)
    pygame.draw.circle(screen, (0, 0, 0), (35, 35), 18)

    rect_brush_rect = pygame.draw.rect(screen, (0, 0, 0), [70, 10, 50, 50])
    pygame.draw.rect(screen, WHITE, [76.5, 26, 37, 20], 2)

    eraser_img = utils.load_image("Eraser.svg")
    eraser_rect = eraser_img.get_rect(topleft=(WIDTH - 150, 7))
    eraser_rect.width = eraser_rect.height = 25
    screen.blit(eraser_img, eraser_rect)

    colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
              (0, 255, 255), (255, 0, 255), (0, 0, 0)]
    color_rects = []
    for i, col in enumerate(colors):
        color_rect = pygame.draw.rect(screen, col, [WIDTH - 35 - 25 * i, 10 + 25 * (i % 4), 25, 25])
        color_rects.append(color_rect)

    return [(circle_brush_rect, 0), (rect_brush_rect, 1)], color_rects, colors

def draw_painting(paints):
    for color, pos, figure in paints:
        if color == WHITE:
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])
        else:
            if figure == 0:
                pygame.draw.circle(screen, color, pos, 20, 2)
            elif figure == 1:
                pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)

# Main loop
active_figure = 0
active_color = WHITE

run = True
while run:
    timer.tick(FPS)
    screen.fill(WHITE)
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    brushes, colors, rgbs = draw_menu(active_color)

    if left_click and mouse[1] > MENU_HEIGHT:
        painting.append((active_color, mouse, active_figure))
    draw_painting(painting)

    if mouse[1] > MENU_HEIGHT:
        if active_color == WHITE:
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20])
        else:
            if active_figure == 0:
                pygame.draw.circle(screen, active_color, mouse, 20, 2)
            elif active_figure == 1:
                pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for brush_rect, figure in brushes:
                if brush_rect.collidepoint(event.pos):
                    active_figure = figure

    pygame.display.flip()

pygame.quit()
