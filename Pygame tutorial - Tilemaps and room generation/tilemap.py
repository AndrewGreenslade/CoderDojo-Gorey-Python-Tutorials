import pygame as pg

FLOOR = 0
WALL = 1

class room:

    
    def __init__(self, position):
        
        self.tileMap =[
            [WALL,  WALL,   WALL,   WALL,   WALL,   WALL,   WALL,   WALL,   WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  FLOOR,  WALL],
            [WALL,  WALL,   WALL,   WALL,   FLOOR,   WALL,   WALL,   WALL,   WALL],
        ]

        self.textures = {
                            FLOOR   :   pg.image.load("images/floor.png"),
                            WALL    :   pg.image.load("images/wall.png")
                        }

        self.mapWidth = len(self.tileMap)     
        self.mapHeight = len(self.tileMap[0]) 
        self.tileSize = 16
        self.pos = position


    def drawRoom(self, window):
        for row in range(self.mapWidth):
            for column in range(self.mapHeight):
                window.blit(self.textures[self.tileMap[row][column]], (self.pos.x + (column * self.tileSize), self.pos.y + (row * self.tileSize)))