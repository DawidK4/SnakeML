import pygame as pg


class Tile:
    jungle = pg.image.load('Photos/jungle.png').convert_alpha()

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = Tile.jungle

    def draw(self, screen, cell_number, cell_size):
        for column in range(cell_number):
            for row in range(cell_number):
                tile = pg.Rect(x, y, cell_size, cell_size)
                screen.blit(self.image, tile)
