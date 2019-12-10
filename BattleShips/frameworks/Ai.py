class AI:
    def __init__(self):
        self.board = Board()

    def place_ship(self):
        ''' 

        param ship (Ship): the ship to place
        returns: nothing
        rtype: None '''
        
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


    def shoot(self, enemy):
        #param shot_koord (tuple[int,int]): (x, y)
        while True:
            xpos = random.randint(0,9)
            ypos = random.randint(0,9)
            shot = enemy.shoot((xpos, ypos))
            if shot[0]:
                return shot