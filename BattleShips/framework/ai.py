''' This module contains the AI class
'''

import random
import sprites

from framework.board import Board
from framework.ship import Ship



class AI():
    ''' Base class for all AI's
    '''


    def __init__(self):
        self.board = Board()
        Board.place_ships_randomly(self.board)

            
    def get_shoot_coordinate(self):
        pass


    def shoot(self, enemy, coordinate) -> None:
        ''' Shoot at a random coordinate

        :param enemy (Board): the enemy board to shoot on

        :returns: NoReturn
        :rtype: None
        '''
        pass



class DumbAI(AI):
    ''' A very basic AI that shoots at a random cell each time
    '''

    def __init__(self):
        super().__init__()


    def shoot(self, enemy):
        super().shoot(enemy)

        while True:
                # get random coordinate
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                coordinate = (x, y)

                # shoot at that coordinate
                shot = enemy.shoot_at(coordinate)

                # if shot was successful, then return, otherwise try again
                if shot[0]:
                    return



class SmartAI(AI):
    _available_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self):
        super().__init__()

        self._found_ship = False
        self._first_hit_cord = None
        self._shoot_direction = None
        self._latest_hit = None
        self._available_directions = []


    def shoot(self, enemy, coordinate):
        super().shoot(enemy, coordinate)

        enemy.shoot_at(coordinate)


    def get_shoot_coordinate(self, enemy):
        super().get_shoot_coordinate()

        # if a ship is found
        if self._found_ship:
            return self._get_smart_coordinate(enemy) # think before shooting
        else:
            # when a ship is not found, shoot random
            return self._get_random_coordinate(enemy)


    def _get_random_coordinate(self, enemy, errorlevel=0) -> tuple:
        ''' Get a almost random coordinate

        :param enemy (Board): the enemy board
        :param errorlevel (int): the number of attempt to shoot at enemy board

        :returns: a coordinate
        :rtype: tuple[int,int]
        '''

        while True:
            # get random coordinate
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            coordinate = (x, y)

            if (not enemy.list[y][x].hit and 
                len(self._get_empy_cells_around(coordinate, enemy)) <= 2 and 
                errorlevel < 40):
                self._get_random_coordinate(enemy, errorlevel + 1)
                break

            # if shot was successful, then return, otherwise try again
            if enemy.can_shoot_at(coordinate):
                cell = enemy.list[coordinate[1]][coordinate[0]]
                if cell.ship is not None:
                    self._latest_hit = coordinate
                    self._first_hit_cord = coordinate
                    self._on_hit_ship(enemy)
                return coordinate
        return coordinate


    def _get_empy_cells_around(self, coordinate, enemy):
        available_directions = SmartAI._available_directions[:]

        # look around the hit cord in all directions
        for cord in available_directions:
            # check if cell is hit, then remove cord from available_directions
            new_cord = (coordinate[0] + cord[0], coordinate[1] + cord[1])
            if (new_cord[0] < 0 or new_cord[0] > 9 or 
                new_cord[1] < 0 or new_cord[1] > 9): 
                available_directions.remove(cord)
                continue
            if enemy.list[new_cord[1]][new_cord[0]].hit:
                available_directions.remove(cord)

        return available_directions


    def _get_smart_coordinate(self, enemy):
        if self._shoot_direction is None or (self._shoot_direction not in self._available_directions and 
                                             self._shoot_direction is not None):
            if len(self._available_directions) == 0:
                self._found_ship = False
                return self._get_random_coordinate(enemy)

            # get random coordinate from available_directions
            self._shoot_direction = random.choice(self._available_directions)

        # shoot at that coordinate
        new_cord = (self._latest_hit[0] + self._shoot_direction[0],
                    self._latest_hit[1] + self._shoot_direction[1])

        # if shot was successful
        if enemy.can_shoot_at(new_cord):
            cell = enemy.list[new_cord[1]][new_cord[0]]
            if cell.ship is not None:
                if cell.ship.have_sunken: # if the ship have sunken find new cell
                    self._found_ship = False
                else:
                    self._latest_hit = new_cord
            else:
                self._available_directions.remove(self._shoot_direction)
                # reverse shoot direction
                self._shoot_direction = (self._shoot_direction[0] * -1, self._shoot_direction[1] * -1)
                self._latest_hit = self._first_hit_cord
        else:
            # can't shoot here, have to try again
            self._available_directions.remove(self._shoot_direction)
            self._shoot_direction = (self._shoot_direction[0] * -1, self._shoot_direction[1] * -1)
            self._get_smart_coordinate(enemy)

        return new_cord

    def _on_hit_ship(self, enemy):
        self._found_ship = True
        self._available_directions = self._get_empy_cells_around(self._first_hit_cord, enemy)



class CheatingAI(AI):
    def __init__(self):
        super().__init__()


    def shoot(self, enemy):
        super().shoot(enemy)


class HackerAI(AI):
    def __init__(self):
        super().__init__()


    def shoot(self, enemy):
        super().shoot(enemy)