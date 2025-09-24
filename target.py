import random

import pygame
from pygame.math import Vector2


class Target:
    """A target that is to be found by the robot"""
    def __init__(self, grid, screen):
        self.grid = grid
        self.screen = screen
        self.position = Vector2()
        self.randomize()

    def randomize(self):
        self.position = Vector2(
            random.randint(0, self.grid.cell_number - 1),
            random.randint(0, self.grid.cell_number - 1)
        )

    def draw(self):
        target_rect = pygame.Rect(
            self.position.x * self.grid.cell_size,
            self.position.y * self.grid.cell_size,
            self.grid.cell_size, self.grid.cell_size)
        pygame.draw.rect(self.screen, (220,20,60), target_rect)