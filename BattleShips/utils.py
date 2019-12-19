import random
import sprites
import config


from framework.ship import Ship


def place_ships_randomly(board) -> None:
        ''' Places all shipsthe the board randomly

        :param board (Board): the board to place the ships on

        returns: NoReturn
        rtype: None
        '''
        
        ships_available = config.ship_types[:]
        normal_sets = []
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
                normal_sets.append(sprites.set_ship_textures[ships_available[0][0]])
                del ships_available[0]

        return normal_sets


def draw_font(text, color, position):
    new_text = config.font.render(text, True , color)
    config.window.blit(new_text, position)
