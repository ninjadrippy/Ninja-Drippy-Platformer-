import pygame
from spritesheet import SpriteSheet

class Evilobstac(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("grumps.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y