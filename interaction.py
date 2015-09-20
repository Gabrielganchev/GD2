

import pygame, sys
from tileC import Tile


def interaction(screen,survivor):

    Mpos = pygame.mouse.get_pos() # [x,y]  mouse position

    Mx = Mpos[0]/Tile.width
    My = Mpos[1]/Tile.height

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in Tile.List:
                if tile.x == (Mx *Tile.width) and tile.y == (My *Tile.width):
                    tile.type = 'solid'
                    tile.walkable = False
                    break



        if event.type== pygame.KEYDOWN:

            if event.key == pygame.K_w: # notrh
                future__tile_number = survivor.get_number() - Tile.V
                if Tile.get_tile(future__tile_number).walkable:
                    survivor.y -= survivor.height



            if event.key == pygame.K_s: # South
                future__tile_number = survivor.get_number() + Tile.V
                if Tile.get_tile(future__tile_number).walkable:
                    survivor.y += survivor.height



            if event.key == pygame.K_a: # WEST
                future__tile_number = survivor.get_number() - Tile.H
                if Tile.get_tile(future__tile_number).walkable:
                    survivor.x -= survivor.width




            if event.key == pygame.K_d: # East
                future__tile_number = survivor.get_number() + Tile.H
                if Tile.get_tile(future__tile_number).walkable:
                    survivor.x += survivor.width