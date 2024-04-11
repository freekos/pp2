import pygame as py

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

py.init()
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

radius = 50
pos_x, pos_y = (SCREEN_WIDTH // 2 - radius // 2), (SCREEN_HEIGHT // 2 - radius // 2)
delta = 20

def left():
    global pos_x
    if pos_x >= (delta + radius):
        pos_x -= delta

def right():
    global pos_x
    if pos_x <= (SCREEN_WIDTH - delta - radius):
        pos_x += delta

def up():
    global pos_y
    if pos_y >= (delta + radius):
        pos_y -= delta

def down():
    global pos_y
    if pos_y <= (SCREEN_HEIGHT - delta - radius):
        pos_y += delta

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                left()
            elif event.key == py.K_RIGHT:
                right()
            elif event.key == py.K_UP:
                up()
            elif event.key == py.K_DOWN:
                down()

    screen.fill((0, 0, 0))
    py.draw.circle(screen, "white", (pos_x, pos_y), radius)

    py.display.flip()
