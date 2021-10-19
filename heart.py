import pygame
from spritesheet import SpriteSheet

class Heart(pygame.sprite.Sprite):
    numberOfHearts = 0
    spacing = 50
    def __init__(self, healthy):
        super().__init__()
        spritesheet = SpriteSheet("heart.png")
        self.healthy = spritesheet.get_image(0, 0, 20, 20)
        self.broken = spritesheet.get_image(0, 20, 20, 40)
        if healthy: 
            self.image = self.healthy
            self.image = pygame.transform.scale2x(self.image) #healthy version
        else: 
            self.image = self.broken
            self.image = pygame.transform.scale2x(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.x = 10 + Heart.spacing * Heart.numberOfHearts
        self.rect.y = 555
        Heart.numberOfHearts += 1

    def change_heart(self): 
        if self.image == self.healthy:
            self.image = self.broken
        else: 
            self.image = self.healthy
    