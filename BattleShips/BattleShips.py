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


# För att skriva ut färgad text
print(Color.YELLOW + "Hej i gult")
# eller
print(f"{Color.GREEN}Hej i grönt")
print("Den här texten är också grön")

# För att reseta färgen, använd Color.RESET
print(Color.RESET)

print("Texten är normal igen")










class Ship:
    def __init__(self, position, lenth, direction):
        self.position = position
        self.lenth = lenth
        self.direction = direction


class Board:
    def __init__(self, size, ships):
        self.list = [[' '] * size[0] for i in range(size[1])] 
        self.ships = ships
        

    def create_num(self):
        for y in range(len(self.list)):
            for x in range(len(self.list[y])):
                if x == 0 or x == len(self.list[y]) - 1 or y == 0 or y == len(self.list) - 1:
                    self.list[y][x] = char


    def create_border(self, char='\u2588'):
        for y in range(len(self.list)):
            for x in range(len(self.list[y])):
                if x == 0 or x == len(self.list[y]) - 1 or y == 0 or y == len(self.list) - 1:
                    self.list[y][x] = char


    def draw(self):
        for ship in self.ships:
            for i in range(ship.lenth):
                x = ship.position[0] + ship.direction[0] * i + 1
                y = ship.position[1] + ship.direction[1] * i + 1
                self.list[y][x] = '\u0FD5'


        for y in range(len(self.list)):
            for x in range(len(self.list[y])):
                print(self.list[y][x], end='')
            print()


def set_color(color):
    print(color, end='')

def reset_color():
    print(Color.RESET, end='')


def draw_boards_side_by_side(b1, b2, margin=(0, 0, 1)):
    for i in range(margin[0]):
        print()

    for y in range(max(len(b1.list), len(b2.list))):
        print(' ' * margin[1], end='')
        print(''.join(b1.list[y]), end='')
        print(' ' * margin[2], end='')
        print(''.join(b2.list[y]))



b1 = Board(size=(11, 11), ships=[Ship((0, 0), 4, (1, 0)), Ship((9, 9), 8, (-1, 0)), Ship((5, 2), 2, (0, -1))])
b1.create_border()
b2 = Board(size=(11, 11), ships=[Ship((2, 2), 3, (0, -1))])
b2.create_border()

set_color(Color.LIGHTCYAN)
b1.draw()
reset_color()
print()
b2.draw()