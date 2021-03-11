import pygame
from rocket import Rocket
from asteroid import Asteroid
from shot import Shot
import emoji
import random

pygame.init()
display = pygame.display.set_mode([1024, 768])
pygame.display.set_caption(emoji.emojize('Pandemic in space :rocket:', use_aliases=True))

#Objects

objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

#Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load('data/galaxy2.png')
bg.image = pygame.transform.scale(bg.image, [1024, 768])
bg.rect = bg.image.get_rect()

rocket = Rocket(objectGroup)
asteroid = Asteroid(objectGroup)
asteroid2 = Asteroid(objectGroup)
asteroid3 = Asteroid(objectGroup)
asteroid4 = Asteroid(objectGroup)

#Music
pygame.mixer.music.load('data/space.mp3')
pygame.mixer.music.play(-1)

#Sounds
shoot = pygame.mixer.Sound('data/shoot.wav')

gameLoop = True
timer = 20
clock = pygame.time.Clock()
if __name__ == '__main__':
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = rocket .rect.center


        #Update:
        objectGroup.update()

        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.3:
                newAsteroid = Asteroid(objectGroup, asteroidGroup)

        collisions = pygame.sprite.spritecollide(rocket, asteroidGroup, False)

        if collisions:
            print('Game Over!')
            gameLoop = False

        hits = pygame.sprite.groupcollide(shotGroup, asteroidGroup, True, True)

        #Draw:
        display.fill([0, 0, 0])
        objectGroup.draw(display)

        pygame.display.update()
