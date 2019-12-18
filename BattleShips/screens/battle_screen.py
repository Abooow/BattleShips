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
    def __init__(self, board):
        super().__init__()


        self.player = board


    def load_content(self) -> None:
        '''
        '''

        super().load_content()

        escape_menu_button = Button(rect=(89,512,55,17),bg=(0,255,0),action=self._esc_menu_button)

        self.buttons.append(escape_menu_button)

        self.water_anim = animations.Water((0, 0))
        self.player_turn = True
        self.change_turn = False

        self.enemy = ai.SmartAI()
        self.player_board_pos = (74, 93)
        self.enemy_board_pos = (549, 93)

        


    def update(self, delta_time):
        events = super().update(delta_time)

        # update water animation
        self.water_anim.update(delta_time)

        # enemy shoot
        if not self.player_turn:
            self._enemy_shoot()

        # get event
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.player_turn:
                self._shoot_at_enemy()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player = Board()
                    Board.place_ships_randomly(self.player)


    def draw(self):

        # draw water animation
        self.water_anim.draw()

        # draw player board
        self.player.draw(self.player_board_pos)

        # draw player board
        self.enemy.board.draw_enemy(self.enemy_board_pos)

        # when it's players turn
        if self.player_turn:
            self._draw_hovering_cell() # draw the hovering cell
            self._draw_crosshair()     # draw crosshair

            
        # draw foreground
        config.window.blit(sprites.img_battle_screen_foreground, (0, 0))
        
        # draw player's ships health squares bottom left
        self._draw_player_ship_health()
        # draw player's ships health squares bottom right
        self._draw_enemy_ship_health()

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


    def _enemy_shoot(self):
        self.enemy.shoot(self.player)
        self.player_turn = True


    def _shoot_at_enemy(self):
        index = self._get_cell_index_at_mouse()

        if 0 <= index[0] < 10 and 0 <= index[1] < 10:
            if self.enemy.board.shoot_at(index)[0]:
                self.player_turn = False


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


class GameState():
    PLAYER_TURN = 0
    ENEMY_TURN = 1