import pygame, sys
from tileC import Tile

def interaction(screen, survivor):

    Mpos = pygame.mouse.get_pos() # [x, y]
    Mx = Mpos[0] / Tile.width
    My = Mpos[1] / Tile.height

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in Tile.List:
                if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width):
                    tile.type = 'solid'
                    tile.walkable = False
                    break

    keys = pygame.key.get_pressed()



    if keys[pygame.K_w]: # North
        future_tile_number = survivor.get_number() - Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                # survivor.y -= survivor.height

    if keys[pygame.K_s]: # South
        future_tile_number = survivor.get_number() + Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                # survivor.y += survivor.height

    if keys[pygame.K_a]: # West
        future_tile_number = survivor.get_number() - Tile.H

        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                # survivor.x -= survivor.width

    if keys[pygame.K_d]: # East
        future_tile_number = survivor.get_number() + Tile.H
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                # survivor.x += survivor.width

