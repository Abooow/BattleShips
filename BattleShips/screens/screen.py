
import pygame
import config


class Screen():
    '''Base class for all screens
    '''

    def __init__(self):
        self.load_content()


    def load_content(self):
        pass


    def update(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.quit_game = True


    def draw(self):
        pass
