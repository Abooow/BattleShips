import pygame


boat_bottom = None
boat_middle = None
boat_top = None

board_cell = None
board_water = None

explosion_anim = None
fire_anim = None
jet_anim = None
missile_anim = None

menu_text = None
menu_start_button = None
menu_quit_button = None

menu_chopper = None
menu_boat1 = None
menu_boat2 = None
menu_explosion = None


__path = 'content/sprites/'


def init():
    __menu_layout()
    __board_layout()
    __boat_parts()
    __animations()



def __boat_parts():
    global boat_bottom, boat_middle, boat_top

    boat_bottom = pygame.image.load(f'{__path}boat_parts/boat_bottom.png')
    boat_middle = pygame.image.load(f'{__path}boat_parts/boat_middle.png')
    boat_top = pygame.image.load(f'{__path}boat_parts/boat_top.png')


def __animations():
    global explosion_anim, fire_anim, jet_anim, missile_anim

    explosion_anim = [pygame.image.load(f'{__path}explosion/ex_{i+1}.png') for i in range(5)]
    fire_anim = [pygame.image.load(f'{__path}fire_animation/Fire{i+1}_resize.png') for i in range(10)]
    jet_anim = [pygame.image.load(f'{__path}jet/jet{i+1}.png') for i in range(5)]
    missile_anim = [pygame.image.load(f'{__path}missile/{i+1}.png') for i in range(6)]
        

def __menu_layout():
    global menu_text, menu_start_button, menu_quit_button, menu_chopper, menu_boat1, menu_boat2, menu_explosion
    
    #Menu_design
    #menu_text = pygame.image.load(f'{path}test/Menu_text.png')
    menu_chopper = pygame.image.load(f'{__path}main_menu_parts/chopper.png')
    menu_boat1 = pygame.image.load(f'{__path}main_menu_parts/boat1.png')
    menu_boat2 = pygame.image.load(f'{__path}main_menu_parts/boat2.png')
    menu_explosion = pygame.image.load(f'{__path}main_menu_parts/explosion.png')

    #Menu_buttons
    menu_start_button = pygame.image.load(f'{__path}Menu/Start_button.png')
    menu_quit_button = pygame.image.load(f'{__path}Menu/Quit_button.png')
    

def __board_layout():
    global board_water, board_cell

    board_water = pygame.image.load(f'{__path}test/vatten.jpg')
    board_cell = pygame.image.load(f'{__path}board/cell.png')