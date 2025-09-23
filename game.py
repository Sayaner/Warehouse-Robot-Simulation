import pygame
from grid import Grid


class Game:
    game_grid = Grid()
    cell_number = game_grid.cell_number
    cell_size = game_grid.cell_size
    screen = pygame.display.set_mode((game_grid.cell_number * game_grid.cell_size, game_grid.cell_number * game_grid.cell_size))

    def update(self):
        pass
