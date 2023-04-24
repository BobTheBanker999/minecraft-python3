import pygame

BLOCK_SIZE = 32 # pixels

BLOCK_IDS = {
    "stone":0,
    "dirt":1,
    "grass":2
}

TEXTURES = ["./assets/stone.png", "./assets/dirt.png", "./assets/grass.png"]

class Block(pygame.sprite.Sprite):

    def __init__(self, blockId:int):
        super(Block, self).__init__()

        self.surf = pygame.image.load(TEXTURES[blockId])
        self.rect = self.surf.get_rect()
        
