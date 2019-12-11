# The screen for place ships,
# everything that have to do with PlaceShips state should be in in here

import pygame
import config
from screens.screen import Screen


class PlaceShipScreen(Screen):
    def __init__(self):
        self.rotation = 0

        super().__init__()


    def load_content(self):
        self.image = pygame.image.load('content/sprites/boat_parts/boat_bottom.png')
        self.org_img = self.image

        super().load_content()


    def update(self, delta_time):
        events = super().update(delta_time)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rotation = 90
                    self.image = pygame.transform.rotate(self.org_img, self.rotation)
                if event.key == pygame.K_RIGHT:
                    self.rotation = 270
                    self.image = pygame.transform.rotate(self.org_img, self.rotation)
                if event.key == pygame.K_UP:
                    self.rotation = 0
                    self.image = pygame.transform.rotate(self.org_img, self.rotation)
                if event.key == pygame.K_DOWN:
                    self.rotation = 180
                    self.image = pygame.transform.rotate(self.org_img, self.rotation)



    def draw(self):
        config.window.blit(self.image, pygame.mouse.get_pos())

        super().draw()