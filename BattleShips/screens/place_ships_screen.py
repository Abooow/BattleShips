''' This module contains the PlaceShipScreen which is the second screen to be shown

everything that have to do with PlaceShips state should be in in here
'''

import pygame
import random
import config
import sprites
import surface_change

from screens.screen import Screen
from framework.board import Board
from framework.ship import Ship


class PlaceShipScreen(Screen):
    ''' The screen for placing your ships


    This screen can change the current_screen to:
        BattleScreen - when the start button is pressed

    other functionalities:
        -
    '''


    # convert the ships rotation (which is a tuple[int,int]) to degrees, so we can use it to rotate the image
    tuple_to_deg = {
        (1, 0) : 270, # right
        (-1, 0) : 90, # left
        (0, 1) : 180, # down
        (0, -1) : 0 } # up


    def __init__(self):
        super().__init__()


    def load_content(self) -> None:
        ''' Initializes/load all content

        :returns: NoReturn
        :rtype: None
        '''

        super().load_content()

        self.board = Board()            # the board to place the ships on
        self.ship_rotation = (-1, 0)    # the rotaion of the ship
        self.ship_length = 5            # the lenth of the ship
        self.board_pos = (123, 120)     # where to draw the board

        self.rain_drops = []            # -> list(tuple[int,int,int]) (x, y, speed)
        self.rain_amount = 50           
        
        self._creat_rain()
        

    def update(self, delta_time) -> None:
        ''' Updates everything

        :returns: NoReturn
        :rtype: None
        '''

        events = super().update(delta_time)

        # place ship when mouse clicked
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._place_ship()

            # rotate ship
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ship_rotation = (-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.ship_rotation = (1, 0)
                if event.key == pygame.K_UP:
                    self.ship_rotation = (0, -1)
                if event.key == pygame.K_DOWN:
                    self.ship_rotation = (0, 1)
                if event.key == pygame.K_1:
                    self.ship_length -= 1
                if event.key == pygame.K_2:
                    self.ship_length += 1

        # update rain drops
        for i in range(self.rain_amount):
            if (self.rain_drops[i][1] > config.SCREEN_HEIGHT):
                x = random.randint(0,config.SCREEN_WIDTH)
                self.rain_drops[i] = (x, -100, self.rain_drops[i][2])
            self.rain_drops[i] = (self.rain_drops[i][0], self.rain_drops[i][1]  + self.rain_drops[i][2], self.rain_drops[i][2])



    def draw(self) -> None:
        ''' Draws everything to the screen

        :returns: NoReturn
        :rtype: None
        '''

        super().draw() 

        # draw rain
        for i in self.rain_drops:
            green = (i[2]*3, 100+i[2]*5, 200-i[2]*6)
            pygame.draw.rect(config.window, green, (i[0],i[1],10,20+i[2]*2))

        # draw background
        config.window.blit(sprites.img_explosion, (0, 0))

        # draw board
        self.board.draw(self.board_pos)
        #draw ship
        self._draw_ship()


    def _creat_rain(self) -> None:
        ''' Instantiates the rain

        :returns: NoReturn
        :rtype: None
        '''

        # x, y, speed
        for i in range(self.rain_amount):
            x = random.randint(0, config.SCREEN_WIDTH)
            y = random.randint(0, config.SCREEN_HEIGHT)
            speed = random.randint(8,30)
            self.rain_drops.append((x, y, speed))


    def _get_cell_index_at_mouse(self) -> tuple:
        ''' Get the cell index the mouse is hovering over

        :returns: the (x, y) index
        :rtype: tuple[int,int]
        '''

        mouse = pygame.mouse.get_pos()
        return ((mouse[0] - self.board_pos[0]) // config.CELL_SIZE,
                (mouse[1] - self.board_pos[1]) // config.CELL_SIZE)


    def _place_ship(self) -> None:
        ''' Place the current selected ship to the board

        :returns: NoReturn
        :rtype: None
        '''

        cell_index = self._get_cell_index_at_mouse()
        ship = Ship(sprites.set_ship_texture0, cell_index, self.ship_length, self.ship_rotation)
        self.board.place_ship(ship)

        
    def _can_place(self) -> bool:
        ''' Checks if the current selected ship can be placed on the board

        :returns: True if the ship can be placed, otherwise False
        :rtype: bool
        '''

        cell_index = self._get_cell_index_at_mouse()
        ship = Ship(sprites.set_ship_texture0, cell_index, self.ship_length, self.ship_rotation)
        return self.board.can_place_ship(ship)


    def _draw_ship(self) -> None:
        ''' Draws the current selected ship at the mouse position
        
        :returns: NoReturn
        :rtype: None
        '''

        # the color for the ship. if can_place then color is white otherwise it's red
        color = (255, 255, 255) if self._can_place() else (255, 50, 50)

        # draw top-part of the ship
        pic = pygame.transform.rotate(sprites.set_ship_texture0[2], PlaceShipScreen.tuple_to_deg[self.ship_rotation])
        x, y = pygame.mouse.get_pos()
        x += self.ship_rotation[0] * (self.ship_length - 1) * config.CELL_SIZE - config.CELL_SIZE * 0.5
        y += self.ship_rotation[1] * (self.ship_length - 1) * config.CELL_SIZE - config.CELL_SIZE * 0.5
        pic = surface_change.colorize(pic.copy(), color)
        config.window.blit(pic, (x,y))

        # draw mid-part of the ship
        pic = pygame.transform.rotate(sprites.set_ship_texture0[1], PlaceShipScreen.tuple_to_deg[self.ship_rotation])
        for i in range(1, self.ship_length - 1):
            x, y = pygame.mouse.get_pos()
            x += self.ship_rotation[0] * i * config.CELL_SIZE - config.CELL_SIZE * 0.5
            y += self.ship_rotation[1] * i * config.CELL_SIZE - config.CELL_SIZE * 0.5
            pic = surface_change.colorize(pic.copy(), color)
            config.window.blit(pic, (x,y))

        # draw bottom-part of the ship
        pic = pygame.transform.rotate(sprites.set_ship_texture0[0], PlaceShipScreen.tuple_to_deg[self.ship_rotation])
        x, y = pygame.mouse.get_pos()
        x += -config.CELL_SIZE * 0.5
        y += -config.CELL_SIZE * 0.5
        pic = surface_change.colorize(pic.copy(), color)
        config.window.blit(pic, (x,y))

image_set0 ['part0','part2',(part0.png),(part2.png)]
image_set1 ['part0','part2',(part0.png),(part2.png)]
image_set2 ['part0','part2',(part0.png),(part2.png)]
image_set3 ['part0','part1','part2', (part0.png), (part1.png),(part2.png)]
image_set4 ['part0','part1','part2', (part0.png), (part1.png),(part2.png)]
image_set5 ['part0','part1','part2', (part0.png), (part1.png),(part2.png)]
image_set6 ['part0','part1','part1','part2', (part0.png), (part1.png),(part1.png), (part2.png)]
image_set7 ['part0','part1','part1','part2', (part0.png),(part1.png),(part1.png),(part2.png)]
image_set8 ['part1','part1','part1','part1','part2', (part0.png), (part1.png),(part1.png),(part1.png),(part2.png)]

ship_texture0_sketch = None
ship_texture0 = [pygame.image.load(f'{path}ship_parts/set0/part{i}.png') for i in range(3)]
   
ship_texture1_sketch = None
ship_texture1 = [pygame.image.load(f'{path}ship_parts/set1/part{i}.png') for i in range(3)]

ship_texture2_sketch = None
ship_texture2 = [pygame.image.load(f'{path}ship_parts/set2/part{i}.png') for i in range(3)]

ship1 = Ship(image_set0 = image_texture0)
ship2 = Ship(image_set1 = image_texture1)
ship3 = Ship(image_set2 = image_texture2)
ship4 = Ship(image_set3 = image_texture1)
ship5 = Ship(image_set4 = image_texture2)
ship6 = Ship(image_set5 = image_texture1)
ship7 = Ship(image_set6 = image_texture2)
ship8 = Ship(image_set7 = image_texture0)
