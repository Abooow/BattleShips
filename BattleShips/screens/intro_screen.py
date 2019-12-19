''' This module contains the IntroScreen class
'''

import pygame
import config
import moviepy.editor as mp

from screens.screen import Screen
from screens.menu_screen import MenuScreen


class IntroScreen(Screen):
    '''Class for displaying credits in game
    '''


    def __init__(self):
        ''' The initialiazion for the screen
        '''
        super().__init__()


    def load_content(self) -> None:
        super().load_content()

        
    def update(self, delta_time) -> None:
        events = super().update(delta_time)

        clip = mp.VideoFileClip(r"content\intro.mp4")
        clip = clip.resize(width=1024)
        clip.preview()

        config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        config.menu_screen = MenuScreen()
        config.current_screen = config.menu_screen

    def draw(self) -> None:
        # draw water animation

        super().draw()