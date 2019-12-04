import os


os.system('color')  
class Color:
    RESET = '\u001b[0m'
    BLACK = '\u001b[30m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'
    LIGHTBLACK = '\u001b[30;1m'
    LIGHTRED = '\u001b[31;1m'
    LIGHTGREEN = '\u001b[32;1m'
    LIGHTYELLOW = '\u001b[33;1m'
    LIGHTBLUE = '\u001b[34;1m'
    LIGHTMAGENTA = '\u001b[35;1m'
    LIGHTCYAN = '\u001b[36;1m'
    LIGHTWHITE = '\u001b[37;1m'

    def print_color(string, color, end='\n'):
        print(f'{color}{string}{Color.RESET}', end=end)


class Ship:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


    def __init__(self, position, length, rotation):
        '''

        param position(tuple[int,int]): 
        param length(int):
        param rotation(tuple[int,int]): '''

        self.position = position
        self.length = length
        self.rotation = rotation


class Board:
    def __init__(self):
        self.list = [[(' ', Color.WHITE)] * 10 for i in range(10)]


    def place_ship(self, ship):
        for i in range(ship.length):
            x = ship.position[0] + i * ship.rotation[0]
            y = ship.position[1] + i * ship.rotation[1]
            self.list[y][x] = ('O', Color.GREEN)
    
    def can_place_ship(self, ship):
        '''

        param ship(tuple([int,int]), int, tuple([int,int])):
        return True or False'''
        
        if (ship.position[0] < 0 or ship.position[0] > len(self.list) or 
            ship.position[1] < 0 or ship.position[1] > len(self.list) or
            ship.rotation[0]*ship.length+ship.position[0] > len(self.list) or 
            ship.rotation[0]*ship.length+ship.position[0] < 0 or 
            ship.rotation[1]*ship.length+ship.position[1] > len(self.list) or 
            ship.rotation[1]*ship.length+ship.position[1] < 0):
            return False
        for i in range(ship.length):
            x = ship.position[0] + i * ship.rotation[0]
            y = ship.position[1] + i * ship.rotation[1]
            if self.list[y][x][2] != None:
                return False
        return True


    def draw(self):
        for y in self.list:
            for x in y:
                Color.print_color(x[0], x[1], end='')
                Color.print_color('|', Color.LIGHTCYAN, end='')
            print()


player2 = Board()
player = Board()

#placing ships state
all_ships_placed = False
shipsAvailable = [2, 2, 2, 2, 3, 3, 3, 4, 4, 6]
#placing ships state
while not all_ships_placed:
    
    for ship in range(len(shipsAvailable)):
        os.system('cls')
        print('Place your ships onto the battlefield.')
        player.draw()
        counter = 0
        for i in shipsAvailable:
            
            counter += 1
            print(counter,".",i*"O")
        print(f'Placing a ship with length {shipsAvailable[0]}.')
        shipLength = shipsAvailable[0]
        shipFirstPos = input('Set start coordinate(x,y(0-9)): ')
        #place function that converts user input to coordinate tuple here, pang()
        while True:
            shipDirection = input('Set direction(LEFT, RIGHT, UP, DOWN)')
            if shipDirection.upper() == 'LEFT': 
                dir = Ship.LEFT 
                break
            elif shipDirection.upper() == 'RIGHT': 
                dir = Ship.RIGHT 
                break
            elif shipDirection.upper() == 'UP': 
                dir = Ship.UP
                break
            elif shipDirection.upper() == 'DOWN': 
                dir = Ship.DOWN
                break
            else: continue
        x = int(shipFirstPos[0])
        y = int(shipFirstPos[1])
        
        #Check if its ok to place the boat
        if player.can_place_ship(Ship((x, y), shipLength, dir)) == True:
            player.place_ship(Ship((x, y), shipLength, dir))
            del shipsAvailable[0]
        




