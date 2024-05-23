import random

import pygame
from pygame import Vector2


class Fruit:
    apple = pygame.image.load('Photos/apple.png').convert_alpha()
    
    def __init__(self,cell_number,cell_size):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.x = random.randint(0, cell_number - 1)
        self.y = 4
        self.pos = Vector2(self.x, self.y)

    def draw(self, screen):
        fruit = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_size)
        screen.blip(self.apple, fruit)
    