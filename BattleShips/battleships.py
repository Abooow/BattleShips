# TODO!: Skapa en ny mapp som heter framework och i den mappen ska ni skapa en __init__.py fil
#        (sammasak som screens mappen), då gör man ett/en package*, det är en samling med filer.
#        I den mappen ska det finnas en fil för varje klass som är finns i den här filen,
#        allså ta en klass härifrån och plasera den i framework mappen.
#        När alla klasser är borta härirån kan ni tabort den här filen
#        
#        
#        *https://www.pythoncentral.io/how-to-create-a-python-package/



import console_color as color
import random


class Ship:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

        
    def get_hit(self):
        
        self.health -= 1



    def __init__(self, position, length, rotation):
        '''

        param position(tuple[int,int]): 
        param length(int):
        param rotation(tuple[int,int]): '''

        self.position = position
        self.length = length
        self.rotation = rotation
        self.health = length


class Board:
    def __init__(self):
        self.list = [[(' ', color.WHITE, None)] * 10 for i in range(10)]
        self.shots_fired = []
        self.ships = []


    def place_ship(self, ship):
        ''' 

        param ship (Ship): the ship to place
        returns: nothing
        rtype: None '''

        for i in range(ship.length):
            x = ship.position[0] + i * ship.rotation[0]
            y = ship.position[1] + i * ship.rotation[1]
            self.list[y][x] = ('■', color.GREEN, ship)

        prow = {
            (1, 0) : '>',
            (-1, 0) : '<',
            (0, 1) : 'V',
            (0, -1) : '^'}
        x = ship.position[0] + (ship.length - 1) * ship.rotation[0]
        y = ship.position[1] + (ship.length - 1) * ship.rotation[1]
        self.list[y][x] = (prow[ship.rotation], color.GREEN, ship)

        self.ships.append(ship)


    def shoot(self, shot_koord):
        '''
        param shot_koord (tuple[int,int]): (x, y)
        return True or False
        rtype: tuple[bool,Ship] '''
        
        #shots_fired checks if coordinate´s been used
        if shot_koord in self.shots_fired:   
            return False, None 
        else:
            koordinat =  self.list[shot_koord[1]][shot_koord[0]]
            self.shots_fired.append(shot_koord)
            # successful shot but missed a boat
            if koordinat[2] == None:
                self.list[shot_koord[1]][shot_koord[0]] = ('*', color.LIGHTCYAN,  koordinat[2])
                return True, None
            # successful shot and hit a boat
            else:
                koordinat[2].get_hit()
                self.list[shot_koord[1]][shot_koord[0]] = (koordinat[0], color.RED,  koordinat[2])
                if koordinat[2].health <= 0:
                    self.ships.remove(koordinat[2])
                return True, koordinat[2]


    def draw(self):
        char = 'A'
        #alphabet = "ABCDEFGHIJ"
        print('  |', end='')
        for j in range(len(self.list[0])):
            color.print_color(char, color.BLUE, end='|')
            char = Board._increment_char(char)
        print()

        for y in range(len(self.list)):
            color.print_color(f'{y} ', color.BLUE, end='')
            for x in range(len(self.list[y])):
                color.print_color('|', color.WHITE, end='')
                color.print_color(self.list[y][x][0], self.list[y][x][1], end='')
      
            color.print_color('|', color.WHITE)


    def draw_anonymously(self):
        ''' Draws the board with the ships
        '''

        char = 'A'
        print('  |', end='')
        for j in range(len(self.list[0])):
            color.print_color(char, color.BLUE, end='|')
            char = Board._increment_char(char)
        print()

        # Board
        for y in range(len(self.list)):
            color.print_color(f'{y} ', color.BLUE, end='')
            for x in range(len(self.list[y])):
                cell = self.list[y][x]
                if cell[2] != None and (x, y) in self.shots_fired:
                    color.print_color('|', color.WHITE, end='')
                    color.print_color('■', cell[1], end='')
                elif (x, y) in self.shots_fired:
                    color.print_color('|', color.WHITE, end='')
                    color.print_color(cell[0], cell[1], end='')
                else:
                    color.print_color('|', color.WHITE, end='')
                    color.print_color(' ', cell[1], end='')
            color.print_color('|', color.WHITE)


    def can_place_ship(self, ship):
        '''

        param ship(tuple([int,int]), int, tuple([int,int])):
        return True or False'''
        
        if (ship.position[0] < 0 or ship.position[0] > len(self.list) or 
            ship.position[1] < 0 or ship.position[1] > len(self.list) or
            ship.rotation[0]*ship.length+ship.position[0] > len(self.list) or 
            ship.rotation[0]*(ship.length - 1)+ship.position[0] < 0 or 
            ship.rotation[1]*ship.length+ship.position[1] > len(self.list) or 
            ship.rotation[1]*(ship.length - 1)+ship.position[1] < 0):
            return False
        for i in range(ship.length):
            x = ship.position[0] + i * ship.rotation[0]
            y = ship.position[1] + i * ship.rotation[1]
            if self.list[y][x][2] != None:
                return False
        return True


    def _increment_char(char): #skicka in en karaktär
        char = ord(char)
        char += 1
        return chr(char)


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
