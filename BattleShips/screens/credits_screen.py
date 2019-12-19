''' This module contains the CreditScreen class
'''

import pygame
import config
import audio
import sprites
import framework.animations as animations

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
        super().load_content()
        
        audio.play_song(audio.song_credits)

        self.credits_y = 0
        self.credits_speed = 4
        self.water_anim1 = animations.Water((0, 0))
        self.water_anim2 = animations.Water((0,512), 7)


    def update(self, delta_time) -> None:
        events = super().update(delta_time)

        # update water animation
        self.water_anim1.update(delta_time)
        self.water_anim2.update(delta_time)

        self.credits_y -= self.credits_speed

        for event in events:
            if event.type == pygame.KEYDOWN:
                audio.play_song(audio.song_main_menu)
                config.current_screen = config.menu_screen


    def draw(self) -> None:
        # draw water animation
        self.water_anim1.draw()
        self.water_anim2.draw()

        if self.credits_y >= -2800:
            config.window.blit(sprites.txt_credits, (0, self.credits_y))
        else:
            config.window.blit(sprites.txt_credits, (0, -2800))

        super().draw()