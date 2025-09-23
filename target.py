import random

import pygame
from pygame.math import Vector2
from grid import Grid
from game import Game


class Target:
    def __init__(self):
        self.x = random.randint(0, Game.cell_number-1)
        self.y = random.randint(0, Game.cell_number-1)
        self.position = Vector2(self.x,self.y)

    def randomize(self):
        self.x = random.randint(0, Game.cell_number - 1)
        self.y = random.randint(0, Game.cell_number - 1)
        self.position = Vector2(self.x, self.y)

    def draw(self):
        target_rect = pygame.Rect(self.position.x * Game.cell_size, self.position.y * Game.cell_size, Game.cell_size, Game.cell_size)
        pygame.draw.rect(Game.screen, (220,20,60), target_rect)