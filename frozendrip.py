import pygame
from spritesheet import SpriteSheet

class FrozenDrip(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("frozendrip.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y