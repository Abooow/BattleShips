''' The main file for the program
'''

import sys
import pygame
import config
import sprites
import audio

pygame.init()
sprites.init() # Initialize content
audio.init() # Initialize audio

from screens.place_ships_screen import PlaceShipScreen
from screens.battle_screen import BattleScreen
from screens.menu_screen import MenuScreen
from screens.win_screen import WinScreen
from screens.lose_screen import LoseScreen
from screens.test_screen import TestScreen


# Initialize the game window
config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Modern Battleship Extreme Warfare')

# Icon
#icon = pygame.image.load('content\sprites\icon.png')
#pygame.display.set_icon(icon)

config.menu_screen = MenuScreen()

# Sets the current screen to MenuScreen
config.current_screen = LoseScreen()

# clock is used to get a framerate of 60fps
clock = pygame.time.Clock()

#Used font for txt
config.font=pygame.font.SysFont('Tahoma',18, True, False)

fps = []
def main() -> None:
    ''' The main function of the program

    :returns: nothing
    :rtype: None
    '''

    # ---------------------- GameLoop
    while not config.quit_game:
        delta_time = clock.get_time()
        fps.append(delta_time)
        if len(fps) > 60:
            del fps[0]

        if delta_time > 0:
            pygame.display.set_caption(f'Modern Battleship Extreme Warfare - {sum(fps) // 60}')

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