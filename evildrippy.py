import pygame
from spritesheet import SpriteSheet

class EvilDrippy(pygame.sprite.Sprite):
    def __init__(self, x, y, platforms):
        super().__init__()
        self.image = pygame.image.load("grumps.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.platforms = platforms
        self.changex = 0
        self.changey = 0
        self.walkingright = []
        self.walkingleft = []
        spritesheet = SpriteSheet("grumpydrip.png")
        image = spritesheet.get_image(0,0,50,50)
        self.walkingright.append(image)
        self.walkingleft.append(pygame.transform.flip(image, True, False))
        image = spritesheet.get_image(50,0,50,50)
        self.walkingright.append(image)
        self.walkingleft.append(pygame.transform.flip(image, True, False))
        image = spritesheet.get_image(0,50,50,50)
        self.walkingright.append(image)
        self.walkingleft.append(pygame.transform.flip(image, True, False))
        image = spritesheet.get_image(50,50,50,50)
        self.walkingright.append(image)
        self.walkingleft.append(pygame.transform.flip(image, True, False))
    
    def update(self):
        self.gravity()
        self.move()
     
        pos_x = self.rect.x
        # You also need the y position for the vertical movement.
        pos_y = self.rect.y
        if self.changex > 0:
            frame = (pos_x // 30) % len(self.walkingright)
            self.image = self.walkingright[frame]
        if self.changex < 0:
            frame = (pos_x // 30) % len(self.walkingleft)
            self.image = self.walkingleft[frame]

    def goleft(self):
        self.changex = -3
    def goright(self):
        self.changex = 3
    def stop(self):
        self.changex = 0
    def gravity(self):
        if self.changey == 0:
            self.changey = 1
        else:
            self.changey += 0.35
        if self.rect.y >= 600 - self.rect.height and self.changey >= 0:
            self.changey = 0
            self.rect.y = 600 - self.rect.height
    def jump(self, platforms):
        self.rect.y += 2
        hitlist = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2
        if len(hitlist) > 0 or self.rect.bottom >= 800:
            self.changey = -10
    def move(self):
        
        self.rect.x += self.changex
        hitlist = pygame.sprite.spritecollide(self, self.platforms, False)
        for platform in hitlist:
            if self.changex > 0:
                self.rect.right = platform.rect.left
            if self.changex < 0:
                self.rect.left = platform.rect.right
        
        self.rect.y += self.changey
        hitlist = pygame.sprite.spritecollide(self, self.platforms, False)
        for platform in hitlist:
            if self.changey > 0:
                self.rect.bottom = platform.rect.top
            if self.changey < 0:
                self.rect.top = platform.rect.bottom
            
            # Stop our vertical movement
            self.changey = 0