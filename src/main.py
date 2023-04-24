import pygame
import world
import player
import game_util

game_util.log("Welcome!")
# variables
SCREEN_W = 960
SCREEN_H = 512
FPS = 60
SKY_COLOR = (80, 90, 255)

chunk_updates = 0
version = "0.0.5.a_01 ('crap physics update')"

clock = pygame.time.Clock()
game_util.log("Created variables")

# init pygame
pygame.init()
pygame.font.init()
game_util.log("Initialized pygame")

# create the screen
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Loading...")
game_util.log("Created window")

# sprite groups
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

# minecraft font
font = pygame.font.Font("./assets/font.ttf", 32)
game_util.log("Loaded sprite groups and font")

# create player
plr = player.Player()
all_sprites.add(plr)
game_util.log("Player.__init__() bug-free")

#=====MAIN LOOP=====#

# TODO: better worldgen
world.start_wgen(blocks, all_sprites)
world.world(blocks, all_sprites)
game_util.log("Generated world data.")

game_util.log("Starting main loop...")
while True:
    
    # fill the screen with the sky color
    window.fill(SKY_COLOR)

    # scan game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_util.log("QUIT event scanned and found")
            game_util.log("Ignore any error like 'pygame.error: display surface quit.' Those do not mean anything")
            pygame.quit()

    # set the window title to the frames per second
    pygame.display.set_caption("GAME")

    for sprite in all_sprites:
        window.blit(sprite.surf, sprite.rect)

    # update the player
    plr.update()

    # make player fall and collide

    bcollide = pygame.sprite.spritecollideany(plr, blocks)
    if not bcollide:
        plr.rect.move_ip(0, 4)
    
    if bcollide:
        plr.rect.move_ip(0, -4)

    plr.move()


    # render the frames per second onscreen
    fps_text = font.render(str(int(clock.get_fps())) + " FPS, " + str(chunk_updates) + " chunk updates", False, (255, 255, 255))
    window.blit(fps_text, (16, 16))

    # render the amount of block onscreen and the version number
    block_text = font.render(str(len(blocks.sprites())) + " blocks currently rendered", False, (255, 255, 255))
    window.blit(block_text, (16, 32))

    version_text = font.render("i progamd fisics in 10 minits at 11 pm so is bad", False, (255, 255, 255))
    window.blit(version_text, (16, 48))

    # reload the display
    clock.tick(FPS)
    pygame.display.flip()
