import pygame
import webbrowser
import time
from level import Level1
from level import Level2
from level import Level3
from level import Level4
from level import Level5
from level import Menu
from fliptxt import FlipTxt
from pygame import mixer
from platform import Platform
from secretplatform import SecretPlatform
from icecream import IceCream
from evildrippy import EvilDrippy
from frozendrip import FrozenDrip
from spritesheet import SpriteSheet

shieldon = False

def shield(drippyimg):
    level.player.walkingright = []
    level.player.walkingleft = []
    spritesheet = SpriteSheet(drippyimg)

    image = spritesheet.get_image(0,0,50,50)
    level.player.walkingright.append(image)
    level.player.walkingleft.append(pygame.transform.flip(image, True, False))

    image = spritesheet.get_image(50,0,50,50)
    level.player.walkingright.append(image)
    level.player.walkingleft.append(pygame.transform.flip(image, True, False))

    image = spritesheet.get_image(0,50,50,50)
    level.player.walkingright.append(image)
    level.player.walkingleft.append(pygame.transform.flip(image, True, False))

    image = spritesheet.get_image(50,50,50,50)
    level.player.walkingright.append(image)
    level.player.walkingleft.append(pygame.transform.flip(image, True, False))

screenwidth = 800
screenheight = 600
lives = 2
icecreams = 0
dmgsound = mixer.Sound("dmg.mp3")
collect = mixer.Sound("icecreamsound.mp3")
levelup = mixer.Sound("levelup.mp3")
specialcrem = mixer.Sound("magic.mp3")
driphit = mixer.Sound("drip.mp3")
zap = mixer.Sound("zap.mp3")
pygame.init()

font = pygame.font.SysFont("comicsansms", 30)
screen = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption("random platformer")
clock = pygame.time.Clock()

levels = [Menu(), Level1(), Level2(), Level3(), Level4(), Level5()]
levelnumber = 4

playing = True
ehe = False

