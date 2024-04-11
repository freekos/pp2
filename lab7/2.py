import os
import pygame as py

import utils

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
SCREEN_CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

py.init()
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def collect_music_files(folder_path):
    music_files = []

    for root, dir, files in os.walk(folder_path):
        for file in files:
            if file.startswith("music-") and file.endswith(".mp3"):
                music_files.append(file)

    return music_files

musics = collect_music_files(utils.get_assets_path())
is_pause, music_i = False, None

def play():
    global music_i
    music_i = 0
    utils.load_music(musics[music_i])
    py.mixer.music.play()

def pause():
    global is_pause
    if is_pause:
        py.mixer.music.unpause()
        is_pause = False
    else:
        py.mixer.music.pause()
        is_pause = True

def stop():
    global music_i
    py.mixer.music.stop()
    music_i = None

def next():
    global music_i
    if (music_i == None or music_i >= len(musics) - 1):
        music_i = 0
    else:
        music_i += 1
    utils.load_music(musics[music_i])
    py.mixer.music.play()

def prev():
    global music_i
    if music_i == None:
        music_i = 0
    elif music_i <= 0:
        music_i = len(musics) - 1
    else:
        music_i -= 1
    utils.load_music(musics[music_i])
    py.mixer.music.play()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                if music_i == None:
                    play()
                else:
                    pause()
            elif event.key == py.K_RETURN:
                stop()
            elif event.key == py.K_RIGHT:
                next()
            elif event.key == py.K_LEFT:
                prev()
    py.display.flip()
