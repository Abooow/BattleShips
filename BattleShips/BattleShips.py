import os
import re

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


    def draw(self):
        for y in self.list:
            for x in y:
                Color.print_color(x[0], x[1], end='')
                Color.print_color('|', Color.LIGHTCYAN, end='')
            print()



def pang(cord):
    hihi = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9
}

    cord = re.match('(?P<letter>[A-J])(?P<num>[0-9)])$', str(attack).upper()) or re.match('(?P<num>[0-9])(?P<letter>[A-J)])$', str(attack).upper())
    if cord:
        y = int(hihi.get(cord.group('letter')))
        x = int(cord.group('num'))
    else:
        return False


player2 = Board()
player = Board()

player.place_ship(Ship((5, 2), 3, Ship.DOWN))
player.place_ship(Ship((0, 0), 4, Ship.RIGHT))
player.place_ship(Ship((9, 9), 6, Ship.UP))


player.draw()


