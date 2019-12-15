# The screen for the main menu,
# everything that have to do with Menu state should be in in here

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
    def __init__(self):
        super().__init__()


    def load_content(self):
        super().load_content()
        #clip = mp.VideoFileClip(r"content\sprites\puff.mp4")
        #clip_resized = clip.resize(width=1024)
        #clip_resized.preview()
        #pygame.mixer.music.load(r'content\sprites\heli_sound.mp3')
        #pygame.mixer.music.play(0)
        #config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        self.x = 0
        self.y = 0


    def update(self, delta_time):
        super().update(delta_time)

        self.y = math.sin(self.x/100)*80

        self.x += 5
        if self.x == 2000:
            self.x = 0


    def draw(self):
        super().draw()

        config.window.blit(sprites.txt_game_name, (10, 0))
        config.window.blit(sprites.txt_start, (448, 300))
        config.window.blit(sprites.txt_quit, (445, 350))
        config.window.blit(sprites.img_boat1, (-400, 200))
        config.window.blit(sprites.img_boat2, (320, 260))
        config.window.blit(sprites.img_chopper, (1000-self.x, 0-self.y))
