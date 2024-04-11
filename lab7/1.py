import time
import pygame as py

import utils

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
SCREEN_CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

py.init()
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

micky_clock = py.transform.scale(utils.load_image("MickyClock.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
micky_left_hand = utils.load_image("MickyLeftHand.png").convert_alpha()
micky_right_hand = utils.load_image("MickyRightHand.png").convert_alpha()

def draw_hand(image: py.image, angle: int):
    rotated_image = py.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=SCREEN_CENTER)

    screen.blit(rotated_image, new_rect)

def draw_clock():
    screen.blit(micky_clock, (0, 0))

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()

    draw_clock()

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    print(minutes, seconds)

    second_angle = ((seconds % 60) / 60) * 360 - 87
    minute_angle = ((minutes % 60) / 60) * 360 - 87

    draw_hand(micky_left_hand, -second_angle)
    draw_hand(micky_right_hand, -minute_angle)

    py.display.flip()
    py.time.delay(1000//60)
