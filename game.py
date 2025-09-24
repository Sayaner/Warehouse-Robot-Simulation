import pygame, random, sys
from pygame.math import Vector2


class Game:
    """This object contains all the game logic"""
    def __init__(self, grid, robot, target, screen, number_of_walls):
        self.grid = grid
        self.robot = robot
        self.target = target
        self.screen = screen
        self.walls = self.generate_walls(number_of_walls)
        self.clock = pygame.time.Clock()
        self.check_positions(self.target, self.robot)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((184, 189, 181))
            self.draw()

            pygame.display.update()
            self.clock.tick(60)

    def generate_walls(self, walls_quantity):
        walls = []
        for _ in range(walls_quantity):
            pos_x = random.randint(0, self.grid.cell_number - 1)
            pos_y = random.randint(0, self.grid.cell_number - 1)
            walls.append(Vector2(pos_x, pos_y))
        return walls

    def draw(self):
        self.target.draw()
        self.robot.draw()
        self.draw_walls()

    def draw_walls(self):
        for wall in self.walls:
            wall_rect = pygame.Rect(
                wall.x*self.grid.cell_size,
                wall.y*self.grid.cell_size,
                self.grid.cell_size, self.grid.cell_size
            )
            pygame.draw.rect(self.screen, pygame.Color('black'), wall_rect)

    def check_positions(self, target, robot):
        while target.position in self.walls:
            target.randomize()
        while robot.position == target.position or robot.position in self.walls:
            robot.randomize()