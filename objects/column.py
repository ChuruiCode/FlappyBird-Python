import pygame, assets, configs

from random import randint
from layer import Layer


class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.OBSTACLE
        self.sprite_name = "column"
        floor_height = assets.get_sprite("floor").get_height()
        bottom_image = assets.get_sprite("pipe-green").convert()
        column_height = bottom_image.get_height()
        top_image = pygame.transform.flip(bottom_image, False, True)
        self.image = pygame.Surface((bottom_image.get_width(), configs.SCREEN_HEIGHT - floor_height), pygame.SRCALPHA)
        # self.image.blit(bottom_image, (0, 200))
        max_y = 300
        min_y = 100
        gap = 100
        # print(self.image.get_height())
        # bottom_y
        # self.image.blit(top_image, (0, -(column_height - col_y)))
        random_y = randint(min_y, max_y)
        self.image.blit(top_image, (0, -random_y))
        self.image.blit(bottom_image, (0, column_height - random_y + gap))
        # self.image.blit(bottom_image, (0, 0))

        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH, 0))

        self.pos = pygame.math.Vector2(self.rect.topleft)

        # mask
        self.mask = pygame.mask.from_surface(self.image)

        # 管道是否通过
        self.passed = False

        super().__init__(*groups)

    # 管道通过小鸟下方得分
    def is_passed(self):
        if self.rect.x < configs.START_POSITION and not self.passed:
            self.passed = True
            return True
        return False

    def update(self, dt):
        self.pos.x -= 100 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()
