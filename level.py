import pygame
from icecream import IceCream
from icecream import Sundae
from player import Player
from platform import Platform
from obstacle import Obstacle
from icecreamtrig import IceCreamTrig
from secretplatform import SecretPlatform
from evildrippy import EvilDrippy
from evilobstac import Evilobstac

pygame.init()
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode([screenwidth, screenheight])
font = pygame.font.SysFont("comicsansms", 30)

class Level:
    def __init__(self):
        self.platformlist = pygame.sprite.Group()
        self.itemlist = pygame.sprite.Group()
        self.enemylist = pygame.sprite.Group()
        self.spritelist = pygame.sprite.Group()
        self.triggerlist = pygame.sprite.Group()
        self.moblist = pygame.sprite.Group()
        # self.textlist = pygame.sprite.Group()

        # Create outer wall/screen boundaries
        testwall = Platform(20, 600, 0, 0)
        self.platformlist.add(testwall)
        testwall = Platform(20, 600, 780, 0)
        self.platformlist.add(testwall)
        ceiling = Platform(800, 20, 0, 0)
        self.platformlist.add(ceiling)
        testplatform = Platform(800, 50, 0, 550)
        self.platformlist.add(testplatform)

    def update(self):
        self.platformlist.update()
        self.itemlist.update()
        self.enemylist.update()
        self.spritelist.update()
        self.triggerlist.update()
        self.moblist.update()

    def draw(self, screen):
        self.platformlist.draw(screen)
        self.enemylist.draw(screen)
        self.itemlist.draw(screen)
        self.spritelist.draw(screen)
        self.triggerlist.draw(screen)
        self.moblist.draw(screen)

    def restart(self):
        self = self.__init__()

class Level1(Level):
    def __init__(self):
        super().__init__()
        
        self.player = Player(50, 50, self.platformlist)
        self.spritelist.add(self.player)

        jumpplatform = Platform(200, 20, 600, 450)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(200, 20, 100, 375)
        self.platformlist.add(jumpplatform)

        icecream = IceCream(625, 425)
        self.itemlist.add(icecream)

        icecream = IceCream(150, 350)
        self.itemlist.add(icecream)

        Rock = Obstacle(100, 355)
        self.enemylist.add(Rock)

        Rock = Obstacle(650, 430)
        self.enemylist.add(Rock)

        Rock = Obstacle(400, 530)
        self.enemylist.add(Rock)
class Level2(Level):
    def __init__(self):
        super().__init__()

        self.player = Player(50, 50, self.platformlist)
        self.spritelist.add(self.player)

        icecream = IceCream(625, 425)
        self.itemlist.add(icecream)

        icecream = IceCream(400, 200)
        self.itemlist.add(icecream)

        mutanticecream = IceCreamTrig(450, 460)
        self.triggerlist.add(mutanticecream)

        jumpplatform = Platform(130, 20, 400, 500)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(130, 20, 400, 400)
        self.platformlist.add(jumpplatform)

        Rock = Obstacle(400, 480)
        self.enemylist.add(Rock)

class Level3(Level):
    def __init__(self):
        super().__init__()

        self.player = Player(50, 50, self.platformlist)
        self.spritelist.add(self.player)

        jumpplatform = Platform(20, 600, 390, 0)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(60, 20, 450, 500)
        self.platformlist.add(jumpplatform)

        jumpplatform = SecretPlatform(60, 20, 290, 500)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(60, 20, 600, 400)
        self.platformlist.add(jumpplatform)

        jumpplatform = SecretPlatform(60, 20, 130, 400)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(30, 20, 500, 250)
        self.platformlist.add(jumpplatform)

        jumpplatform = SecretPlatform(30, 20, 270, 250)
        self.platformlist.add(jumpplatform)

        icecream = IceCream(200, 25)
        self.itemlist.add(icecream)

        jumpplatform = Platform(35, 20, 600, 120)
        self.platformlist.add(jumpplatform)

        jumpplatform = SecretPlatform(35, 20, 165, 120)
        self.platformlist.add(jumpplatform)

class Level4(Level):
    def __init__(self):
        super().__init__()

        self.player = Player(50, 50, self.platformlist)
        self.spritelist.add(self.player)

        self.evildrippy = EvilDrippy(400, 50, self.platformlist)
        self.moblist.add(self.evildrippy)

        jumpplatform = Platform(300, 20, 100, 140)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(300, 20, 550, 140)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(20, 500, 100, 0)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(40, 20, 680, 440)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(260, 20, 210, 400)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(20, 190, 450, 210)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(20, 30, 530, 320)
        self.platformlist.add(jumpplatform)

        mutanticecream = IceCreamTrig(430, 370)
        self.triggerlist.add(mutanticecream)

        icecream = IceCream(375, 200)
        self.itemlist.add(icecream)

class Level5(Level):
    def __init__(self):
        super().__init__()

        self.player = Player(50, 50, self.platformlist)
        self.spritelist.add(self.player)

        self.evildrippy = EvilDrippy(360, 50, self.platformlist)
        self.moblist.add(self.evildrippy)

        jumpplatform = Platform(300, 20, 100, 140)
        self.platformlist.add(jumpplatform)

        icecream = IceCream(150, 100)
        self.itemlist.add(icecream)

        icecream = IceCream(200, 100)
        self.itemlist.add(icecream)

        jumpplatform = Platform(20, 500, 100, 0)
        self.platformlist.add(jumpplatform)

        mutanticecream = IceCreamTrig(300, 500)
        self.triggerlist.add(mutanticecream)

        jumpplatform = Platform(50, 20, 420, 280)
        self.platformlist.add(jumpplatform)

        jumpplatform = Platform(50, 20, 600, 320)
        self.platformlist.add(jumpplatform)

class Menu(Level):
    def __init__(self):
        super().__init__()

        self.player = Player(50, 50, self.platformlist)
        self.spritelist.add(self.player)

        icecream = IceCream(330, 520)
        self.itemlist.add(icecream)

        title = font.render("hi", 1, (189, 209, 242))
        screen.blit(title, (0, 0))
        pygame.display.update()

        # pygame_gui library

class GameOverMenu(Level):
    def __init__(self, prev=0):
        super().__init__()

        self.player = Player(360, 480, self.platformlist)
        self.spritelist.add(self.player)

        restart = Sundae(200, 480, 'restart')
        leave = Sundae(520, 480, 'quit')
        self.itemlist.add(restart)
        self.itemlist.add(leave)

        title = font.render("GAME OVER", 1, (255, 255, 255))
        screen.blit(title, (0, 0))
        pygame.display.update()
