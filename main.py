import pygame, sys, random
from grid import Grid
from robot import Robot
from target import Target
from game import Game

def draw():
    target.draw()
    robot.draw()
    main_game.draw_walls(50)


pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Warehouse Robot Simulation")

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)



main_game = Game()
game_grid = Grid()
robot = Robot()
target = Target()

# robot, target and walls all need to have different position
while target.position in main_game.walls:
    target.randomize()
while robot.position == target.position or robot.position in main_game.walls:
    robot.randomize()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_game.screen.fill((184,189,181))
    draw()


    pygame.display.update()
    clock.tick(60)



