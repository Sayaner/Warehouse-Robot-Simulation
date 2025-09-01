import pygame, sys
from grid import Grid

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Warehouse Robot Simulation")

clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

running = True
while running:
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 0, 60, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()