import pygame
import battleships
import screens


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480


exit = False
current_screen = screens.MenuScreen()

while not exit:
        current_screen.update()

        current_screen.draw()
