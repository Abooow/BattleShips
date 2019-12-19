''' This module contains the WinScreen which is the screen to be shown after you win the game
'''

import pygame
import random
import sprites
import surface_change
import audio
import config

from screens.screen import Screen
from framework.button import Button
from framework.animation import Animation


class WinScreen(Screen):

    def __init__(self, placeship_screen):
        super().__init__()

        self.placeship_screen = placeship_screen


    def load_content(self):            
        super().load_content()
        audio.effect_mission_accomplished.play()
        self.moveX = 0

        #start button width and height
        self.SW = sprites.txt_start.get_width()
        self.SH = sprites.txt_start.get_height()

        #quit button width and height
        self.QW = sprites.txt_quit.get_width()
        self.QH = sprites.txt_quit.get_height()

        #text width center alingment for start and quit buttons
        self.SC = config.SCREEN_WIDTH-self.SW
        self.QC = config.SCREEN_WIDTH-self.QW

        restart_button = Button(rect=(self.SC * 0.5, 400, self.SW, self.SH), bg=(), image=sprites.txt_restart_win_lose, action=self._place_ships_menu)
        menu_button = Button(rect=(self.SC * 0.5, 450, self.SW, self.SH), bg=(), image=sprites.txt_menu_win_lose, action=self._main_menu)
        quit_button = Button(rect=(self.QC * 0.5, 500, self.QW, self.QH), bg=(), image=sprites.txt_quit_win_lose, action=self._exit_button)

        self.buttons.append(restart_button)
        self.buttons.append(menu_button)
        self.buttons.append(quit_button)


    def update(self, delta_time):         
        super().update(delta_time)

        #if respect txt is in the middle it will stop moving
        if self.moveX < (config.SCREEN_WIDTH-sprites.txt_respect.get_width())*0.5+25:
            self.moveX += 5     


    def draw(self):
        config.window.blit(sprites.img_accomplished, (0, -100))
        config.window.blit(sprites.txt_respect, (self.moveX, 300))

        super().draw() # draws the buttons


    def _main_menu(self):
        pygame.mixer.stop()
        config.current_screen = config.menu_screen


    def _place_ships_menu(self):
        pygame.mixer.stop()
        config.current_screen = self.placeship_screen


    def _exit_button(self):
        pygame.mixer.stop()
        config.quit_game =True
    