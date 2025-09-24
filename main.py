import pygame, sys, random
from grid import Grid
from robot import Robot
from target import Target
from game import Game


pygame.init()
pygame.display.set_caption("Warehouse Robot Simulation")

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

grid = Grid()
screen = pygame.display.set_mode(
            (grid.cell_number * grid.cell_size,
             grid.cell_number * grid.cell_size)
        )

game = Game(grid, Robot(grid, screen), Target(grid, screen), screen, 200)
game.run()






