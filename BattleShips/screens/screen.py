
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
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                config.quit_game = True

        return events


    def draw(self):
        pass
