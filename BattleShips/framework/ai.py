''' This module contains the AI class
'''

import random

from framework.board import Board


class AI:
    ''' A very basic AI that shoots at a random cell each time
    '''


    def __init__(self):
        self.board = Board()


    def place_ships(self) -> None:
        ''' Places all ships on randomly the board

        returns: NoReturn
        rtype: None
        '''
        
        all_ships_placed = False
        shipsAvailable = [2, 2, 2, 2, 3, 3, 3, 4, 4, 6]
        while all_ships_placed == False:
            xpos = random.randint(0,9)
            ypos = random.randint(0,9)
            postuple = (xpos, ypos)
            #(tuple([int,int]), int, tuple([int,int]))
            ship = Ship(postuple,shipsAvailable[0], [(1, 0), (-1, 0), (0, 1), (0, -1)][random.randint(0, 3)])
            if self.board.can_place_ship(ship):
                self.board.place_ship(ship)
                del shipsAvailable[0]
                if len(shipsAvailable) < 1:
                    all_ships_placed = True


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