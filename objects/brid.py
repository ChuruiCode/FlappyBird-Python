import pygame, assets, configs

from random import randint
from layer import Layer


class Brid(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER
        self.sprite_name = "brid"
        self.import_frames()
        self.frams_index = 0
        self.image = self.frams[self.frams_index]

        # self.rect = self.image.get_rect(midleft=(0, (configs.SCREEN_HEIGHT - assets.get_sprite("floor").convert().get_height()) / 2))
        self.rect = self.image.get_rect(topleft=(-50, 50))

        self.pos = pygame.math.Vector2(self.rect.topleft)

        # 下降重力值
        self.gravity = 800
        # 方向
        self.direction = 0

        # mask
        self.mask = pygame.mask.from_surface(self.image)

        super().__init__(*groups)

    def import_frames(self):
        self.frams = [
            assets.get_sprite("redbird-downflap").convert_alpha(),
            assets.get_sprite("redbird-midflap").convert_alpha(),
            assets.get_sprite("redbird-upflap").convert_alpha(),
        ]

    def start_action(self, dt):
        if self.pos.x < configs.START_POSITION:
            self.pos.x += 200 * dt
            self.rect.x = round(self.pos.x)

    def animate(self, dt):
        self.frams_index += 10 * dt
        if self.frams_index >= len(self.frams):
            self.frams_index = 0
        self.image = self.frams[int(self.frams_index)]

    def apply_gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

        if int(self.pos.y) < 0:
            # 判断小鸟的高度超出平米上方-100限制爬升
            self.pos.y = 0

    def jump(self):
        self.direction = -configs.JUMP_HEIGHT

    def rotate(self):
        # 旋转角度
        rotate_bird = pygame.transform.rotozoom(self.image, -self.direction * 0.06, 1)
        self.image = rotate_bird

        # mask
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.start_action(dt)
        self.animate(dt)
        self.apply_gravity(dt)
        self.rotate()
        # print("self.rect.x", self.rect.x)
        # print("self.rect.left", self.rect.left)
        # print("self.rect.centerx", self.rect.centerx)
        # print("self.rect.right", self.rect.right)
