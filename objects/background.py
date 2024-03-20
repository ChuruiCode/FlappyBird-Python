# 游戏主背景
from typing import Any
import pygame.sprite
import assets
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.BACKGROUND
        self.sprite_name = "background"
        bg_image = assets.get_sprite("background").convert()
        # 创建矩形绘制区域 宽度为两倍，横向放置两张图片
        self.image = pygame.Surface((bg_image.get_width() * 2, bg_image.get_height()))
        # 图片放置位置
        self.image.blit(bg_image, (0, 0))
        self.image.blit(bg_image, (bg_image.get_width(), 0))

        # 检查 self.image 是否是有效的 Pygame 表面
        self.rect = self.image.get_rect(topleft=(0, 0))

        self.pos = pygame.math.Vector2(self.rect.topleft)

        super().__init__(*groups)

    def update(self, dt):
        self.pos.x -= 200 * dt
        self.rect.x = round(self.pos.x)
        # print("self.pos.x", self.pos.x)
        if self.rect.centerx <= 0:
            self.pos.x = 0
