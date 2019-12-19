import pygame
import math
import config
import sprites
import audio
import framework.ai as ai
import framework.animations as animations

from framework.ship import Ship
from framework.board import Board
from framework.button import Button
from screens.screen import Screen
from screens.win_screen import WinScreen
from screens.lose_screen import LoseScreen


class BattleScreen(Screen):
    def __init__(self, placeship_screen, board):
        super().__init__()

        self.placeship_screen = placeship_screen
        self.player = board


    def load_content(self) -> None:
        '''
        '''

        super().load_content()
        audio.play_song(audio.song_game_background)
        escape_menu_button = Button(rect=((config.SCREEN_WIDTH-52)*0.5,515,sprites.txt_menu.get_width(),sprites.txt_menu.get_height()), image=sprites.txt_menu, action=self._esc_menu_button, bg=(None))

        #killstreaks buttons
        killstreak_nuke = Button(rect=(380,570,sprites.img_killstreak_nuke.get_width(),sprites.img_killstreak_nuke.get_height()), image=sprites.img_killstreak_nuke, action=self._killstreak_nuke)
        killstreak_airstrike = Button(rect=(380,640,sprites.img_killstreak_airstrike.get_width(),sprites.img_killstreak_airstrike.get_height()), image=sprites.img_killstreak_airstrike, action=self._killstreak_airstrike)
        killstreak_hellstrike = Button(rect=(600,570,sprites.img_killstreak_hellstrike.get_width(),sprites.img_killstreak_hellstrike.get_height()), image=sprites.img_killstreak_hellstrike, action=self._killstreak_hellstrike)
        killstreak_radarscan = Button(rect=(600,640,sprites.img_killstreak_radarscan.get_width(),sprites.img_killstreak_radarscan.get_height()), image=sprites.img_killstreak_radarscan, action=self._killstreak_radarscan)

        self.buttons.append(escape_menu_button)
        self.buttons.append(killstreak_nuke)
        self.buttons.append(killstreak_airstrike)
        self.buttons.append(killstreak_hellstrike)
        self.buttons.append(killstreak_radarscan)

        self.missile_shot = None

        self.water_anim = animations.Water((0, 0))
        self.player_turn = True
        self.change_turn = False
        self.can_shoot = True
        self.timer = 0

        self.enemy = ai.SmartAI()
        self.player_board_pos = (74, 93)
        self.enemy_board_pos = (549, 93)

        self.delay  = 500
        self.hand_x = 0

        
    def update(self, delta_time):
        events = super().update(delta_time)

        # update water animation
        self.water_anim.update(delta_time)

        # enemy shoot
        if not self.player_turn and self.timer > self.delay and self.missile_shot is None:
            self._enemy_shoot()
        elif not self.player_turn and self.missile_shot is None:
            self.timer += delta_time


        # get event
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.player_turn and self.can_shoot:
                self._shoot_at_enemy()


        if self.missile_shot is not None:
            self.missile_shot.update(delta_time)


        self.hand_x += 1
        self.player.update(delta_time)
        self.enemy.board.update(delta_time)


    def draw(self):

        # draw water animation
        self.water_anim.draw()

        config.window.blit(sprites.img_vignette, (0, -175))

        # draw player board
        self.player.draw(self.player_board_pos)

        # draw player board
        self.enemy.board.draw_enemy(self.enemy_board_pos)

        # when it's players turn
        if self.player_turn and self.can_shoot and self.missile_shot is None:
            self._draw_hovering_cell() # draw the hovering cell
            self._draw_crosshair()     # draw crosshair

            
        # draw foreground
        config.window.blit(sprites.img_battle_screen_foreground, (0, 0))

        # draw hand
        hand_img = sprites.img_hand_left if self.player_turn else sprites.img_hand_right
        offset = -40 if self.player_turn else 0
        config.window.blit(hand_img, (460 + math.sin(self.hand_x/5)*10 + offset, 3))
        
         # draw the attack missile
        if self.missile_shot is not None:
            self.missile_shot.draw()

        # draw player's ships health squares bottom left
        self._draw_player_ship_health()
        # draw player's ships health squares bottom right
        self._draw_enemy_ship_health()

        # killstreak names
        config.window.blit(sprites.txt_nuke, (375, 555))
        config.window.blit(sprites.txt_airstrike, (350, 625))
        config.window.blit(sprites.txt_hellstrike, (560, 555))
        config.window.blit(sprites.txt_radarscan, (560, 625))

        #killstreak points
        #config.window.blit(sprites.txt_7, (350, 585))
        #config.window.blit(sprites.txt_3, (570, 585))
        #config.window.blit(sprites.txt_3, (570, 655))
        #config.window.blit(sprites.txt_5, (350, 655))

        super().draw()


    def _draw_player_ship_health(self):
        for y in range(len(self.player.ships)):
            ship = self.player.ships[y]

            for x in range (ship.length):
                if ship.hit_parts[x]: # Hit
                    pygame.draw.rect(config.window, (255, 0, 0), (5 + 25 * x, 535 + (20 * y), 20, 10)) #x,y
                else: # Not hit
                    pygame.draw.rect(config.window, (0, 255, 0), (5 + 25 * x, 535 + (20 * y), 20, 10))


    def _draw_enemy_ship_health(self):

        # draw enemy's ships health squares bottom left
        for y in range(len(self.enemy.board.ships)):
            ship = self.enemy.board.ships[y]
            color = (255, 0, 0) if all(ship.hit_parts) else (0, 255, 0) # sets the color to red (255, 0, 0) if ALL ship_parts is hit, otherwise green (0, 255, 0)

            for x in range (ship.length):
                pygame.draw.rect(config.window, color, (995 - (25 * x), 535 + (20 * y), 20, 10))


    def _get_cell_index_at_mouse(self) -> tuple:
        ''' Get the cell index the mouse is hovering over

        :returns: the (x, y) index
        :rtype: tuple[int,int]
        '''

        mouse = pygame.mouse.get_pos()
        return ((mouse[0] - self.enemy_board_pos[0]) // config.CELL_SIZE,
                (mouse[1] - self.enemy_board_pos[1]) // config.CELL_SIZE)


    def _check_if_won(self):
        # won
        ships = self.enemy.board.ships
        if len([ship for ship in ships if ship.health == 0]) == len(ships):
            pygame.mixer.music.stop()
            config.current_screen = WinScreen(self.placeship_screen)

        # lost
        ships = self.player.ships
        if len([ship for ship in ships if ship.health == 0]) == len(ships):
            pygame.mixer.music.stop()
            config.current_screen = LoseScreen(self.placeship_screen)
            #audio.play_song(audio.effect_mission_failed)


    def _shoot(self, board, index) -> None:
        self.player_turn = not self.player_turn
        self.can_shoot = True
        self.missile_shot = None
        board.shoot_at(index)
        self._check_if_won()


    def _create_missile(self, enemy, position, shoot_cord):
        start_pos = (position[0], -75)
        end_pos = position[1] + shoot_cord[1] * config.CELL_SIZE

        self.missile_shot = animations.Missile(start_pos, end_pos, speed=10 + shoot_cord[1] * 2, 
                                               action=lambda: self._shoot(enemy, shoot_cord))


    def _enemy_shoot(self) -> None:
        coord = self.enemy.get_shoot_coordinate(self.player)
        position = (self.player_board_pos[0] + coord[0] * config.CELL_SIZE, 0)
        self._create_missile(self.player, position, coord)


    def _shoot_at_enemy(self):
        coord = self._get_cell_index_at_mouse()

        if 0 <= coord[0] < 10 and 0 <= coord[1] < 10:
            if self.enemy.board.can_shoot_at(coord):
                position = (self.enemy_board_pos[0] + coord[0] * config.CELL_SIZE, 0)
                self._create_missile(self.enemy.board, position, coord)
                self.can_shoot = False
                self.timer = 0


    def _draw_hovering_cell(self):
        index = self._get_cell_index_at_mouse()

        if 0 <= index[0] < 10 and 0 <= index[1] < 10:
            pos = (self.enemy_board_pos[0] + index[0] * config.CELL_SIZE,
                   self.enemy_board_pos[1] + index[1] * config.CELL_SIZE)

            config.window.blit(sprites.img_marked_cell, pos)


    def _draw_crosshair(self):
        mouse = pygame.mouse.get_pos()

        hor_line = (0, mouse[1] - 2, 1024, 4)
        ver_line = (mouse[0] - 2, 0, 4, 700)
        pygame.draw.rect(config.window, (0, 200, 70), hor_line)
        pygame.draw.rect(config.window, (0, 200, 70), ver_line)

        cross_pos = (mouse[0] - 90, mouse[1] - 90)
        config.window.blit(sprites.img_crosshair, cross_pos)


    def _esc_menu_button(self):
        pygame.mixer.music.stop()
        config.current_screen = config.menu_screen
        audio.play_song(audio.song_main_menu)

    #killstreaks
    def _killstreak_nuke(self):
        #7 hits
        None

    def _killstreak_airstrike(self):
        #5 hits
        None

    def _killstreak_hellstrike(self):
        #3 hits
        None

    def _killstreak_radarscan(self):
        #4 hits
        None


class GameState():
    PLAYER_TURN = 0
    ENEMY_TURN = 1