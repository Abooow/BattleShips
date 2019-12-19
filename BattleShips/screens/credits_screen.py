''' This module contains the CreditScreen class
'''

import pygame
import config
from screens.screen import Screen
from framework.animations import Water


class CreditScreen(Screen):
    '''Class for displaying credits in game
    '''


    def __init__(self):
        ''' The initialiazion for the screen
        '''
        super().__init__()


    def load_content(self) -> None:
        ''' All content the are supposed to be loaded/initialized only once at the beginning are meant to belong in this method, this method is called once

        :returns: nothing
        :rtype: None
        '''
        
        super().load_content()
        self.water_anim = animations.Water((0, 0))

    def update(self, delta_time) -> list:
        ''' Every thing that are supposed to update every frame are meant to belong in this method, this method is called 60 FPS
        note: This method is called BEFORE the draw() method

        :param delta_time (int): the time since last frame

        :returns: every events that occured
        :rtype: list[event]
        '''

        super().update(delta_time)
        # update water animation
        self.water_anim.update(delta_time)

    def draw(self) -> None:
        ''' Every thing that are supposed to be drawn are ment to belong in this method, this method is called 60 FPS
        note: This method is called AFTER the update() method

        :returns: nothing
        :rtype: None
        '''

        super().draw()
        # draw water animation
        self.water_anim.draw()