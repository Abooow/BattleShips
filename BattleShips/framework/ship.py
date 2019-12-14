class Ship:
    ''' Base class for a ship

    example:
        ship_texure1 = [^, #, U]  <- it have to be (top_part, middle_part, bottom_part) (prow, deck, stern)

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
    '''


    # The different rotations for the ship, other values are allowed but not recommended
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


    def __init__(self, image_set, position, length, rotation):
        '''
        :param image_set (list[surface]): what texture this ship uses (top-part, middle-part, bottom-part) (prow, deck, stern)
        :param position (tuple[int,int]): (x, y) index where the ship starts
        :param length (int): the lenght of the ship
        :param rotation (tuple[int,int]): the rotation of the ship
        '''

        self.image_set = image_set
        self.position = position
        self.length = length
        self.rotation = rotation
        self.health = length

        self.parts = [True] * length


    def get_hit(self, part) -> bool:
        ''' Takes a hit and loses 1 health

        :param part (int): what part of the ship to shoot at

        :returns: True if the ship have sunken(0 health) otherwise False
        :rtype: bool
        '''

        self.health -= 1
        return True if self.health <= 0 else False