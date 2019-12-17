''' This module contains the PlaceShipScreen which is the second screen to be shown

everything that have to do with PlaceShips state should be in in here
'''

import pygame
import random
import config
import sprites
import surface_change
import utils

from screens.screen import Screen
from screens.battle_screen import BattleScreen
from framework.board import Board
from framework.ship import Ship
from framework.button import Button


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
        #Creates start, trash and random buttons
        start_button = Button(rect=(780, 637, 186, 51), bg=None, hc=(0, 100, 0),  image=(sprites.img_start_button), action=self._start_game_button)
        trash_button = Button(rect=(434, 637, 77, 51), bg=None, hc=(0, 100, 0), image=(sprites.img_trash_button), action=self._trash_button)
        random_button = Button(rect=(540, 637, 77, 51), bg=None, hc=(0, 100, 0),  image=(sprites.img_random_button),action=self._random_button)

        #Adds the buttons to the "buttons" -list
        self.buttons.append(start_button)
        self.buttons.append(trash_button)
        self.buttons.append(random_button)
        
        self.board = Board()            # the board to place the ships on
        self.ship_rotation = (-1, 0)    # the rotaion of the ship
        self.ship_length = 5            # the lenth of the ship
        self.board_pos = (233, 120)     # where to draw the board

        

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


    def draw(self) -> None:
        ''' Draws everything to the screen

        :returns: NoReturn
        :rtype: None
        ''' 

        # draw background
        config.window.blit(sprites.img_place_ships_background, (0, 0))

        #Draw foreground
        config.window.blit(sprites.img_place_ships_foreground, (0, 0))

        # draw board
        self.board.draw(self.board_pos)
        #draw ship
        self._draw_ship()

        super().draw()

    
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


    def _start_game_button(self):
        config.current_screen = BattleScreen()

    
    def _random_button(self):
        self._trash_button()
        utils.place_ships_randomly(self.board)
        
    
    def _trash_button(self):
        self.board = Board()