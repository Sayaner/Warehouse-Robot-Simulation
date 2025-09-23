import pygame, random
from grid import Grid
from pygame.math import Vector2


class Game:
    game_grid = Grid()
    cell_number = game_grid.cell_number
    cell_size = game_grid.cell_size
    screen = pygame.display.set_mode((game_grid.cell_number * game_grid.cell_size, game_grid.cell_number * game_grid.cell_size))
    number_of_walls = 200
    walls = []

    for i in range(number_of_walls-1):
        pos_x = random.randint(0, cell_number - 1)
        pos_y = random.randint(0, cell_number - 1)
        wall_position = Vector2(pos_x, pos_y)
        walls.append(wall_position)


    def update(self):
        pass

    def draw_walls(self, number_of_walls):
        for i in range(len(self.walls)-1):
            wall_rect = pygame.Rect(self.walls[i].x*self.cell_size, self.walls[i].y*self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, pygame.Color('black'), wall_rect)