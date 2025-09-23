import random

import pygame
from pygame.math import Vector2
from grid import Grid
from game import Game
from target import Target

target = Target()
class Robot:
    def __init__(self):
        self.x = random.randint(0, Game.cell_number - 1)
        self.y = random.randint(0, Game.cell_number - 1)
        self.position = Vector2(self.x, self.y)

    def randomize(self):
        self.x = random.randint(0, Game.cell_number - 1)
        self.y = random.randint(0, Game.cell_number - 1)
        self.position = Vector2(self.x, self.y)

    def draw(self):
        robot_rect = pygame.Rect(self.position.x * Game.cell_size, self.position.y * Game.cell_size, Game.cell_size,
                                  Game.cell_size)
        pygame.draw.rect(Game.screen, (30,144,255), robot_rect)