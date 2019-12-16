''' This module contains the AI class
'''

import random
import sprites

from framework.board import Board
from framework.ship import Ship



class AI:
    ''' A very basic AI that shoots at a random cell each time
    '''


    def __init__(self):
        self.board = Board()
        Board.place_ships_randomely(self.board)

            
    def random_shot(self, enemy) -> None:
        ''' Shoot at a random coordinate

        :param enemy (Board): the enemy board to shoot on

        :returns: NoReturn
        :rtype: None
        '''

        while True:
            # get random coordinate
            xpos = random.randint(0,9)
            ypos = random.randint(0,9)

            # shoot at that coordinate
            shot = enemy.shoot_at((xpos, ypos))

            # if shot was successful, then return, otherwise try again
            if shot[0]:
                return