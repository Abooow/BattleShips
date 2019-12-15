# The screen for place ships,
# everything that have to do with PlaceShips state should be in in here

import pygame
import random
import config
import sprites
import surface_change

from screens.screen import Screen
from framework.board import Board
from framework.ship import Ship


class PlaceShipScreen(Screen):
    _shipRotation_to_deg = {
            (1, 0) : 270,
            (-1, 0) : 90,
            (0, 1) : 180,
            (0, -1) : 0 }


    def __init__(self):
        self.board = Board()
        self.ship_rotation = (-1, 0)
        self.ship_length = 5
        self.cell_size = 40
        self.board_pos = (123, 120)

        super().__init__()


    def load_content(self):
        self.amount = 50
        self.xy = []
        self._creat_rain()
       
        super().load_content()
        

    def update(self, delta_time):
        events = super().update(delta_time)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.__place_ship()

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

        for i in range(self.amount):
            if (self.xy[i][1] > config.SCREEN_HEIGHT):
                x = random.randint(0,config.SCREEN_WIDTH)
                self.xy[i] = (x, -100, self.xy[i][2])
            self.xy[i] = (self.xy[i][0], self.xy[i][1]  + self.xy[i][2], self.xy[i][2])

        super().update(delta_time)


    def draw(self):
        for i in self.xy:
            green = (i[2]*3, 100+i[2]*5, 200-i[2]*6)
            pygame.draw.rect(config.window, green, (i[0],i[1],10,100))

        config.window.blit(sprites.img_explosion, (0, 0))

        self.board.draw(self.board_pos, self.cell_size)
        self._draw_ship()

        super().draw() 


    def _creat_rain(self):
        for i in range(self.amount):
            x = random.randint(0, config.SCREEN_WIDTH)
            y = random.randint(0, config.SCREEN_HEIGHT)
            speed = random.randint(8,30)
            self.xy.append((x, y, speed))


    def __place_ship(self):
        mouse = pygame.mouse.get_pos()
        cell_index = ((mouse[0] - self.board_pos[0]) // self.cell_size, (mouse[1] - self.board_pos[1]) // self.cell_size)
        ship = Ship(sprites.set_ship_texture0, cell_index, self.ship_length, self.ship_rotation)
        self.board.place_ship(ship)


    def _draw_ship(self):
        color = (255, 255, 255) if self._can_place() else (255, 50, 50)

        # draw toppart
        pic = pygame.transform.rotate(sprites.set_ship_texture0[2], PlaceShipScreen._shipRotation_to_deg[self.ship_rotation])
        x, y = pygame.mouse.get_pos()
        x += self.ship_rotation[0] * (self.ship_length - 1) * self.cell_size - self.cell_size * 0.5
        y += self.ship_rotation[1] * (self.ship_length - 1) * self.cell_size - self.cell_size * 0.5
        pic = surface_change.colorize(pic.copy(), color)
        config.window.blit(pic, (x,y))

        # draw midpart
        pic = pygame.transform.rotate(sprites.set_ship_texture0[1], PlaceShipScreen._shipRotation_to_deg[self.ship_rotation])
        for i in range(1, self.ship_length - 1):
            x, y = pygame.mouse.get_pos()
            x += self.ship_rotation[0] * i * self.cell_size - self.cell_size * 0.5
            y += self.ship_rotation[1] * i * self.cell_size - self.cell_size * 0.5
            
            pic = surface_change.colorize(pic.copy(), color)
            config.window.blit(pic, (x,y))

        # draw bottompart
        pic = pygame.transform.rotate(sprites.set_ship_texture0[0], PlaceShipScreen._shipRotation_to_deg[self.ship_rotation])
        x, y = pygame.mouse.get_pos()
        x += -self.cell_size * 0.5
        y += -self.cell_size * 0.5
        pic = surface_change.colorize(pic.copy(), color)
        config.window.blit(pic, (x,y))



    def _can_place(self):
        mouse = pygame.mouse.get_pos()
        cell_index = ((mouse[0] - self.board_pos[0]) // self.cell_size, (mouse[1] - self.board_pos[1]) // self.cell_size)
        ship = Ship(sprites.set_ship_texture0, cell_index, self.ship_length, self.ship_rotation)
        return self.board.can_place_ship(ship)
