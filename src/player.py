import pygame

# feast ur eyestalks on my sh^tty physics system

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((32, 32))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        # physics stuff
        self.yvel = 0
        self.xvel = 0
        self.speedx = 5
        self.speedy = 10

    def update(self):
        self.yvel = 0
        self.xvel = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.xvel -= self.speedx
        
        if keys[pygame.K_d]:
            self.xvel += self.speedx

        if keys[pygame.K_SPACE]:
            self.yvel -= self.speedy

    def move(self):
        self.rect.move_ip(self.xvel, self.yvel)
