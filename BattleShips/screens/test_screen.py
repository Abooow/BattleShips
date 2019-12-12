
import pygame
import pic_module

from screens.screen import Screen
from framework.button import Button
from framework.animation import Animation


class TestScreen(Screen):
    def __init__(self):
        super().__init__()


    def load_content(self):
        super().load_content()

        self.exp = Animation(pic_module.explosion, 1)
        self.animations = [self.exp]

        self.buttons.append(Button((300, 300, 80, 30), image=pic_module.menu_start_button, bg=(100,10,120), action=self.press))


    def update(self, delta_time):
        events = super().update(delta_time)
        self.exp.update(delta_time)


    def draw(self):
        super().draw()
        self.exp.draw(pygame.mouse.get_pos())


    def press(self, obj):
        self.exp.fps += 1