import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#Game objects setup - HINT: place player creation line near here!

#Game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #getting pressed keys and storing them in a variable every frame
    keys = pygame.key.get_pressed()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR gameobjects here


    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(30) / 1000

pygame.quit()