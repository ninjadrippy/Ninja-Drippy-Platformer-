import pygame
from spritesheet import SpriteSheet

class FlipTxt(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("fliptxt.png")
        self.image = pygame.transform.scale(self.image, (268, 28))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y