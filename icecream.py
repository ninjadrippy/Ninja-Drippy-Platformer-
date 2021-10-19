import pygame
from spritesheet import SpriteSheet

class IceCream(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("icecream.png")
        self.image = pygame.transform.scale(self.image, (10, 19))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Sundae(pygame.sprite.Sprite):
    sprites = {'restart': 'sundae.png', 
               'quit': 'quitcream.png' 
               }
    def __init__(self, x, y, option):
        super().__init__()
        self.option = option
        self.image = pygame.image.load(Sundae.sprites[option])
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
