''' This module contains the PlaceShipScreen which is the second screen to be shown

everything that have to do with PlaceShips state should be in in here
'''

import pygame
import random
import config
import sprites
import utils
import surface_change

from framework.button import Button
from framework.board import Board
from framework.ship import Ship
from screens.screen import Screen
from screens.battle_screen import BattleScreen


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
        self.start_button = Button(rect=(780, 637, 186, 51), bg=None, hc=(0, 100, 0),  image=(sprites.img_start_button), action=self._start_game_button)
        self.start_button.visible = False
        trash_button = Button(rect=(434, 637, 77, 51), bg=None, hc=(0, 100, 0), image=(sprites.img_trash_button), action=self._trash_button)
        random_button = Button(rect=(540, 637, 77, 51), bg=None, hc=(0, 100, 0),  image=(sprites.img_random_button),action=self._random_button)

        #Adds the buttons to the "buttons" -list
        self.buttons.append(self.start_button)
        self.buttons.append(trash_button)
        self.buttons.append(random_button)

        self.board = Board()            # the board to place the ships on
        self.board_pos = (233, 120)     # where to draw the board
        self.selected_ship = None
        self.ships_available = [PlaceableShip(ship) for ship in config.ship_types]
        self.placed_ships = []
        
        self._create_ship_buttons()

        

    def update(self, delta_time) -> None:
        ''' Updates everything

        :returns: NoReturn
        :rtype: None
        '''

        events = super().update(delta_time)

        # place ship when mouse clicked
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.selected_ship is not None:
                self._place_ship()

            # rotate ship
            if event.type == pygame.KEYDOWN and self.selected_ship is not None:
                if event.key == pygame.K_LEFT:
                    self.selected_ship.rotation = (-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.selected_ship.rotation = (1, 0)
                if event.key == pygame.K_UP:
                    self.selected_ship.rotation = (0, -1)
                if event.key == pygame.K_DOWN:
                    self.selected_ship.rotation = (0, 1)

        if len(self.placed_ships) == len(config.ship_types):
                self.start_button.visible = True
        else:
            self.start_button.visible = False


    def draw(self) -> None:
        ''' Draws everything to the screen

        :returns: NoReturn
        :rtype: None
        ''' 

        # draw background
        config.window.blit(sprites.img_place_ships_background, (0, 0))

        # draw blueprint
        config.window.blit(sprites.img_place_ships_blueprint, (0, 0))

        # draw ships_background
        config.window.blit(sprites.img_place_ships_ships_background, (0, 0))

        # draw board
        self.board.draw(self.board_pos)

        # draw selected ship
        if self.selected_ship is not None:
            self._draw_selected_ship()
        
        # draw foreground
        config.window.blit(sprites.img_place_ships_foreground, (0, 0))

        # draw available ships
        self._draw_ships_background()
        super().draw()
        self._draw_available_ships()



    def _create_ship_buttons(self):
        y_spacing = 560 / len(config.ship_types)
        start_pos = (993, (y_spacing - 40) * 0.5)

        for i, ship in enumerate(config.ship_types):
            ship_lenth = ship[1]

            position = (start_pos[0] - ship_lenth * 40, start_pos[1] + i * y_spacing)
            size = (ship_lenth * 40, 40)
            rect = (position[0], position[1], size[0], size[1])

            button = Button(rect, bg=None, image=None, action=self._create_lambda(i))
            self.ships_available[i].button = button

            self.buttons.append(button)


    def _create_lambda(self, i):
        return lambda: self._on_pickup(self.ships_available[i])


    def _on_pickup(self, ship):
        if not ship.placed:
            if self.selected_ship is not None:
                self.selected_ship.super.available = True
            self.selected_ship = ship.copy()
            ship.pickup()


    def _draw_available_ships(self):
        y_spacing = 560 / len(config.ship_types)
        start_pos = (953, (y_spacing - 40) * 0.5)

        for i, ship in enumerate(self.ships_available):
            position = (start_pos[0], start_pos[1] + i * y_spacing)
            color = (70, 200, 70) if ship.button._is_hovering() else (255, 255, 255)
            ship.draw(position, color)


    def _draw_ships_background(self):
        y_spacing = 560 / len(config.ship_types)
        start_pos = (953, (y_spacing - 40) * 0.5)

        for i, ship in enumerate(self.ships_available):
            position = (start_pos[0], start_pos[1] + i * y_spacing)
            ship.draw(position, (60, 60, 60), False)


    def _draw_selected_ship(self) -> None:
        ''' Draws the current selected ship at the mouse position
        
        :returns: NoReturn
        :rtype: None
        '''

        # the color for the ship. if can_place then color is white otherwise it's red
        color = (255, 255, 255) if self._can_place() else (255, 50, 50)

        x, y = pygame.mouse.get_pos()
        x += self.selected_ship.rotation[0] - config.CELL_SIZE * 0.5
        y += self.selected_ship.rotation[1] - config.CELL_SIZE * 0.5
       

        self.selected_ship.draw((x, y), color, False)


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
        self.selected_ship.position = cell_index
        ship = self.selected_ship.to_sketch_ship()

        if self._can_place():
            self.placed_ships.append(self.selected_ship)
            self.selected_ship.super.placed = True
            self.board.place_ship(ship)
            self.selected_ship = None
        

    def _can_place(self) -> bool:
        ''' Checks if the current selected ship can be placed on the board

        :returns: True if the ship can be placed, otherwise False
        :rtype: bool
        '''

        cell_index = self._get_cell_index_at_mouse()
        self.selected_ship.position = cell_index
        ship = self.selected_ship.to_ship()
        return self.board.can_place_ship(ship)


    def _bubblesort_ships(self, ships):
    # Swap the elements to arrange in order
        for iter_num in range(len(ships)-1, 0, -1):
            for idx in range(iter_num):
                if ships[idx].length > ships[idx+1].length:
                    ships[idx], ships[idx+1] = ships[idx+1], ships[idx]


    def _blueprint_to_board(self):
        board = Board()
        self._bubblesort_ships(self.placed_ships)
        for ship in self.placed_ships:
            board.place_ship(ship.to_ship())

        return board


    def _start_game_button(self):
        config.current_screen = BattleScreen(self._blueprint_to_board())

    
    def _random_button(self):
        self._trash_button()
        normal_sets = utils.place_ships_randomly(self.board)

        for i, ship in enumerate(self.board.ships):
            new_ship = PlaceableShip()
            new_ship.normal_texture = normal_sets[i]
            new_ship.position = ship.position
            new_ship.rotation = ship.rotation
            new_ship.length = ship.length

            self.placed_ships.append(new_ship)
        
        for ship in self.ships_available:
            ship.placed = True
            ship.available = False
    

    def _trash_button(self):
        self.board = Board()

        # save buttons
        saved_buttons = [ship.button for ship in self.ships_available]

        # reset
        self.selected_ship = None
        self.ships_available = [PlaceableShip(ship) for ship in config.ship_types]
        self.placed_ships = []

        # apply butons
        for i, button in enumerate(saved_buttons):
            self.ships_available[i].button = button


class PlaceableShip():
    # convert the ships rotation (which is a tuple[int,int]) to degrees, so we can use it to rotate the image
    tuple_to_deg = {
        (1, 0) : 270, # right
        (-1, 0) : 90, # left
        (0, 1) : 180, # down
        (0, -1) : 0 } # up

    def __init__(self, ship=None):
        if ship is not None:
            self.normal_texture = sprites.set_ship_textures[ship[0]]
            self.placed_texture = sprites.set_ship_textures_sketch[ship[0]]
        else:
            self.normal_texture = None
            self.placed_texture = None

        self.available = True
        self.placed = False
        self.length = 1 if ship is None else ship[1]
        self.rotation = (-1, 0)
        self.position = None
        self.button = None

        self.super = None


    def pickup(self):
        self.available = False


    def place(self, board, position, rotation):
        self.position = position
        self.rotation = rotation

        ship = self._to_ship()
        board.place(ship)


    def draw(self, position, color = (255, 255, 255), hide = True):
        if hide and not self.available:
            return

        for j in range(self.length):
            # the cell index
            new_position = (position[0] + self.rotation[0] * j * 40, 
                            position[1] + self.rotation[1] * j * 40 )

            # the image index for each part (0=stern, 1=deck, 2=prow)
            image_index = 0 if j == 0 else 2 if j == self.length-1 else 1

            img = surface_change.transform(self.normal_texture[image_index], (1, 1), PlaceableShip.tuple_to_deg[self.rotation])
            img = surface_change.colorize(img, color)
            config.window.blit(img, new_position)


    def to_sketch_ship(self):
        return Ship(self.placed_texture, self.position, self.length, self.rotation)


    def to_ship(self):
        return Ship(self.normal_texture, self.position, self.length, self.rotation)


    def copy(self):
        ship = PlaceableShip()

        ship.normal_texture = self.normal_texture
        ship.placed_texture = self.placed_texture
        ship.available = self.available
        ship.placed = self.placed
        ship.length = self.length
        ship.rotation = self.rotation
        ship.position = self.position
        ship.button = self.button
        ship.super = self

        return ship