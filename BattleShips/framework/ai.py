''' This module contains the AI class
'''

import random
import sprites

from framework.board import Board
from framework.ship import Ship



class AI:
    ''' A very basic AI that shoots at a random cell each time
    '''
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


    def __init__(self):
        self.found_ship = False
        self.last_hit_success = False
        self.directions = AI.directions[:]
        self.shots = []

        self.board = Board()
        Board.place_ships_randomly(self.board)

            
    def shoot(self, enemy) -> None:
        ''' Shoot at a random coordinate

        :param enemy (Board): the enemy board to shoot on

        :returns: NoReturn
        :rtype: None
        '''

        # if a ship is found
        if self.found_ship:
            self._smart_shoot() # think before shooting
        else:
            # when a ship is not found, shoot random
            while True:
                # get random coordinate
                x = random.randint(0, 9)
                y = random.randint(0, 9)

                # shoot at that coordinate
                shot = enemy.shoot_at((x, y))

                # if shot was successful, then return, otherwise try again
                if shot[0]:
                    self.shots.append((x, y))
                    if shot[1] if not None:
                        self._on_hit_ship(shot[1])
                    return


    def _smart_shoot(self):
        pass


    def _on_hit_ship(self, hit_ship):
        self.found_ship = True