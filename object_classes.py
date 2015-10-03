import pygame
from tileC import Tile
from random import randint

class Character(pygame.Rect):

    width, height = 32, 32

    def __init__(self, x, y):

        self.tx, self.ty = None, None
        pygame.Rect.__init__(self, x, y, Character.width, Character.height)

    def __str__(self):
        return str(self.get_number())

    def set_target(self, next_tile):
        if self.tx == None and self.ty == None:
            self.tx = next_tile.x
            self.ty = next_tile.y

    def get_number(self):

        return ((self.x / self.width) + Tile.H) + ((self.y / self.height) * Tile.V)

    def get_tile(self):

        return Tile.get_tile(self.get_number())

class Zombie(Character):

    List = []
    spawn_tiles = (9,42,91,134,193,219,274)

    def __init__(self, x, y):

        Character.__init__(self, x, y)
        Zombie.List.append(self)

    @staticmethod
    def draw_zombies(screen):
        for zombie in Zombie.List:
            pygame.draw.rect(screen, [210, 24, 77], zombie)

    @staticmethod
    def movement():
        for zombie in Zombie.List:
            if zombie.tx != None and zombie.ty != None: # Target is set

                X = zombie.x - zombie.tx
                Y = zombie.y - zombie.ty

                vel = 4

                if X < 0: # --->
                    zombie.x += vel
                elif X > 0: # <----
                    zombie.x -= vel

                if Y > 0: # up
                    zombie.y -= vel
                elif Y < 0: # dopwn
                    zombie.y += vel

                if X == 0 and Y == 0:
                    zombie.tx, zombie.ty = None, None

    @staticmethod
    def spawn(total_frames, FPS):
        if total_frames % (FPS * 3) == 0:
            r = randint(0, len(Zombie.spawn_tiles) - 1)
            tile_num = Zombie.spawn_tiles[r]
            spawn_node = Tile.get_tile(tile_num)
            Zombie(spawn_node.x, spawn_node.y)


class Survivor(Character):
    original_img = None

    def __init__(self, x, y,img_path):
        self.direction = 'w'

        self.img = pygame.image.load(img_path)
        Survivor.original_img = self.img

        Character.__init__(self, x, y)

    def movement(self):

        if self.tx != None and self.ty != None: # Target is set

            X = self.x - self.tx
            Y = self.y - self.ty

            vel = 8

            if X < 0: # --->
                self.x += vel
            elif X > 0: # <----
                self.x -= vel

            if Y > 0: # up
                self.y -= vel
            elif Y < 0: # dopwn
                self.y += vel

            if X == 0 and Y == 0:
                self.tx, self.ty = None, None


    def rotate(self, direction):
        if direction == 'n':
            pass.direction = 'n'

        if direction == 's':
            pass.direction = 's'

        if direction == 'e':
            pass.direction = 'e'
            self.img = pygame.transform.flip(Survivor)
        if direction == 'w':
            pass.direction = 'w'
            self.img = Survivor.original_img


    def draw(self, screen):
        screen.blit(self.img,(self.x, self.y))

