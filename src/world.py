import pygame
import block
import noise
import random

WORLD_LENGTH = 960//block.BLOCK_SIZE
FILLER_THICKNESS = 3

# create the random list
pos_list = noise.generate(6, 10, WORLD_LENGTH)

def start_wgen(spriteGroup:pygame.sprite.Group, allSprites:pygame.sprite.Group):
    b = block.Block(2)
    b.rect.move_ip(0, pos_list[0]*block.BLOCK_SIZE)
    for i in range(1, FILLER_THICKNESS):
        b2 = block.Block(1)
        b2.rect.move_ip(0, (pos_list[0]+i)*block.BLOCK_SIZE)
        spriteGroup.add(b2)
        allSprites.add(b2)

    # RENDERER PASS #
    spriteGroup.add(b)
    allSprites.add(b)

def world(spriteGroup:pygame.sprite.Group, allSprites:pygame.sprite.Group):

    for i in range(WORLD_LENGTH-1):
        b = block.Block(2)
        b.rect.move_ip((i+1)*block.BLOCK_SIZE, pos_list[i+1]*block.BLOCK_SIZE)

        for j in range(1, FILLER_THICKNESS):
            b2 = block.Block(1)
            b2.rect.move_ip((i+1)*block.BLOCK_SIZE, (pos_list[i+1]+j)*block.BLOCK_SIZE)
            spriteGroup.add(b2)
            allSprites.add(b2)

        # RENDERER PASS #
        spriteGroup.add(b)
        allSprites.add(b)
