import pygame, assets, configs
from layer import Layer


class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        # 分数值
        self.value = 0
        # 创建一个半透明的画布
        self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)

        self.__create()

        super().__init__(*groups)

    def __create(self):
        self.images = []
        self.width = 0
        self.str_value = str(self.value)
        for str_value_char in self.str_value:
            img = assets.get_sprite(str_value_char)
            self.images.append(img)
            self.width += img.get_width()
        self.height = self.images[0].get_height()
        self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, 50))

        x = 0
        for img in self.images:
            self.image.blit(img, (x, 0))
            x += img.get_width()

    def update(self, dt):
        self.__create()
