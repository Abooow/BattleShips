''' This module contains different animations, such as Jet, Missile, Explosion, Water
'''

import pygame
import sprites
import config
import random
import surface_change
from framework.animation import Animation


class Explosion(Animation):
    def __init__(self, position, fps = 12):
        ''' 
        :param position (tuple[int,int]): (x, y) position where the explosion starts
        :param fps (int): the animation speed
        '''

        super().__init__(sprites.anim_explosion, fps, loop=False)

        self.position = position


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

        super().draw(self.position)


class Water(Animation):
    def __init__(self, position, offset = 0, fps = 12):
        ''' 
        :param position (tuple[int,int]): (x, y) position where the explosion starts
        :param fps (int): the animation speed
        '''

        super().__init__(sprites.anim_water, fps, loop=True, offset=offset)

        self.position = position


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

        super().draw(self.position)


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
    _new_anim_missile = surface_change.transform_many(sprites.anim_missile, (1, 1), 180)


    def __init__(self, start_position, max_y, speed, fps = 12, action=None):
        ''' 
        :param position (tuple[int,int]): (x, y) position where the explosion starts
        :param end_y (int): max
        :param speed (int): the rocket speed
        :param fps (int): the animation speed
        '''

        super().__init__(Missile._new_anim_missile, fps, loop=True)

        self.position = (start_position[0] - 6, start_position[1])
        self.max_y = max_y
        self.speed = speed
        self.action = action


    def update(self, delta_time) -> None:
        ''' Updates the missile animation

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        super().update(delta_time)

        if not self.done:
            self.position = (self.position[0], self.position[1] + self.speed)
            if self.position[1] >= self.max_y + 45:
                self.done = True
                if self.action is not None:
                    self.action()
    
                    
    def draw(self) -> None:
        ''' Draws the missile animation to the screen

        :returns: NoReturn
        :rtype: None
        '''

        super().draw(self.position)
