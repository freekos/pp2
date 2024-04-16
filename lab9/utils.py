import pygame as py
import os

def load_image(path: str) -> py.Surface:
    file_path = get_file_path(path)
    image = py.image.load(file_path)
    return image

def load_music(path: str):
    file_path = get_file_path(path)
    py.mixer.music.load(file_path)

def get_file_path(path: str) -> str:
    assets_path = get_assets_path()
    file_path = os.path.join(assets_path, path)
    return file_path

def get_assets_path():
    root = os.getcwd()
    return f"{root}/assets"
