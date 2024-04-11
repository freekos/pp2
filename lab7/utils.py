import pygame as py
import os

def load_image(path: str) -> py.Surface:
    root = os.getcwd()
    file_path = os.path.join(f"{root}/assets", path)
    image = py.image.load(file_path)
    return image