while playing == True:
    level = levels[levelnumber]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                level.player.goleft()

                if levelnumber >= 4 and (isinstance(level, Level4) or isinstance(level, Level5)):
                    level.evildrippy.goleft()
            if event.key == pygame.K_RIGHT:
                level.player.goright()
                if levelnumber >= 4 and (isinstance(level, Level4) or isinstance(level, Level5)):
                    level.evildrippy.goright()
            if event.key == pygame.K_SPACE:
                level.player.jump(level.platformlist) 
                if levelnumber >= 4 and (isinstance(level, Level4) or isinstance(level, Level5)): #we can fix this
                    level.evildrippy.jump(level.platformlist)
            if event.key == ord('r'):
                level.restart()

        if event.type == pygame.KEYUP:
            level.player.stop()
            if levelnumber >= 4 and (isinstance(level, Level4) or isinstance(level, Level5)):
                level.evildrippy.stop()

    if levelnumber >= 4 and (isinstance(level, Level4) or isinstance(level, Level5)): #we can fix this
        if (level.player.rect.x - 20 <= level.evildrippy.rect.x <= level.player.rect.x + 20) == False:
            if level.player.rect.x > level.evildrippy.rect.x:
                level.evildrippy.goright()
            if level.player.rect.x < level.evildrippy.rect.x:
                level.evildrippy.goleft()
            
    # Game Logic

    hitlist = pygame.sprite.spritecollide(level.player, level.itemlist, True)
    for icecream in hitlist:
        collect.play()
        print("u got ice cream!")
        icecreams += 1
        if icecreams >= 1 and levelnumber == 0:
            levelnumber += 1
            icecreams = 0
            levelup.play()

        elif icecreams >= 2 and levelnumber == 1:
            levelnumber += 1
            icecreams = 0
            levelup.play()

        elif icecreams >= 3 and levelnumber == 2:
            levelnumber += 1
            icecreams = 0
            levelup.play()

        elif icecreams == 1 and levelnumber == 3:
            levelnumber += 1
            icecreams = 0
            levelup.play()
            continue
            print(levelnumber)
            print(level)

        elif icecreams == 2 and levelnumber == 4:
            levelnumber += 1
            icecreams = 0
            levelup.play()
        
        elif icecreams == 2 and levelnumber == 5:
            # levelnumber += 1
            # icecreams = 0
            levelup.play()

    hitlist = pygame.sprite.spritecollide(level.player, level.triggerlist, True)
    
    for icecreamtrig in hitlist:
        ehe = True
        specialcrem.play()
        if levelnumber == 2:
            webbrowser.open("https://youtu.be/O91DT1pR1ew")
            jumpplatform = Platform(130, 20, 600, 250)
            level.platformlist.add(jumpplatform)
            jumpplatform = SecretPlatform(200, 20, screenwidth / 2 - 100, 135)
            level.platformlist.add(jumpplatform)
            icecream = IceCream(340, 90)
            level.itemlist.add(icecream)

        if levelnumber == 5:
            # t_end = time.time() + 10
            # while time.time() < t_end:
                shield("drippyshield.png")
                shieldon = True
            # shield("Drippywalksmall.png")
    
    if levelnumber >= 4 and (isinstance(level, Level4) or isinstance(level, Level5)):

        hitlist = pygame.sprite.spritecollide(level.evildrippy, level.triggerlist, True)
        
        for icecreamtrig in hitlist:
            ehe = True
            # if levelnumber == 4 and levels == Level4():
            zap.play()
            level.evildrippy.kill()
            frozendrip = FrozenDrip(400, 350)
            level.platformlist.add(frozendrip)

            icecream = IceCream(350, 100)
            level.itemlist.add(icecream)

    hitlist = pygame.sprite.spritecollide(level.player, level.enemylist, True)
    for rock in hitlist:
        dmgsound.play()
        lives -= 1
        print("you have " + str(lives) + " lives left")
        print("o no u hit a rock")
    if lives == 0:
        pygame.time.wait(1000)
        break

    hitlist = pygame.sprite.spritecollide(level.player, level.moblist, True)
    for evildrippy in hitlist:
        if shieldon == False:
            driphit.play()
            print("oh no! you hit evil drippy :(")
            print("you have " + str(lives) + " lives left")
            lives -= 2
            level.restart()
        elif shieldon == True:
            zap.play()
            # evildriprect = level.evildrippy.get_rect()
            level.evildrippy.kill()
            frozendrip = FrozenDrip(level.evildrippy.rect.x, (level.evildrippy.rect.y - 15))
            level.platformlist.add(frozendrip)
            shieldon = False
            shield("Drippywalksmall.png")
    if lives == 0:
        pygame.time.wait(1000)
        break

    pygame.display.update()
    level.update()
    screen.fill((0, 0, 0))
    level.draw(screen)
    if levelnumber == 0:
        title = font.render("arrows to move, space to jump", 1, (189, 209, 242))
        screen.blit(title, (screenwidth / 2 - title.get_width() / 2, screenheight / 6))
    if levelnumber == 4:
        title = font.render("this grumpy drippy seems to hate blue ice cream...", 1, (0, 117, 2))
        screen.blit(title, (screenwidth / 2 - title.get_width() / 2, 550))
    if levelnumber == 5:
        title = font.render("what happens if you eat the ice cream?", 1, (0, 117, 2))
        screen.blit(title, (screenwidth / 2 - title.get_width() / 2, 550))
    if ehe == True and levelnumber == 2:
        title = font.render("haha, gotcha ;)", 1, (189, 209, 242))
        screen.blit(title, (screenwidth / 2 - title.get_width() / 2, screenheight / 6))
        ehe == False
    if levelnumber == 3:
        fliptxt = FlipTxt(460, 50)
        level.platformlist.add(fliptxt)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
print("game over")