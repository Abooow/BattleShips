''' This module contains different animations, such as Jet, Missile, Explosion, Water
'''

import pygame
import sprites
import config
import random
import surface_change
from framework.animation import Animation


class Explosion(Animation):
    def __init__(self, x, y, fps = 12):
        ''' 
        :param x (int): X position where the missile starts
        :param y (int): Y position where the missile starts
        :param fps (int): the animation speed
        '''

        super().__init__(sprites.anim_explosion, fps, loop=True)

        self.x = x
        self.y = y
        self.max_y = 550 - random.random() * 100


    def update(self, delta_time) -> None:
        ''' Updates the explosion animation

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''
        super().update(delta_time)


    def draw(self) -> None:
        ''' Draws the explosion animation to the screen

        :returns: NoReturn
        :rtype: None
        '''
        super().draw((self.x, self.y))
       