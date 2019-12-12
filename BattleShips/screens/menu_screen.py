# The screen for the main menu,
# everything that have to do with Menu state should be in in here

import pygame
import config
import random
import math
import moviepy.editor as mp

from screens.screen import Screen
from framework.ship import Ship
from framework.board import Board
from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize


class MenuScreen(Screen):
    def __init__(self):
        super().__init__()


    def load_content(self):
        super().load_content()
        clip = mp.VideoFileClip(r"content\sprites\puff.mp4")
        clip_resized = clip.resize(width=1024)
        #clip_resized = clip_resized.volumex(0)
        clip_resized.preview()
        pygame.mixer.music.load(r'content\sprites\heli_sound.mp3')
        pygame.mixer.music.play(0)
        config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.game_name = pygame.image.load(r'content\sprites\Game_name.png')
        self.game_name = pygame.transform.scale(self.game_name, (1000, 35))

        self.start = pygame.image.load(r'content\sprites\Start_button.png')
        self.start = pygame.transform.scale(self.start, (200, 30))

        self.quit = pygame.image.load(r'content\sprites\Quit_button.png')
        self.quit = pygame.transform.scale(self.quit, (200, 30))

        self.boat_1 = pygame.image.load(r'content\sprites\Boat1.png')
        self.boat_1 = pygame.transform.scale(self.boat_1, (1200, 700))

        self.boat_2 = pygame.image.load(r'content\sprites\Boat2.png')
        self.boat_2 = pygame.transform.scale(self.boat_2, (900, 700))

        self.chopper = pygame.image.load(r'content\sprites\chopper.png')
        self.chopper = pygame.transform.scale(self.chopper, (900, 700))
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
        config.window.blit(self.game_name, (10, 0))
        config.window.blit(self.start, (448, 300))
        config.window.blit(self.quit, (445, 350))
        config.window.blit(self.boat_1, (-400, 200))
        config.window.blit(self.boat_2, (320, 260))
        config.window.blit(self.chopper, (1000-self.x, 0-self.y))
