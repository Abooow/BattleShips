
import pygame
import config
import pic_module

from framework.cell import Cell


class Board:
    def __init__(self):
        self.list = [[Cell()] * 10 for i in range(10)]
        self.shots_fired = []
        self.ships = []


    def place_ship(self, ship):
        ''' 

        param ship (Ship): the ship to place
        returns: nothing
        rtype: None '''

        rotation = {
            (1, 0) : 270,
            (-1, 0) : 90,
            (0, 1) : 180,
            (0, -1) : 0}
        # enitre boat
        for i in range(ship.length):
            x = ship.position[0] + i * ship.rotation[0]
            y = ship.position[1] + i * ship.rotation[1]
            self.list[y][x] = Cell(pic_module.boat_middle, rotation[ship.rotation], ship)

        # front
        x = ship.position[0] + (ship.length - 1) * ship.rotation[0]
        y = ship.position[1] + (ship.length - 1) * ship.rotation[1]
        self.list[y][x] = Cell(pic_module.boat_top, rotation[ship.rotation], ship)

        # back
        x = ship.position[0]
        y = ship.position[1]
        self.list[y][x] = Cell(pic_module.boat_bottom, rotation[ship.rotation], ship)

        self.ships.append(ship)


    def shoot(self, shot_koord):
        '''
        param shot_koord (tuple[int,int]): (x, y)
        return True or False
        rtype: tuple[bool,Ship] '''
        
        #shots_fired checks if coordinate´s been used
        if shot_koord in self.shots_fired:   
            return False, None 
        else:
            koordinat =  self.list[shot_koord[1]][shot_koord[0]]
            self.shots_fired.append(shot_koord)
            # successful shot but missed a boat
            if koordinat[2] == None:
                self.list[shot_koord[1]][shot_koord[0]] = ('*', color.LIGHTCYAN,  koordinat[2])
                return True, None
            # successful shot and hit a boat
            else:
                koordinat[2].get_hit()
                self.list[shot_koord[1]][shot_koord[0]] = (koordinat[0], color.RED,  koordinat[2])
                if koordinat[2].health <= 0:
                    self.ships.remove(koordinat[2])
                return True, koordinat[2]


    def draw(self, position):
        ''' Draws the board with the ships
        '''
        size = (50, 50)
        for y in range(len(self.list)):
            for x in range(len(self.list[y])):
                self.list[y][x].draw((x * size[0] + position[0], y * size[1] + position[1]))

    def draw_enemy(self):
        ''' Draws the board with the ships
        '''

        size = (50, 50)
        for y in range(len(self.list)):
            for x in range(len(self.list[y])):
                self.list[y][x].draw_enemy((x * size[0], y * size[1]))


    def can_place_ship(self, ship):
        '''

        param ship(tuple([int,int]), int, tuple([int,int])):
        return True or False'''
        
        if (ship.position[0] < 0 or ship.position[0] > len(self.list) - 1 or 
            ship.position[1] < 0 or ship.position[1] > len(self.list) - 1 or
            ship.rotation[0]*ship.length+ship.position[0] > len(self.list) or 
            ship.rotation[0]*(ship.length - 1)+ship.position[0] < 0 or 
            ship.rotation[1]*ship.length+ship.position[1] > len(self.list) or 
            ship.rotation[1]*(ship.length - 1)+ship.position[1] < 0):
            return False
        for i in range(ship.length):
            x = ship.position[0] + i * ship.rotation[0]
            y = ship.position[1] + i * ship.rotation[1]
            if self.list[y][x].ship != None:
                return False
        return True