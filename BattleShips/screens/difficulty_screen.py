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
from framework.animations import Water
from screens.place_ships_screen import PlaceShipScreen
from screens.menu_screen import MenuScreen



class DifficultyScreen(Screen):

    def __init__(self):
        super().__init__()


    def load_content(self):            
        super().load_content()
        audio.play_song(audio.song_main_menu)
        self.Water0 = Water((0,0))
        self.Water1 = Water((0,512), 7)

        retard_ai = Button(rect=((config.SCREEN_WIDTH-sprites.txt_retard.get_width())*0.5, 300, sprites.txt_retard.get_width(), sprites.txt_retard.get_height()), bg=(), image=sprites.txt_retard, action=self._retard_ai)
        smart_ai = Button(rect=((config.SCREEN_WIDTH-sprites.txt_smart.get_width())*0.5, 350, sprites.txt_smart.get_width(), sprites.txt_smart.get_height()), bg=(), image=sprites.txt_smart, action=self._smart_ai)
        einstein_ai = Button(rect=((config.SCREEN_WIDTH-sprites.txt_einstein.get_width())*0.5, 400, sprites.txt_einstein.get_width(), sprites.txt_einstein.get_height()), bg=(), image=sprites.txt_einstein, action=self._einstein_ai)
        putin_ai = Button(rect=((config.SCREEN_WIDTH-sprites.txt_putin.get_width())*0.5, 450, sprites.txt_putin.get_width(), sprites.txt_putin.get_height()), bg=(), image=sprites.txt_putin, action=self._putin_ai)

        self.buttons.append(retard_ai)
        self.buttons.append(smart_ai)
        self.buttons.append(einstein_ai)
        self.buttons.append(putin_ai)

    def update(self, delta_time):         
        super().update(delta_time)   
        
        self.Water0.update(delta_time)
        self.Water1.update(delta_time)

    def draw(self):
        self.Water0.draw()
        self.Water1.draw()
        config.window.blit(sprites.img_vignette, (0, 0))
        config.window.blit(sprites.txt_choose_difficulty, ((config.SCREEN_WIDTH-sprites.txt_choose_difficulty.get_width())*0.5, 100))

        super().draw() # draws the buttons

    def _retard_ai(self):
        None

    def _smart_ai(self):
        None

    def _einstein_ai(self):
        None

    def _putin_ai(self):
        None
    