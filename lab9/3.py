import pygame as py
import math

import utils

py.init()

fps = 60

timer = py.time.Clock()

WIDTH = 800
HEIGHT = 600

active_figure = 0
active_color = 'white'

screen = py.display.set_mode([WIDTH, HEIGHT])

py.display.set_caption("Paint")

painting = []

def draw_menu(color):
    py.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    py.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    circle_brush = [py.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    py.draw.circle(screen, 'white', (35, 35), 20)
    py.draw.circle(screen, 'black', (35, 35), 18)

    rect_brush = [py.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    py.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)

    square_brush = [py.draw.rect(screen, 'black', [130, 10, 50, 50]), 2]
    py.draw.rect(screen, 'white', [135, 15, 40, 40], 2)

    right_triangle_brush = [py.draw.rect(screen, 'black', [190, 10, 50, 50]), 3]
    py.draw.polygon(screen, 'white', [(195, 15), (195, 55), (235, 15)], 2)

    equilateral_triangle_brush = [py.draw.rect(screen, 'black', [250, 10, 50, 50]), 4]
    side_length = 50
    center_x = 250 + side_length / 2
    center_y = 10 + side_length / 2
    triangle_height = side_length * math.sqrt(3) / 2
    triangle_height *= 1
    vertex1 = (center_x, center_y - triangle_height / 2)
    vertex2 = (center_x - side_length / 2 * 0.9, center_y + triangle_height / 2 * 0.9)
    vertex3 = (center_x + side_length / 2 * 0.9, center_y + triangle_height / 2 * 0.9)
    py.draw.polygon(screen, 'white', [vertex1, vertex2, vertex3], 2)

    rhombus_brush = [py.draw.rect(screen, 'black', [310, 10, 50, 50]), 5]
    top_left = (310, 10)
    top_right = (360, 10)
    bottom_left = (310, 60)
    bottom_right = (360, 60)
    mid_top = ((top_left[0] + top_right[0]) // 2, (top_left[1] + top_right[1]) // 2 + 4)
    mid_left = ((top_left[0] + bottom_left[0]) // 2 + 4, (top_left[1] + bottom_left[1]) // 2)
    mid_bottom = ((bottom_left[0] + bottom_right[0]) // 2, (bottom_left[1] + bottom_right[1]) // 2 - 4)
    mid_right = ((top_right[0] + bottom_right[0]) // 2 - 4, (top_right[1] + bottom_right[1]) // 2)
    py.draw.polygon(screen, 'white', [mid_top, mid_left, mid_bottom, mid_right], 2)

    brush_list = [circle_brush, rect_brush, square_brush, right_triangle_brush, equilateral_triangle_brush,
                  rhombus_brush]

    py.draw.circle(screen, color, (400, 35), 30)
    py.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    eraser = utils.load_image("Eraser.svg")
    eraser_rect = eraser.get_rect(topleft=(WIDTH - 150, 7))
    eraser_rect.width = eraser_rect.height = 25
    screen.blit(eraser, [WIDTH - 150, 7, 25, 25])

    blue = py.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = py.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = py.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = py.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = py.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = py.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = py.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list


def draw_painting(paints):
    for color, pos, figure in paints:
        if color == (255, 255, 255):
            py.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 50])
        else:
            if figure == 0:
                py.draw.circle(screen, color, pos, 20, 2)
            elif figure == 1:
                py.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)
            elif figure == 2:
                py.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 35, 35], 2)
            elif figure == 3:
                py.draw.polygon(screen, color, [(pos[0] - 15, pos[1] - 15),
                                                    (pos[0] - 15, pos[1] + 35),
                                                    (pos[0] + 35, pos[1] - 15)], 2)
            elif figure == 4:
                size = 50
                triangle_height = size * math.sqrt(3) / 2
                vertex1 = (pos[0], pos[1] - triangle_height / 2)
                vertex2 = (pos[0] - size / 2, pos[1] + triangle_height / 2)
                vertex3 = (pos[0] + size / 2, pos[1] + triangle_height / 2)
                py.draw.polygon(screen, color, [vertex1, vertex2, vertex3], 2)
            elif figure == 5:
                py.draw.polygon(screen, color, [(pos[0] - 25, pos[1]),
                                                    (pos[0], pos[1] - 25),
                                                    (pos[0] + 25, pos[1]),
                                                    (pos[0], pos[1] + 25)], 2)


run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = py.mouse.get_pos()
    left_click = py.mouse.get_pressed()[0]
    brushes, colors, rgbs = draw_menu(active_color)
    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure))
    draw_painting(painting)
    if mouse[1] > 85:
        if active_color == (255, 255, 255):
            py.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 50])
        else:
            if active_figure == 0:
                py.draw.circle(screen, active_color, mouse, 20, 2)
            elif active_figure == 1:
                py.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)
            elif active_figure == 2:
                py.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 35, 35], 2)
            elif active_figure == 3:
                py.draw.polygon(screen, active_color, [(mouse[0] - 15, mouse[1] - 15),
                                                           (mouse[0] - 15, mouse[1] + 35),
                                                           (mouse[0] + 35, mouse[1] - 15)], 2)
            elif active_figure == 4:
                size = 50
                triangle_height = size * math.sqrt(3) / 2
                vertex1 = (mouse[0], mouse[1] - triangle_height / 2)
                vertex2 = (mouse[0] - size / 2, mouse[1] + triangle_height / 2)
                vertex3 = (mouse[0] + size / 2, mouse[1] + triangle_height / 2)
                py.draw.polygon(screen, active_color, [vertex1, vertex2, vertex3], 2)
            elif active_figure == 5:
                py.draw.polygon(screen, active_color, [(mouse[0] - 25, mouse[1]),
                                                           (mouse[0], mouse[1] - 25),
                                                           (mouse[0] + 25, mouse[1]),
                                                           (mouse[0], mouse[1] + 25)], 2)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        if event.type == py.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]

        py.display.flip()

py.quit()
