''' This module contains all the sprites used in the BattleShips program
'''

import pygame


# img_  = normal image
# txt_  = image of a text
# set_  = an array of images
# anim_ = animation, an array of images

img_battle_screen_foreground = None
img_accomplished = None
img_crosshair = None
img_explosion = None
img_chopper = None
img_boat1 = None
img_boat2 = None
img_boat3 = None
img_boat4 = None
img_cell = None
img_mute_sound_button = None
img_unmute_sound_button = None
img_start_button = None
img_place_ships_foreground = None
img_place_ships_background = None
img_random_button = None
img_trash_button = None
img_missmarker = None
img_hitmarker = None
img_marked_cell = None
img_killstreak_nuke = None
img_killstreak_airstrike = None
img_killstreak_hellstrike = None
img_killstreak_radarscan = None
img_lose = None

txt_mission_accomplished = None
txt_place_your_ships = None
txt_main_menu = None
txt_game_name = None
txt_restart = None
txt_select = None
txt_start = None
txt_quit = None
txt_nuke = None
txt_airstrike = None
txt_hellstrike = None
txt_radarscan = None
txt_menu = None
txt_respect = None
txt_menu_win_lose = None
txt_restart_win_lose = None
txt_quit_win_lose = None

set_ship_texture0_sketch = None
set_ship_texture0 = None

anim_explosion = None
anim_water_splash = None
anim_missile = None
anim_water = None
anim_radar = None
anim_fire = None
anim_jet = None



def init() -> None:
    ''' Load all sprites

    :returns: nothing
    :rtype: None
    '''
    
    global img_battle_screen_foreground, img_accomplished, img_crosshair, img_explosion, img_chopper, img_boat1, img_boat2, img_boat3, img_boat4, img_cell
    global img_start_button, img_place_ships_foreground, img_place_ships_background, img_random_button, img_trash_button, img_lose
    global img_killstreak_nuke, img_killstreak_airstrike, img_killstreak_hellstrike, img_killstreak_radarscan
    global img_missmarker, img_hitmarker, img_marked_cell
    global txt_mission_accomplished, txt_place_your_ships, txt_main_menu, txt_game_name, txt_restart, txt_select, txt_start, txt_quit, txt_menu
    global txt_nuke, txt_airstrike, txt_hellstrike, txt_radarscan, txt_respect, txt_menu_win_lose, txt_restart_win_lose, txt_quit_win_lose
    global set_ship_texture0_sketch, set_ship_texture0
    global anim_explosion, anim_water_splash, anim_missile, anim_water, anim_radar, anim_fire, anim_jet
    global img_mute_sound_button, img_unmute_sound_button

    path = 'content/sprites/'

    # all img_
    img_battle_screen_foreground = pygame.image.load(f'{path}battle_screen/foreground.png')
    img_accomplished = pygame.image.load(f'{path}win_screen/Accomplished.png')
    img_place_ships_foreground = pygame.image.load(f'{path}place_ship_screen/foreground.png')
    img_place_ships_background = pygame.image.load(f'{path}place_ship_screen/background.png')
    img_crosshair = pygame.image.load(f'{path}battle_screen/crosshair.png')
    img_explosion = pygame.image.load(f'{path}menu_screen/explosion.png')
    img_chopper = pygame.image.load(f'{path}menu_screen/chopper.png')
    img_boat1 = pygame.image.load(f'{path}menu_screen/boat1.png')
    img_boat2 = pygame.image.load(f'{path}menu_screen/boat2.png')
    img_boat3 = pygame.image.load(f'{path}menu_screen/boat3.png')
    img_boat4 = pygame.image.load(f'{path}menu_screen/boat4.png')
    img_cell = pygame.image.load(f'{path}board/cell.png')
    img_missmarker = pygame.image.load(f'{path}board/missmarker.png')
    img_hitmarker = pygame.image.load(f'{path}board/hitmarker.png')
    img_marked_cell = pygame.image.load(f'{path}board/marked_cell.png')
    img_killstreak_nuke = pygame.image.load(f'{path}battle_screen/killstreaks/nuke.png')
    img_killstreak_airstrike = pygame.image.load(f'{path}battle_screen/killstreaks/airstrike.png')
    img_killstreak_hellstrike = pygame.image.load(f'{path}battle_screen/killstreaks/hellstrike.png')
    img_killstreak_radarscan = pygame.image.load(f'{path}battle_screen/killstreaks/radarscan.png')
    img_mute_sound_button = pygame.image.load(f'{path}menu_screen/mute_music_button.png')
    img_unmute_sound_button = pygame.image.load(f'{path}menu_screen/unmute_music_button.png')
    img_lose = pygame.image.load(f'{path}lose_screen/failed.png')

    img_start_button = pygame.image.load(f'{path}place_ship_screen/start_button.png')
    img_random_button = pygame.image.load(f'{path}place_ship_screen/random_button.png')
    img_trash_button = pygame.image.load(f'{path}place_ship_screen/trash_button.png')

    # all txt_
    txt_mission_accomplished = pygame.image.load(f'{path}win_screen/mission_accomplished.png')
    txt_place_your_ships = pygame.image.load(f'{path}place_ship_screen/place_your_ships.png')
    txt_main_menu = pygame.image.load(f'{path}buttons/main_menu.png')
    txt_game_name = pygame.image.load(f'{path}menu_screen/game_name.png')
    txt_restart = pygame.image.load(f'{path}buttons/restart.png')
    txt_select = pygame.image.load(f'{path}buttons/select.png')
    txt_start = pygame.image.load(f'{path}buttons/start.png')
    txt_quit = pygame.image.load(f'{path}buttons/quit.png')
    txt_nuke = pygame.image.load(f'{path}battle_screen/killstreaks/NAMES/txt_nuke.png')
    txt_airstrike = pygame.image.load(f'{path}battle_screen/killstreaks/NAMES/txt_airstrike.png')
    txt_hellstrike = pygame.image.load(f'{path}battle_screen/killstreaks/NAMES/txt_hellstrike.png')
    txt_radarscan = pygame.image.load(f'{path}battle_screen/killstreaks/NAMES/txt_radarscan.png')
    txt_menu = pygame.image.load(f'{path}battle_screen/menu.png')
    txt_respect = pygame.image.load(f'{path}win_screen/respect.png')
    txt_menu_win_lose = pygame.image.load(f'{path}win_screen/buttons_for gameover_win screen/txt_mainmenu.png')
    txt_restart_win_lose = pygame.image.load(f'{path}win_screen/buttons_for gameover_win screen/txt_restart.png')
    txt_quit_win_lose = pygame.image.load(f'{path}win_screen/buttons_for gameover_win screen/txt_quit.png')
    

    # all set_
    set_ship_texture0_sketch = None
    set_ship_texture0 = [pygame.image.load(f'{path}ship_parts/set0/part{i}.png') for i in range(3)]

    # all anim_
    anim_explosion = [pygame.image.load(f'{path}animations/explosion/frame{i}.png') for i in range(4)]
    anim_water_splash = [pygame.image.load(f'{path}animations/water_splash/frame{i}.png') for i in range(8)]
    anim_missile = [pygame.image.load(f'{path}animations/missile/frame{i}.png') for i in range(6)]
    anim_radar = [pygame.image.load(f'{path}animations/radar/frame{i}.png') for i in range(8)]
    anim_water = [pygame.image.load(f'{path}animations/water/frame{i}.png') for i in range(8)]
    anim_fire = [pygame.image.load(f'{path}animations/fire/frame{i}.png') for i in range(10)]
    anim_jet = [pygame.image.load(f'{path}animations/jet/frame{i}.png') for i in range(5)]
