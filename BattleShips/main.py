''' The main file for the program
'''

import pygame
import config
import sprites

from screens.place_ships_screen import PlaceShipScreen
from screens.menu_screen import MenuScreen
from screens.test_screen import TestScreen


# Initialize the game window
pygame.init()
config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Modern Battleship Extreme Warfare')

# Initialize content
sprites.init()

# Icon
#icon = pygame.image.load('content\sprites\icon.png')
#pygame.display.set_icon(icon)

# Sets the current screen to MenuScreen
config.current_screen = MenuScreen()

clock = pygame.time.Clock()


def main():
    # ---------------------- GameLoop
    while not config.quit_game:
        delta_time = clock.get_time()

        if delta_time > 0:
            pygame.display.set_caption(f'Modern Battleship Extreme Warfare - {1000 // delta_time}')

        # --------------------UPDATE--------------------
        config.current_screen.update(delta_time) # update everything in the current screen

        # ---------------------DRAW---------------------
        config.window.fill((20, 20, 20))    # clear screen
        config.current_screen.draw()        # draw everything in the current screen
        pygame.display.update()             # render everything

        # FPS
        clock.tick(60)

if __name__ == '__main__':
    main()
    pygame.quit()