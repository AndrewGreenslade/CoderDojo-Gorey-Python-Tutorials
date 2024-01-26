# Example file showing a basic pygame "game loop"
import pygame
from tilemap import room

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
FirstRoom = room(pygame.math.Vector2(100,100))

# Initializing RGB GB Color
BGColor = (0, 0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Changing BG color
    screen.fill(BGColor)

    # RENDER YOUR GAME HERE
    FirstRoom.drawRoom(screen)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()