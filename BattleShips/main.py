# The main file for the program

from screens import place_ships_screen
import pygame
import battleships
import config

# Initialize the game window
pygame.init()
config.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption('Modern Battleship Extreme Warfare')
# Icon
icon = pygame.image.load('content\sprites\icon.png')
pygame.display.set_icon(icon)

# Sets the current screen to MenuScreen
config.current_screen = place_ships_screen.PlaceShipScreen()


clock = pygame.time.Clock()

# ---------------------- GameLoop ----------------------------------------
while not config.quit_game:
    # den här filen är typ klar, inget mer behövs skrivas i den här filen.


    # --------------------UPDATE--------------------
    config.current_screen.update(clock.get_time())

    # ---------------------DRAW---------------------
    config.window.fill((0,0,0))
    config.current_screen.draw()
    pygame.display.update()

    # FPS
    clock.tick(60)

pygame.quit()