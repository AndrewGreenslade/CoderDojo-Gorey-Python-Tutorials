import pygame
import characters

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#Game objects setup
FirstPlayer = characters.Player( pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 40) 
SecondPlayer = characters.SpritePlayer() 

#Game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #managing input and moving player with it
    keys = pygame.key.get_pressed()
    FirstPlayer.movePlayer(keys, dt)
    SecondPlayer.movePlayer(keys, dt)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    FirstPlayer.DrawPlayer(screen)
    SecondPlayer.DrawPlayer(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()