''' This module contains the MenuScreen which is the first screen to be shown when the program starts

everything that have to do with Menu state should be in in here
'''

import pygame
import random
import math
import config
import sprites
import utils
#import moviepy.editor as mp

#from moviepy.editor import VideoFileClip
#from moviepy.video.fx.resize import resize
from screens.screen import Screen
from framework.ship import Ship
from framework.board import Board
from framework.button import Button
from framework.animations import Water
from screens.place_ships_screen import PlaceShipScreen


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
        self.Water0 = Water((0,0))
        self.Water1 = Water((0,512), 7)

        self.sound_effects_button = Button(rect=(450, 580, 50, 50),
                                           image=sprites.img_unmute_sound_button,
                                           hc = (0, 0, 255),bg = None,
                                           action=self._sound_effects_button)
        self.sound_music_button = Button(rect=(525, 580, 50, 50),
                                         image=sprites.img_unmute_sound_button,
                                         hc = (0,0,255), bg = None, 
                                         action=self._sound_music_button)
       
       #start button width and height
        self.SW = sprites.txt_start.get_width()
        self.SH = sprites.txt_start.get_height()

        #quit button width and height
        self.QW = sprites.txt_quit.get_width()
        self.QH = sprites.txt_quit.get_height()

        #text width center alingment for start and quit buttons
        self.SC = config.SCREEN_WIDTH-self.SW
        self.QC = config.SCREEN_WIDTH-self.QW

        start_button = Button(rect=(self.SC * 0.5, 300, self.SW, self.SH), bg=(), image=sprites.txt_start, action=self._place_ships_menu)
        quit_button = Button(rect=(self.QC * 0.5, 400, self.QW, self.QH),bg=None, image=sprites.txt_quit, action=self._exit_button)
    
        self.buttons.append(start_button)
        self.buttons.append(quit_button)
        self.buttons.append(self.sound_effects_button)
        self.buttons.append(self.sound_music_button)


        #clip = mp.VideoFileClip(r"content\sprites\puff.mp4")
        #clip_resized = clip.resize(width=1024)
        #clip_resized.preview()
        #config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        self.heli_x = 0
        self.heli_y = 0

        self.boat2_x = 0
        self.boat2_y = 0

        self.boat1_y = 0


    def update(self, delta_time) -> None:
        ''' Updates everything

        :returns: NoReturn
        :rtype: None
        '''

        super().update(delta_time)

        self.Water0.update(delta_time)
        self.Water1.update(delta_time)

        self.heli_y = math.sin(self.heli_x / 100) * 80
        
        self.heli_x += 5
        if self.heli_x == 2000:
            self.heli_x = 0

        self.boat2_x += 5
        if self.boat2_x == 1500:
            self.boat2_x = -500
        self.boat2_y = math.sin(self.boat2_x/100)*5

        self.boat1_y = math.sin(self.boat2_x/100)*5


    def draw(self) -> None:
        ''' Draws everything to the screen

        :returns: NoReturn
        :rtype: None
        '''

        self.Water0.draw()
        self.Water1.draw()
        config.window.blit(sprites.txt_game_name, ((config.SCREEN_WIDTH-sprites.txt_game_name.get_width())*0.5, 20))
        config.window.blit(sprites.img_boat2, (320-self.boat2_x, 260-self.boat2_y))
        config.window.blit(sprites.img_boat1, (-400, 200-self.boat1_y))
        config.window.blit(sprites.img_chopper, (1000-self.heli_x, 0-self.heli_y))
        

        utils.draw_font('Music', (255,255,255), (523,550))
        utils.draw_font('Effects', (255,255,255), (444,550))


        super().draw()

    
    def _place_ships_menu(self):
        config.current_screen = PlaceShipScreen()


    def _exit_button(self):
        config.quit_game =True
    

    def _sound_effects_button(self):
        if config.sound_effects_on:
            config.sound_effects_on = False
            self.sound_effects_button.image = sprites.img_mute_sound_button
        else:
            config.sound_effects_on = True
            self.sound_effects_button.image = sprites.img_unmute_sound_button


    def _sound_music_button(self):
        if config.sound_song_on:
            config.sound_song_on = False
            self.sound_music_button.image = sprites.img_mute_sound_button
        else:
            config.sound_song_on = True
            self.sound_music_button.image = sprites.img_unmute_sound_button
        pass

    
    def mute_button_txt(self):
        pygame.font.init()
        text = font.render('Soundbutton', True , (0,0,255))