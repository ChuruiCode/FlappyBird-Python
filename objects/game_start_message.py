import pygame, assets, configs

from random import randint

from layer import Layer


class GameStartMessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.sprite_name = "game_start_message"
        self.image = assets.get_sprite("message").convert_alpha()
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 2))

        super().__init__(*groups)
