''' This module contains the Ship class
'''

class Ship:
    ''' Base class for a ship

    A Ship have a image set (texture), a coordinate where the ship starts, a lenth and a rotation
    ment to be used together with the Board class


    example:
        ship_texure1 = [U, #, ^]  <- the order is important, it have to be (bottom-part, middle-part, top-part) (stern, deck, prow)

        ship1 = Ship(image_set=ship_texure1, position=(1, 5), length=4, rotation=(0, -1))


    NOTE!: this example does not use a list of images, PLEASE use a list of images instead

    the example will create something like this:
        (board)
        ---------------------
        | | | | | | | | | | |
        | | | | | | | | | | |
        | |^| | | | | | | | |
        | |#| | | | | | | | |
        | |#| | | | | | | | |
        | |U| | | | | | | | |
        | | | | | | | | | | |
        | | | | | | | | | | |
        ---------------------

    In order to use your ship you need a Board to place the ship on, like this:
        player_board = Board()

        player_board.place_ship(ship1)

    for more info, look at the Board class


    example of a placed ship:
        image_set = [U, #, ^]

        ^  <- prow  | image_index = 2 | ship_part = 3
        #  <- deck  | image_index = 1 | ship_part = 2
        #  <- deck  | image_index = 1 | ship_part = 1
        U  <- stern | image_index = 0 | ship_part = 0
    '''


    # The different rotations for the ship, other values are allowed but not recommended
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


    def __init__(self, image_set, position, length, rotation):
        '''
        :param image_set (list[surface]): what texture this ship uses (bottom-part, middle-part, top-part) (stern, deck, prow)
        :param position (tuple[int,int]): (x, y) index where the ship starts
        :param length (int): the lenght of the ship
        :param rotation (tuple[int,int]): the rotation of the ship
        '''

        self.image_set = image_set
        self.position = position
        self.length = length
        self.rotation = rotation

        # health of the ship (same as length)
        self.health = length
        # all parts of the ship that are hit/destroyed
        self.hit_parts = [False] * length


    def get_hit(self, part) -> bool:
        ''' Takes a hit and loses 1 health

        :param part (int): what part of the ship to shoot at

        :returns: True if the ship have sunken (0 health), otherwise False
        :rtype: bool
        '''

        self.health -= 1
        self.parts[part] = True
        return True if self.health <= 0 else False