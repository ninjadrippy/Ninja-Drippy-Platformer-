import pygame
import webbrowser
import time
import os
from level import *
from fliptxt import FlipTxt
from pygame import mixer
from platform import Platform
from secretplatform import SecretPlatform
from icecream import *
from evildrippy import EvilDrippy
from frozendrip import FrozenDrip
from heart import Heart
from spritesheet import SpriteSheet
import asyncio


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
lives = 3
maxlives = 3
icecreams = 0

pygame.mixer.init()

main_channel = pygame.mixer.Channel(0)
main_channel.set_volume(0.2)
main_channel.play(pygame.mixer.Sound("music.mp3"), loops=-1, fade_ms=5000)


dmgsound = mixer.Sound("dmg.mp3")
collect = mixer.Sound("icecreamsound.mp3")
collect.set_volume(0.2)
levelup = mixer.Sound("levelup.mp3")
specialcrem = mixer.Sound("magic.mp3")
driphit = mixer.Sound("drip.mp3")
zap = mixer.Sound("zap.mp3")

pygame.init()

font = pygame.font.SysFont("comicsansms", 30)
screen = pygame.display.set_mode([screenwidth, screenheight])
pygame.display.set_caption("random platformer")
clock = pygame.time.Clock()

levels = [Menu(), Level1(), Level2(), Level3(), Level4(), Level5(), Win(), GameOverMenu()]
levelnumber = 6

playing = True
ehe = False
hasDied = False

while playing == True:
    level = levels[levelnumber] if lives != 0 else levels[-1]

    def update_hearts(lives): 
        Heart.numberOfHearts = 0
        hearts = [Heart(True) if i < lives else Heart(False) for i in range(maxlives)]
        for heart in hearts: 
            level.platformlist.add(heart)
        return hearts

    HEARTS = update_hearts(lives)
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
            if event.key == ord('r') and level != levels[-1]:
                lives = maxlives
                update_hearts(lives)
                level.restart()

        if lives == 0 and not hasDied: 
            prev = level
            levels[-1] = GameOverMenu()
            hasDied = True

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
        
        elif icecreams == 2 and levelnumber == 5: #After this level is done we win
            levelnumber += 1
            icecreams = 0
            levelup.play()

            main_channel.pause()
            end_channel = pygame.mixer.Channel(1)
            end_channel.set_volume(0.2)
            end_channel.play(pygame.mixer.Sound("victory_music_again.mp3"), loops=-1, fade_ms=5000)

        if icecreams == 30 and isinstance(level, Win):
            levelup.play()
            level.portal.start("opening")
            level.portalSpawned = True
            print("The portal should be opening!")
            print(hitlist)

        if isinstance(level, Win) and level.portalSpawned == True and isinstance(icecream, Portal):
            levelup.play()
            levelnumber += 1

        if isinstance(icecream, Sundae) and icecream.option != 'quit':
            print("you restarted")
            levels = [Menu(), Level1(), Level2(), Level3(), Level4(), Level5(), GameOverMenu()]
            levelnumber = 0
            level = levels[levelnumber]
            lives = 3
            HEARTS = update_hearts(lives)
            level.restart()
            icecreams = 0
            levelup.play()

        elif isinstance(icecream, Sundae):
            print("you quit.")
            exit()

    hitlist = pygame.sprite.spritecollide(level.player, level.triggerlist, True)
    
    for icecreamtrig in hitlist:
        ehe = True
        specialcrem.play()
        if levelnumber == 2:
            main_channel.pause()
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
                main_channel.unpause()
                shield("drippyshield.png")
                shieldon = True
            # shield("Drippywalksmall.png")
        if levelnumber == 6:
            main_channel.pause()

            webbrowser.open("https://www.youtube.com/watch?v=oySU9DNaemU")
    
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
        update_hearts(lives)
        print("you have " + str(lives) + " lives left")
        print("o no u hit a rock")
    # if lives == 0:
    #     prev = level
    #     level = GameOverMenu()

    hitlist = pygame.sprite.spritecollide(level.player, level.moblist, True)
    for evildrippy in hitlist:
        if shieldon == False:
            driphit.play()
            print("oh no! you hit evil drippy :(")
            print("you have " + str(lives) + " lives left")
            temp = lives
            lives = maxlives - lives #set lives = 0
            update_hearts(lives)
            lives = temp #Reset lives back to max, bc we restart the level
            update_hearts(lives)
            level.restart()
        
        elif shieldon == True:
            zap.play()
            # evildriprect = level.evildrippy.get_rect()
            level.evildrippy.kill()
            frozendrip = FrozenDrip(level.evildrippy.rect.x, (level.evildrippy.rect.y - 15))
            level.platformlist.add(frozendrip)
            shieldon = False
            shield("Drippywalksmall.png")
    # if lives == 0:
    #     prev = level
    #     level = GameOverMenu()

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

    if levelnumber == 6: 
        level.portal.update()
        level.portal.draw(screen)

        if level.portal.collide(level.player) and level.portalSpawned == True:
            print("idk why this won't work")
            level.portal.start('closing')
            if level.portal.stage == 'done':
                levelup.play()
                levelnumber += 1

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
print("game over")