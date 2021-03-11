import pygame

class Rocket(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/ship.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

    def update(self, *args):
        #Logica
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 5

        elif keys[pygame.K_a]:
            self.rect.x -= 5

        elif keys[pygame.K_s]:
            self.rect.y += 5

        elif keys[pygame.K_d]:
            self.rect.x += 5

        elif keys[pygame.K_UP]:
            self.rect.y -= 5

        elif keys[pygame.K_DOWN]:
            self.rect.y += 5

        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5

        elif keys[pygame.K_LEFT]:
            self.rect.x -= 5

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 768:
            self.rect.bottom = 768
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1024:
            self.rect.right = 1024
