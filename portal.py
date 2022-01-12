import pygame
from spritesheet import SpriteSheet

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.opening = []
        self.idle = []
        self.closing = []
        for i in range(17):
            spritesheet = SpriteSheet(f"portals/portal-{i}.png")
            res = (200, 150)
            # self.idle.append(pygame.transform.scale(spritesheet.get_image(0,0,256,256), res))  # x, y, x + offset, y + offset
            # self.closing.append(pygame.transform.scale(spritesheet.get_image(256,0,512,256), res))
            # self.opening.append(pygame.transform.scale( spritesheet.get_image(0,256,256,512), res))
            self.idle.append(pygame.transform.flip(spritesheet.get_image(0,0,256,256), True, False)) # x, y, x + offset, y + offset
            self.closing.append(pygame.transform.flip(spritesheet.get_image(256,0,512,256), True, False))
            self.opening.append(pygame.transform.flip(spritesheet.get_image(0,256,256,512), True, False))

        self.sprites = {
            "opening": self.opening,
            "idle": self.idle,
            "closing": self.closing
        }
        self.stage = ''
        self.image_count = 0
        self.image = self.opening[0]
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x + 150, self.y + 150, 20, 20)


    def start(self, stage):
        self.stage = stage 

    def update(self):
        if self.stage == '':
            return
        
        self.image_count += 1

        stage = self.stage 
        if stage == 'opening':
            image = self.opening if self.image_count == len(self.opening) - 1 else self.idle
        if stage == 'idle':
            image = self.idle
        if stage == 'closing':
            image = self.closing
        if stage == 'done': 
            self.image = self.opening[0]
            return
        self.image_count = self.image_count % len(self.opening) if not (self.image_count % len(self.closing) == 0 and image == self.closing) else self.closing[-1]
        self.image = image[self.image_count]
        if self.image == self.closing[-1]:
            self.stage = 'done'

    def draw(self, screen): 
        new_rect = self.image.get_rect(center = (self.x, self.y))
        screen.blit(self.image, new_rect.center)

    def collide(self, player): 
        get_mask = lambda img: pygame.mask.from_surface(img)
        drippy_mask = get_mask(player.image)
        portal_mask = get_mask(self.image)
        b_point = drippy_mask.overlap(portal_mask, (self.x - player.rect.x, self.y - round(player.rect.y)))
        if b_point: 
            return True
        return False

