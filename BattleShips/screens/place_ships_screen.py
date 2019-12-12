# The screen for place ships,
# everything that have to do with PlaceShips state should be in in here

import pygame
import random
import config
import pic_module

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

        super().__init__()


    def load_content(self):
        self.image = pic_module.boat_bottom
        self.org_img = self.image
        self.text_img = pygame.image.load(r'content\sprites\placeYourShips.png')
        self.amount = 50
        self.xy = []
        self.creat_rain()
       
        super().load_content()
        

    def creat_rain(self):
        for i in range(self.amount):
            x = random.randint(0, config.SCREEN_WIDTH)
            y = random.randint(0, config.SCREEN_HEIGHT)
            speed = random.randint(10,20)
            self.xy.append((x, y, speed))


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
            green = (i[2], 255-i[2]*2, 72-i[2])
            pygame.draw.rect(config.window, green, (i[0],i[1],10,100))

        config.window.blit(self.text_img, (config.SCREEN_WIDTH*0.5-self.text_img.get_rect().size[0]*0.5, config.SCREEN_HEIGHT*0.05))

        config.window.blit(pic_module.board_water, (100, 100))
        self.board.draw((100, 100))
        self._draw_ship()

        super().draw() 


    def __place_ship(self):
        mouse = pygame.mouse.get_pos()
        cell = ((mouse[0] - 100) // 50, (mouse[1] - 100) // 50)
        ship = Ship(cell, self.ship_length, self.ship_rotation)
        if self.board.can_place_ship(ship):
            self.board.place_ship(ship)


    def _draw_ship(self):
        # draw toppart
        pic = pygame.transform.rotate(pic_module.boat_top, PlaceShipScreen._shipRotation_to_deg[self.ship_rotation])
        x, y = pygame.mouse.get_pos()
        x += self.ship_rotation[0] * (self.ship_length - 1) * 50 - 25
        y += self.ship_rotation[1] * (self.ship_length - 1) * 50 - 25
        config.window.blit(pic, (x,y))

        # draw midpart
        pic = pygame.transform.rotate(pic_module.boat_middle, PlaceShipScreen._shipRotation_to_deg[self.ship_rotation])
        for i in range(1, self.ship_length - 1):
            x, y = pygame.mouse.get_pos()
            x += self.ship_rotation[0] * i * 50 - 25
            y += self.ship_rotation[1] * i * 50 - 25
            config.window.blit(pic, (x,y))

        # draw bottompart
        pic = pygame.transform.rotate(pic_module.boat_bottom, PlaceShipScreen._shipRotation_to_deg[self.ship_rotation])
        x, y = pygame.mouse.get_pos()
        x += -25
        y += -25
        config.window.blit(pic, (x,y))
