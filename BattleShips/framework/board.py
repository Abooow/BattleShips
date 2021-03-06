''' This module contains the Board class
'''

import pygame
import config
import sprites
import random

from framework.cell import Cell
from framework.ship import Ship


class Board:
    ''' Base class for a board

    A Board is the playfield where all the ships are placed


    example of a placed ship:
        image_set = [U, #, ^]

        ^  <- prow  | image_index = 2 | ship_part = 3
        #  <- deck  | image_index = 1 | ship_part = 2
        #  <- deck  | image_index = 1 | ship_part = 1
        U  <- stern | image_index = 0 | ship_part = 0
    '''

    def place_ships_randomly(board) -> None:
        ''' Places all ships on randomly the board

        :param board (Board): the board to place the ships on

        returns: NoReturn
        rtype: None
        '''
        
        ships_available = config.ship_types[:]
        while len(ships_available) > 0:
            xpos = random.randint(0,9)
            ypos = random.randint(0,9)
            pos_tuple = (xpos, ypos)

            # create a ship
            ship = Ship(sprites.set_ship_textures_sketch[ships_available[0][0]], 
                        pos_tuple, 
                        ships_available[0][1], 
                        random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)]))

            if board.place_ship(ship):
                del ships_available[0]


    def __init__(self):
        # create a 2d array filled with cells
        self.list = [[0] * 10 for i in range(10)]
        for i in range(10):
            for j in range(10):
                self.list[i][j] = Cell()
        self.shots_fired = []
        self.ships = []


    def place_ship(self, ship) -> bool:
        ''' Places a ship on the board

        :param ship (Ship): the ship to place
        :returns: True if the placement was successful, otherwise False
        :rtype: bool
        '''

        if not self.can_place_ship(ship):
            # placement failed
            return False

        # convert the ships rotation (which is a tuple[int,int]) to degrees, so we can use it to rotate the image
        tuple_to_deg = {
            (1, 0) : 270, # right
            (-1, 0) : 90, # left
            (0, 1) : 180, # down
            (0, -1) : 0 } # up
        rotation = tuple_to_deg[ship.rotation]

        # divide the ship in different parts and place each part on a cell
        for i in range(ship.length):
            # the cell index
            x = ship.position[0] + i * ship.rotation[0]
            y = ship.position[1] + i * ship.rotation[1]
            # the image index for each part (0=stern, 1=deck, 2=prow)
            image_index = 0 if i == 0 else 2 if i == ship.length-1 else 1

            self.list[y][x] = Cell(ship=ship, image_index=image_index, ship_part=i, rotation=rotation)

        # save the ship in self.ships list
        self.ships.append(ship)
        
        # placement was successful
        return True


    def can_shoot_at(self, coordinate) -> tuple:
        ''' Shoot at this board at the given coordinate
        
        :param coordinate (tuple[int,int]): the coordinate to shoot at (x, y)

        :return: first value: (True if a shot was successfully fired otherwise False) second value: (the ship that was hit, if any was hit, otherwise None)
        :rtype: tuple[bool,Ship]

        '''

        if (coordinate[0] < 0 or coordinate[0] > 9 or coordinate[1] < 0 or coordinate[1] > 9): 
            return False

        return False if self.list[coordinate[1]][coordinate[0]].hit else True


    def shoot_at(self, coordinate) -> tuple:
        ''' Shoot at this board at the given coordinate
        
        :param coordinate (tuple[int,int]): the coordinate to shoot at (x, y)

        :return: first value: (True if a shot was successfully fired otherwise False) second value: (the ship that was hit, if any was hit, otherwise None)
        :rtype: tuple[bool,Ship]
        '''
        
        # checks if the coordinate have been used
        if coordinate in self.shots_fired or not self.can_shoot_at(coordinate):   
            return False, None 
        else:
            # coordinate have not been used, add it to shots_fired list
            self.shots_fired.append(coordinate)
            
            # get the cell at this coordinate
            cell = self.list[coordinate[1]][coordinate[0]]

            # successful shot but missed a ship
            # cell.shoot_at() returns True if a ship was hit
            if cell.shoot_at():
                return True, cell.ship
            # successful shot but missed a ship
            else:
                return True, None


    def update(self, delta_time) -> None:
        ''' Updates all cells

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        for row in self.list:
            for col in row:
                col.update(delta_time)


    def draw(self, position) -> None:
        ''' Draws every cell on that are on this board

        :param position (tuple[int,int]): where to draw the board (x, y)

        :returns: NoReturn
        :rtype: None
        '''

        for y in range(len(self.list)):
            for x in range(len(self.list[y])):
                self.list[y][x].draw((x * config.CELL_SIZE + position[0], y * config.CELL_SIZE + position[1]))


    def draw_enemy(self, position) -> None:
        ''' Draws every cell on that are on this board but doesn't show the placed ships, only hits and misses

        :param position (tuple[int,int]): where to draw the board (x, y)

        :returns: NoReturn
        :rtype: None
        '''

        for y in range(len(self.list)):
            for x in range(len(self.list[y])):
                self.list[y][x].draw_enemy((x * config.CELL_SIZE + position[0], y * config.CELL_SIZE + position[1]))


    def can_place_ship(self, ship) -> bool:
        ''' Check if the ship can be placed on this board

        :param ship(Ship): the ship to check if it's placeable

        :return: True if the ship can be placed, otherwise False
        :rtype: bool
        '''
        
        # checks if the ship is outside the boundaries
        if (ship.position[0] < 0 or ship.position[0] > len(self.list) - 1 or 
            ship.position[1] < 0 or ship.position[1] > len(self.list) - 1 or
            ship.rotation[0] * ship.length+ship.position[0] > len(self.list) or 
            ship.rotation[0] * (ship.length - 1)+ship.position[0] < 0 or 
            ship.rotation[1] * ship.length+ship.position[1] > len(self.list) or 
            ship.rotation[1] * (ship.length - 1)+ship.position[1] < 0):
            return False

        # checks if the ship is overlapping any other ship on the board
        for i in range(ship.length):
            x = ship.position[0] + i * ship.rotation[0]
            y = ship.position[1] + i * ship.rotation[1]
            if self.list[y][x].ship != None:
                return False

        return True