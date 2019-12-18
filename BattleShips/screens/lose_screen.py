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
from screens.place_ships_screen import PlaceShipScreen
from screens.menu_screen import MenuScreen



class LoseScreen(Screen):

    def __init__(self):
        super().__init__()


    def load_content(self):            
        super().load_content()
        audio.effect_mission_failed.play()

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

    def draw(self):
        config.window.blit(sprites.img_lose, (0, -100))

        super().draw() # draws the buttons

    def _main_menu(self):
        pygame.mixer.stop()
        config.current_screen = MenuScreen()

    def _place_ships_menu(self):
        pygame.mixer.stop()
        config.current_screen = PlaceShipScreen()

    def _exit_button(self):
        pygame.mixer.stop()
        config.quit_game =True
    