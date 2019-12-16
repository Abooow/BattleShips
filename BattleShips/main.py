''' The main file for the program
'''

import sys
import pygame
import config
import sprites

sprites.init() # Initialize content

from screens.place_ships_screen import PlaceShipScreen
from screens.battle_screen import BattleScreen
from screens.menu_screen import MenuScreen
from screens.test_screen import TestScreen

>>>>>>> battle_screen_health

# Initialize the game window
pygame.init()
config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Modern Battleship Extreme Warfare')

# Icon
#icon = pygame.image.load('content\sprites\icon.png')
#pygame.display.set_icon(icon)

# Sets the current screen to MenuScreen
config.current_screen = BattleScreen()

# clock is used to get a framerate of 60fps
clock = pygame.time.Clock()


def main() -> None:
    ''' The main function of the program
    '''

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

        clock.tick(60) # set the FPS to 60

if __name__ == '__main__':
    # main loop
    main()

    # Quit
    pygame.quit()
    #sys.exit()