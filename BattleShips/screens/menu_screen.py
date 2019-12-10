# The screen for the main menu,
# everything that have to do with Menu state should be in in here
import pygame

from screens.screen import Screen


class MenuScreen(Screen):
    def __init__(self):
        super().__init__()


    def load_content(self):
        super().load_content()


    def update(self, delta_time):
        super().update(delta_time)


    def draw(self):
        super().draw()
        start = pygame.image.load(r'content\Menu_test4.png')
        start = pygame.transform.scale(start, (1000, 800))
        window.blit(start, (0, -145))