# 通过名称获取图片资源
import os, pygame

sprites = {}


def load_sprites():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split(".")[0]] = pygame.image.load(os.path.join(path, file))


def get_sprite(name):
    return sprites[name]
