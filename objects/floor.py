import pygame
import assets, configs
from layer import Layer


class Floor(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.FLOOR
        self.sprite_name = "floor"
        bg_image = assets.get_sprite("floor").convert()
        # 相同图片拼接两张
        self.image = pygame.Surface((bg_image.get_width() * 2, bg_image.get_height()))
        # 图片放置位置
        self.image.blit(bg_image, (0, 0))
        self.image.blit(bg_image, (bg_image.get_width(), 0))

        # 检查 self.image 是否是有效的 Pygame 表面
        self.rect = self.image.get_rect(bottomleft=(0, configs.SCREEN_HEIGHT))

        self.pos = pygame.math.Vector2(self.rect.topleft)

        # mask
        self.mask = pygame.mask.from_surface(self.image)

        super().__init__(*groups)

    def update(self, dt):
        self.pos.x -= 150 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.centerx <= 0:
            self.pos.x = 0
