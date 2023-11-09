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
            allows player to be movesd by using W,S,A,D on users keyboard
        """
        if keys[pygame.K_w]:
            self.pos.y -= 300 * dt
        if keys[pygame.K_s]:
            self.pos.y += 300 * dt
        if keys[pygame.K_a]:
            self.pos.x -= 300 * dt
        if keys[pygame.K_d]:
            self.pos.x += 300 * dt



class SpritePlayer():
    """
        contains the player object and allows for drawing of player on pygame window/users screen
    """
    
    def __init__(self):
        """
        Runs when the object is first created, also loads a image called 'square.png'
        """
        self.image = pygame.image.load("./square.png")
        self.rect = self.image.get_rect()
    

    def DrawPlayer(self, screen):
        """
        draws player on the screen using pygame.blit()
        """
        screen.blit(self.image, self.rect)

    
    def movePlayer(self,keys,dt):
        """
        allows player sprite to be moved by using arrow keys on users keyboard
        """
        if keys[pygame.K_UP]:
            self.rect.y -= 300 * dt
        if keys[pygame.K_DOWN]:
            self.rect.y += 300 * dt
        if keys[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if keys[pygame.K_RIGHT]:
            self.rect.x += 300 * dt