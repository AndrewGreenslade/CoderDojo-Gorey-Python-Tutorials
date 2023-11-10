import pygame

class Player():
    """
    contains the player object and allows for drawing of player on pygame window/users screen
    """

    def __init__(self, start_pos, size):
        """
            retains the players start position, and size, which are specified by the user,
            also contains the players color, which is green in this case.
        """
        self.color = "green"
        self.pos = start_pos
        self.size = size

    
    def DrawPlayer(self, screen):
        """
        draws player on the screen using pygame.draw() function
        """
        pygame.draw.circle(screen, self.color, self.pos, self.size)


    def movePlayer(self,keys,dt):
        """
            allows player to be moved by using W,S,A,D on users keyboard
        """
        if keys[pygame.K_w]:
            self.pos.y -= 300 * dt