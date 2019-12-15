''' This module contains all the sprites used in the BattleShips program
'''

import pygame


# img_  = normal image
# txt_  = image of a text
# set_  = an array of images
# anim_ = animation, an array of images

img_explosion = None
img_chopper = None
img_boat1 = None
img_boat2 = None
img_boat3 = None
img_boat4 = None
img_cell = None

txt_mission_accomplished = None
txt_place_your_ships = None
txt_main_menu = None
txt_game_name = None
txt_restart = None
txt_select = None
txt_start = None
txt_quit = None

set_ship_texture0_sketch = None
set_ship_texture0 = None

anim_explosion = None
anim_missile = None
anim_water = None
anim_fire = None
anim_jet = None



def init() -> None:
    ''' Load all sprites

    :returns: nothing
    :rtype: None
    '''

    global img_explosion, img_chopper, img_boat1, img_boat2, img_boat3, img_boat4, img_cell
    global txt_mission_accomplished, txt_place_your_ships, txt_main_menu, txt_game_name, txt_restart, txt_select, txt_start, txt_quit
    global set_ship_texture0_sketch, set_ship_texture0
    global anim_explosion, anim_missile, anim_water, anim_fire, anim_jet

    path = 'content/sprites/'

    # all img_
    img_explosion = pygame.image.load(f'{path}menu_screen/explosion.png')
    img_chopper = pygame.image.load(f'{path}menu_screen/chopper.png')
    img_boat1 = pygame.image.load(f'{path}menu_screen/boat1.png')
    img_boat2 = pygame.image.load(f'{path}menu_screen/boat2.png')
    img_boat3 = pygame.image.load(f'{path}menu_screen/boat3.png')
    img_boat4 = pygame.image.load(f'{path}menu_screen/boat4.png')
    img_cell = pygame.image.load(f'{path}board/cell.png')

    # all txt_
    txt_mission_accomplished = pygame.image.load(f'{path}win_screen/mission_accomplished.png')
    txt_place_your_ships = pygame.image.load(f'{path}place_ship_screen/place_your_ships.png')
    txt_main_menu = pygame.image.load(f'{path}buttons/main_menu.png')
    txt_game_name = pygame.image.load(f'{path}menu_screen/game_name.png')
    txt_restart = pygame.image.load(f'{path}buttons/restart.png')
    txt_select = pygame.image.load(f'{path}buttons/select.png')
    txt_start = pygame.image.load(f'{path}buttons/start.png')
    txt_quit = pygame.image.load(f'{path}buttons/quit.png')

    # all set_
    set_ship_texture0_sketch = None
    set_ship_texture0 = [pygame.image.load(f'{path}ship_parts/set0/part{i}.png') for i in range(3)]

    # all anim_
    anim_explosion = [pygame.image.load(f'{path}animations/explosion/frame{i}.png') for i in range(4)]
    anim_missile = [pygame.image.load(f'{path}animations/missile/frame{i}.png') for i in range(6)]
    anim_water = None
    anim_fire = [pygame.image.load(f'{path}animations/fire/frame{i}.png') for i in range(10)]
    anim_jet = [pygame.image.load(f'{path}animations/jet/frame{i}.png') for i in range(5)]