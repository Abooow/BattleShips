''' This module contains all the audio used in the BattleShips program
'''

import pygame
import config

#effects
effect_explosion = None
effect_heli = None
effect_hitmarker = None
effect_miss = None
effect_missile_shooting = None
effect_mission_accomplished = None
effect_mission_failed = None
effect_place_boat = None

#songs
song_game_background = None
song_main_menu = None

def init() -> None:

    #effects 
    global effect_explosion, effect_heli, effect_hitmarker, effect_miss, effect_missile_shooting, effect_mission_accomplished, effect_mission_failed, effect_place_boat
    #songs
    global song_game_background, song_main_menu

    #effects 
    path_effects = 'Content/audio/effects/'
    #songs
    path_songs = 'Content/audio/songs/'

    #load_effects
    effect_explosion = pygame.mixer.Sound(f'{path_effects}effect_explosion.ogg')
    effect_heli = pygame.mixer.Sound(f'{path_effects}effect_heli.ogg')
    effect_hitmarker = pygame.mixer.Sound(f'{path_effects}effect_hitmarker.ogg')
    effect_miss = pygame.mixer.Sound(f'{path_effects}effect_miss.ogg')
    effect_missile_shooting = pygame.mixer.Sound(f'{path_effects}effect_missile_shooting.ogg')
    effect_mission_accomplished = pygame.mixer.Sound(f'{path_effects}effect_mission_accomplished.ogg')
    effect_mission_failed = pygame.mixer.Sound(f'{path_effects}effect_mission_failed.ogg')
    effect_place_boat = pygame.mixer.Sound(f'{path_effects}effect_place_boat.ogg')

    #load_songs
    song_game_background = f'{path_songs}song_game_background.mp3'
    song_main_menu = f'{path_songs}song_main_menu.mp3'

#function to choose what effect is going to be played
def play_effect(effect):
    '''
    play_effect(effect_name)
    '''
    if config.effects_on:
        effect.play()

#function to choose what song is going to be played
def play_song(path):
    '''
    play_song(song_name)
    '''
    pygame.mixer.music.load(path)
    if config.song_on:
        pygame.mixer.music.play(-1)