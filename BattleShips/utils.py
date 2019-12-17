import random
import sprites

from framework.ship import Ship


def place_ships_randomly(board) -> None:
        ''' Places all shipsthe the board randomly

        :param board (Board): the board to place the ships on

        returns: NoReturn
        rtype: None
        '''
        
        ships_available = [2, 2, 2, 3, 3, 4, 4, 5]
        while len(ships_available) > 0:
            xpos = random.randint(0,9)
            ypos = random.randint(0,9)
            pos_tuple = (xpos, ypos)

            # create a ship
            ship = Ship(sprites.set_ship_texture0, 
                        pos_tuple, 
                        ships_available[0], 
                        [(1, 0), (-1, 0), (0, 1), (0, -1)][random.randint(0, 3)])

            if board.place_ship(ship):
                del ships_available[0]