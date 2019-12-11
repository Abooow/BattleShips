# The main file for the program

from screens import place_ships_screen
import pygame
from framework import ai
import config

# Initialize the game window
pygame.init()
config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('BattleShips')


# Sets the current screen to MenuScreen
config.current_screen = place_ships_screen.PlaceShipScreen()


clock = pygame.time.Clock()

# ---------------------- GameLoop ----------------------------------------
while not config.quit_game:
    # den här filen är typ klar, inget mer behövs skrivas i den här filen.


    # --------------------UPDATE--------------------
    config.current_screen.update(clock.get_time())

    # ---------------------DRAW---------------------
<<<<<<< HEAD
    config.window.fill((255, 255, 255))
=======
    config.window.fill((0, 0, 0))
>>>>>>> b71b0d311b2def795e55c1a11afeed4ea393c46a
    config.current_screen.draw()
    pygame.display.update()

    # FPS
    clock.tick(60)

pygame.quit()