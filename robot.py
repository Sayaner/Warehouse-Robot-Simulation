import random

import pygame
from pygame.math import Vector2


class Robot:
    """A robot that avoids the walls and uses pathfinding to locate the target"""
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
        robot_rect = pygame.Rect(
            self.position.x * self.grid.cell_size,
            self.position.y * self.grid.cell_size,
            self.grid.cell_size, self.grid.cell_size)
        pygame.draw.rect(self.screen, (30,144,255), robot_rect)