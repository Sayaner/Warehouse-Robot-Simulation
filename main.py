import pygame, sys, random
from grid import Grid
from robot import Robot
from target import Target
from game import Game

def draw():
    target.draw()
    robot.draw()


pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Warehouse Robot Simulation")

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)



main_game = Game()
game_grid = Grid()
target = Target()
robot = Robot()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_game.screen.fill((184,189,181))
    draw()


    pygame.display.update()
    clock.tick(60)



