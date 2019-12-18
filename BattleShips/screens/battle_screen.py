import pygame
import config
import sprites
import framework.ai as ai
import framework.animations as animations

from framework.ship import Ship
from framework.board import Board
from framework.button import Button
from screens.screen import Screen


class BattleScreen(Screen):
    def __init__(self):
        super().__init__()


    def load_content(self) -> None:
        '''
        '''

        super().load_content()

        escape_menu_button = Button(rect=((config.SCREEN_WIDTH-57.5)*0.5,512,55,17),bg=(0,255,0),action=self._esc_menu_button)

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

        self.player = Board()
        self.enemy = ai.SmartAI()
        self.player_board_pos = (74, 93)
        self.enemy_board_pos = (549, 93)

        Board.place_ships_randomly(self.player)


    def update(self, delta_time):
        events = super().update(delta_time)

        # update water animation
        self.water_anim.update(delta_time)

        # enemy shoot
        if not self.player_turn and self.missile_shot is None:
            self._enemy_shoot()

        # get event
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.player_turn:
                self._shoot_at_enemy()


        if self.missile_shot is not None:
            self.missile_shot.update(delta_time)


        self.player.update(delta_time)
        self.enemy.board.update(delta_time)


    def draw(self):

        # draw water animation
        self.water_anim.draw()

        # draw player board
        self.player.draw(self.player_board_pos)

        # draw player board
        self.enemy.board.draw_enemy(self.enemy_board_pos)

        # when it's players turn
        if self.player_turn and self.missile_shot is None:
            self._draw_hovering_cell() # draw the hovering cell
            self._draw_crosshair()     # draw crosshair

            
        # draw foreground
        config.window.blit(sprites.img_battle_screen_foreground, (0, 0))
        
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


    def _shoot(self, board, index) -> None:
        self.player_turn = not self.player_turn
        self.missile_shot = None
        board.shoot_at(index)


    def _create_missile(self, enemy, position, shoot_cord):
        start_pos = (position[0], -75)
        end_pos = position[1] + shoot_cord[1] * config.CELL_SIZE
        self.missile_shot = animations.Missile(start_pos, end_pos, speed=15, 
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
        config.current_screen = config.menu_screen

    #killstreaks
    def _killstreak_nuke(self):
        None

    def _killstreak_airstrike(self):
        None

    def _killstreak_hellstrike(self):
        None

    def _killstreak_radarscan(self):
        None


class GameState():
    PLAYER_TURN = 0
    ENEMY_TURN = 1