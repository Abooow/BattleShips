''' A module that contains a few classes for testing
'''

import pygame
import random
import sprites
import surface_change

from screens.screen import Screen
from framework.button import Button
from framework.animation import Animation
from framework.animations import Water, Explosion, Jet, Missile


class emir(Screen):

    def __init__(self):
        super().__init__()

    def load_content(self):            
        super().load_content()
        self.Water = Water(0,0)
        self.Explosion = Explosion(0,0)
        self.Jet = Jet(300,300)
        self.Missile = Missile(600,400)

    def update(self, delta_time):         
        super().update(delta_time)
        self.Water.update(delta_time)
        self.Explosion.update(delta_time)
        self.Jet.update(delta_time)
        self.Missile.update(delta_time)

    def draw(self):
        super().draw()
        self.Water.draw()
        self.Explosion.draw()
        self.Jet.draw()
        self.Missile.draw()

        