''' A module that contains a few classes for testing
'''

import pygame
import random
import sprites
import surface_change

from screens.screen import Screen
from framework.button import Button
from framework.animation import Animation


class TestScreen(Screen):
    ''' A test screen for testing animations


    This screen can change the current_screen to:
        -

    other functionalities:
        -
    '''


    def __init__(self):
        super().__init__()
        

    def load_content(self) -> None:
        ''' Initializes/load all content

        :returns: NoReturn
        :rtype: None
        '''

        super().load_content()

        self.start = False
        self.jet = Jet()

        start_button = Button(rect=(300, 300, 405, 60), image=sprites.txt_start, bg=(60,60,60), action=self.button_pressed)
        self.buttons.append(start_button)


    def update(self, delta_time) -> None:
        ''' Updates everything

        :returns: NoReturn
        :rtype: None
        '''

        events = super().update(delta_time)

        if self.start:
            self.jet.update(delta_time)


    def draw(self) -> None:
        ''' Draws everything to the screen

        :returns: NoReturn
        :rtype: None
        '''

        super().draw()
        self.jet.draw()


    def button_pressed(self) -> None:
        ''' A method that gets invoked when the START button is pressed

        :returns: NoReturn
        :rtype: None
        '''

        self.start = True
        self.jet.x = -200


class Jet(Animation):
    ''' A jet animation class (TEST)

    can drop bombs, that will explode on impact
    '''


    # a rotated copy of sprites.anim_jet
    new_anim_jet = surface_change.transform_many(sprites.anim_jet, (1, 1), 270)


    def __init__(self, fps=14):
        '''
        :param fps (int): the animation speed
        '''

        super().__init__(Jet.new_anim_jet, fps, True)

        self.missiles = []
        self.x = -200
        self.y = 100


    def update(self, delta_time) -> None:
        ''' Updates the jet animation

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        super().update(delta_time)

        self.x += 8
        #if self.x >= 1124:
            #self.x = -200

        for missile in self.missiles:
            missile.update(delta_time)
                #self.missiles.remove(missile)

        if 1024 > self.x > 0 and random.random() <= 0.1:
            self._drop_bomb()


    def draw(self) -> None:
        ''' Draws the jet to the screen

        :returns: NoReturn
        :rtype: None
        '''

        super().draw((self.x, self.y))

        for missile in self.missiles:
            missile.draw()


    def _drop_bomb(self) -> None:
        ''' Drops a bomb from the jet

        :returns: NoReturn
        :rtype: None
        '''

        self.missiles.append(Missile(self.x, self.y))


class Missile(Animation):
    ''' A missile that will explode on impact
    '''


    # a resized copy of sprites.anim_fire
    new_anim_fire = surface_change.transform_many(sprites.anim_fire, (3, 3), 0)


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
        self._explode = False
        self._explodsion_anim = Animation(sprites.anim_explosion, 12, False)
        self._fire_anim = Animation(Missile.new_anim_fire, 12, True)


    def update(self, delta_time) -> None:
        ''' Updates the missile animation

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        if not self._explode:
            super().update(delta_time)
            self.y += 5

            if self.y >= self.max_y:
                self._explode = True
        else:
            if self._explodsion_anim.done:
                self._fire_anim.update(delta_time)
            else:
                self._explodsion_anim.update(delta_time)


    def draw(self) -> None:
        ''' Draws the missile animation to the screen

        :returns: NoReturn
        :rtype: None
        '''

        if not self._explode:
            super().draw((self.x, self.y))
        else:
            if self._explodsion_anim.done:
                self._fire_anim.draw((self.x - 90, self.y - 50))
            else:
                self._explodsion_anim.draw((self.x - 70, self.y - 50))