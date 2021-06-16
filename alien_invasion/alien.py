import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        """初始化外星人，并设置其起始位置。"""
        super().__init__()
        self.screen = ai_game.screen

        #加载外星人图像并设置其rect属性
        self.image = pygame.image.load('alien_invasion\\images\\alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


