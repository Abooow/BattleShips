import pygame
import os
import sys


boat_bottom = None
boat_middle = None
boat_top = None
board_water = None
explosion = None


menu_text = None
menu_start_button = None
menu_quit_button = None

menu_chopper = None
menu_boat1 = None
menu_boat2 = None
menu_explosion = None



def boat_parts():
    global boat_bottom, boat_middle, boat_top

    boat_bottom = pygame.image.load('Content/Sprites/Battleships_Design/boat_parts/boat_bottom.png')
    boat_middle = pygame.image.load('Content/Sprites/Battleships_Design/boat_parts/boat_middle.png')
    boat_top = pygame.image.load('Content/Sprites/Battleships_Design/boat_parts/boat_top.png')



path = 'Content/Sprites/'




def explosion():
    global explosion
    explosion = []
    
    for j in range(1,6):
        explosion.append(pygame.image.load(path+f'explosion/ex_{j}.png'))
            
    
explosion()



def menu_layout():
    global menu_text, menu_start_button, menu_quit_button, menu_chopper, menu_boat1, menu_boat2, menu_explosion
    
    #Menu_design
    menu_text = pygame.image.load(path+f'test/Menu_text.png')
    menu_chopper = pygame.image.load(path+f'main_menu_parts/chopper.png')
    menu_boat1 = pygame.image.load(path+f'main_menu_parts/boat1.png')
    menu_boat2 = pygame.image.load(path+f'main_menu_parts/boat2.png')
    menu_explosion = pygame.image.load(path+f'main_menu_parts/explosion.png')

    #Menu_buttons
    menu_start_button = pygame.image.load(path+f'Menu/Start_button.png')
    menu_quit_button = pygame.image.load(path+f'Menu/Quit_button.png')
    





def board_layout():
    global board_water

    board_water = pygame.image.load(path+f'test/vatten.jpg')
    board_route = pygame.image.load(path+f'Diverse/Ruta.png')



def init():
    menu_layout()
    board_layout()
    boat_parts()
    explosion()


    

       