
import pygame, sys, Funk
from tileC import Tile
from object_classes import *
from interaction import interaction
from A_Star import A_Star

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((704, 448)) # 32, 32

for y in range(0, screen.get_height(), 32):
    for x in range(0, screen.get_width(), 32):
        if Tile.total_tiles in Tile.invalids:
            Tile(x, y, 'solid')
        else:
            Tile(x, y, 'empty')

clock = pygame.time.Clock()
FPS = 20
total_frames = 0

# zombie1 = Zombie(80, 80)
survivor = Survivor(32 * 2, 32 * 4)


while True:

    screen.fill([0,0,0])
    A_Star(screen, survivor, total_frames, FPS)
    interaction(screen, survivor)
    Tile.draw_tiles(screen)
    survivor.draw(screen)
    Zombie.draw_zombies(screen)

    pygame.display.flip()
    clock.tick(FPS)
    total_frames += 1