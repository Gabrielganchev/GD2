import pygame
from tileC import Tile
from random  import randint

class Character(pygame.Rect):
    width, height = 32,32

    def __init__(self,x,y):

        pygame.Rect.__init__(self,x,y,Character.width, Character.height)


    def __str__(self):
        return str(self.get_number())
    def get_number(self):
        return ((self.x/ self.width) +Tile.H )+ ((self.y/ self.height) *Tile.V)

    def get_tile(self):
        return Tile.get_tile(self.get_number())



class Zombie(Character):
    List = []
    spawn_tiles=(9,42,134,193,219,274)
    def __init__(self,x,y):

        self.tx, self.ty = None, None
        Character.__init__(self,x,y)
        Zombie.List.append(self)


    @staticmethod
    def draw_zombies(screen):
        for zombie in Zombie.List:
            pygame.draw.rect(screen,[210,24,77],zombie)



    def set_target(self, next_tile):
        if self.tx == None and self.ty == None:
            self.tx = next_tile.x
            self.ty = next_tile.y

    @staticmethod
    def movement():
        for zombie in Zombie.List:
            if zombie.tx != None and zombie.ty != None:
                X = zimbie.x - zombie.tx
                Y = zombie.y - zombie.ty

                if X < 0: # --->
                    zombie.x += vel
                elif x >0:# <====
                    zombie.x -= vel


                if Y < 0: # up
                    zombie.y += vel
                elif Y >0: # down
                    zombie.y -= vel
                if X == 0 and Y == 0:
                    zombie.tx, zombie.ty = None , None


    @staticmethod
    def spawn(total_frames, FPS):
        if total_frames % FPS ==0:
            r = randint(0,len(Zombie.spawn_tiles)-1)
            tile_num = Zombie.spawn_tiles[r]
            spawn_node = Tile.get_tile(tile_num)
            Zombie(spawn_node.x,spawn_node.y)
class Survivor(Character):
    def __init__(self,x,y):
        Character.__init__(self,x,y)
    def draw(self,screen):
        r = self.width / 2
        pygame.draw.circle(screen, [77,234,156], (self.x + r,self.y +r) , r)