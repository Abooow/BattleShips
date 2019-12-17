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
        :param x (int): X position where the explosion starts
        :param y (int): Y position where the explosion starts
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


class Water(Animation):
    def __init__(self, x, y, fps = 12):
        ''' 
        :param x (int): X position where the water starts
        :param y (int): Y position where the water starts
        :param fps (int): the animation speed
        '''

        super().__init__(sprites.anim_water, fps, loop=True)

        self.x = x
        self.y = y
        self.max_y = 550 - random.random() * 100


    def update(self, delta_time) -> None:
        ''' Updates the water animation

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''
        super().update(delta_time)


    def draw(self) -> None:
        ''' Draws the water animation to the screen

        :returns: NoReturn
        :rtype: None
        '''
        super().draw((self.x, self.y))


class Jet(Animation):
    def __init__(self, x, y, fps = 12):
        ''' 
        :param x (int): X position where the jet starts
        :param y (int): Y position where the jet starts
        :param fps (int): the animation speed
        '''

        super().__init__(sprites.anim_jet, fps, loop=True)

        self.x = x
        self.y = y
        self.max_y = 550 - random.random() * 100


    def update(self, delta_time) -> None:
        ''' Updates the jet animation

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''
        super().update(delta_time)


    def draw(self) -> None:
        ''' Draws the jet animation to the screen

        :returns: NoReturn
        :rtype: None
        '''
        super().draw((self.x, self.y))


class Missile(Animation):
    def __init__(self, x, y, fps = 12):
        ''' 
        :param x (int): X position where the missile starts
        :param y (int): Y position where the missile starts
        :param fps (int): the animation speed
        '''

        super().__init__(sprites.anim_missile, fps, loop=True)

        self.x = x
        self.y = y
        self.max_y = 550 - random.random() * 100


    def update(self, delta_time) -> None:
        ''' Updates the missile animation

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''
        super().update(delta_time)


    def draw(self) -> None:
        ''' Draws the missile animation to the screen

        :returns: NoReturn
        :rtype: None
        '''
        super().draw((self.x, self.y))
