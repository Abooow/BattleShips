''' This module contains the MenuScreen which is the first screen to be shown when the program starts

everything that have to do with Menu state should be in in here
'''

import pygame
import random
import math
import config
import sprites
#import moviepy.editor as mp

#from moviepy.editor import VideoFileClip
#from moviepy.video.fx.resize import resize
from screens.screen import Screen
from framework.ship import Ship
from framework.board import Board


class MenuScreen(Screen):
    ''' The screen for the main menu


    This screen can change the current_screen to:
        PlaceShipScreen - when the start button is pressed

    other functionalities:
        Quit the program - when the quit button is pressed
    '''


    def __init__(self):
        super().__init__()


    def load_content(self) -> None:
        ''' Initializes/load all content

        :returns: NoReturn
        :rtype: None
        '''

        super().load_content()

        #clip = mp.VideoFileClip(r"content\sprites\puff.mp4")
        #clip_resized = clip.resize(width=1024)
        #clip_resized.preview()
        #pygame.mixer.music.load(r'content\sprites\heli_sound.mp3')
        #pygame.mixer.music.play(0)
        #config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        self.heli_x = 0
        self.heli_y = 0


    def update(self, delta_time) -> None:
        ''' Updates everything

        :returns: NoReturn
        :rtype: None
        '''

        super().update(delta_time)

        self.heli_y = math.sin(self.heli_x/100)*80

        self.heli_x += 5
        if self.heli_x == 2000:
            self.heli_x = 0


    def draw(self) -> None:
        ''' Draws everything to the screen

        :returns: NoReturn
        :rtype: None
        '''

        super().draw()

        config.window.blit(sprites.txt_game_name, (10, 0))
        config.window.blit(sprites.txt_start, (448, 300))
        config.window.blit(sprites.txt_quit, (445, 350))
        config.window.blit(sprites.img_boat1, (-400, 200))
        config.window.blit(sprites.img_boat2, (320, 260))
        config.window.blit(sprites.img_chopper, (1000-self.heli_x, 0-self.heli_y))
