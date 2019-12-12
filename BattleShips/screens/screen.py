
import pygame
import config


class Screen():
    '''Base class for all screens
    '''

    def __init__(self):
        self.buttons = []
        self.animations = []
        self.load_content()


    def load_content(self):
        pass


    def update(self, delta_time):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                config.quit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.buttons:
                    button.update(self)


        for animation in self.animations:
            animation.update(delta_time)
            if animation.done and not animation.loop:
                self.animations.remove(animation)

        return events


    def draw(self):
        for button in self.buttons:
            button.draw()