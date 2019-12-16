import pygame
import config
import sprites
<<<<<<< HEAD

from framework.board import Board
from framework.ship import Ship
from screens.screen import Screen
from framework.ai import AI


class BattleScreen(Screen):
    def __init__(self):
        super().__init__()


    def load_content(self) -> None:
        '''
        '''

        super().load_content()

        self.player_turn = True

        self.player = Board()
        self.enemy = AI()
        self.player_board_pos = (74, 93)
        self.enemy_board_pos = (549, 93)

        Board.place_ships_randomely(self.player)


    def update(self, delta_time):
        events = super().update(delta_time)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.player_turn:
                self._shoot_at_enemy()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player = Board()
                    Board.place_ships_randomely(self.player)


    def draw(self):

        # draw player board
        self.player.draw(self.player_board_pos)

        # draw player board
        self.enemy.board.draw_enemy(self.enemy_board_pos)

        if self.player_turn:
            self._draw_hovering_cell() # draw the hovering cell
            self._draw_cross_mark()    # draw cross mark

        # draw foreground
        config.window.blit(sprites.img_battle_screen_foreground, (0, 0))
        
        super().draw()


    def _get_cell_index_at_mouse(self) -> tuple:
        ''' Get the cell index the mouse is hovering over

        :returns: the (x, y) index
        :rtype: tuple[int,int]
        '''

        mouse = pygame.mouse.get_pos()
        return ((mouse[0] - self.enemy_board_pos[0]) // config.CELL_SIZE,
                (mouse[1] - self.enemy_board_pos[1]) // config.CELL_SIZE)


    def _shoot_at_enemy(self):
        index = self._get_cell_index_at_mouse()

        if 0 <= index[0] < 10 and 0 <= index[1] < 10:
            if self.enemy.board.shoot_at(index)[0]:
                return
                self.player_turn = False


    def _draw_hovering_cell(self):
        index = self._get_cell_index_at_mouse()

        if 0 <= index[0] < 10 and 0 <= index[1] < 10:
            pos = (self.enemy_board_pos[0] + index[0] * config.CELL_SIZE + 1,
                   self.enemy_board_pos[1] + index[1] * config.CELL_SIZE + 1)

            pygame.draw.rect(config.window, (150, 150, 150), (pos[0], 
                                                              pos[1], 
                                                              config.CELL_SIZE - 1, 
                                                              config.CELL_SIZE - 1))

    def _draw_cross_mark(self):
        mouse = pygame.mouse.get_pos()

        hor_line = (0, mouse[1] - 2, 1024, 4)
        ver_line = (mouse[0] - 2, 0, 4, 700)

        pygame.draw.rect(config.window, (0, 200, 70), hor_line)
        pygame.draw.rect(config.window, (0, 200, 70), ver_line)



class GameState():
    PLAYER_TURN = 0
    ENEMY_TURN = 1
=======
from framework.board import Board
from framework.ship import Ship
from screens.screen import Screen


class BattleScreen(Screen):
    
    def __init__(self):
        super().__init__()
        
    
    def load_content(self):
        super().load_content()
        
        self.player_board = Board()
        self.enemy_board = Board()
        #test placed boats
        self.player_board.place_ship(Ship(sprites.set_ship_texture0, (0,0), 2, (1, 0)))
        self.player_board.place_ship(Ship(sprites.set_ship_texture0, (0,1), 2, (1, 0)))
        self.player_board.place_ship(Ship(sprites.set_ship_texture0, (0,2), 2, (1, 0)))
        self.player_board.place_ship(Ship(sprites.set_ship_texture0, (0,3), 3, (1, 0)))
        self.player_board.place_ship(Ship(sprites.set_ship_texture0, (0,4), 3, (1, 0)))
        self.player_board.place_ship(Ship(sprites.set_ship_texture0, (0,5), 4, (1, 0)))
        self.player_board.place_ship(Ship(sprites.set_ship_texture0, (0,6), 4, (1, 0)))
        self.player_board.place_ship(Ship(sprites.set_ship_texture0, (0,7), 5, (1, 0)))

        self.enemy_board.place_ship(Ship(sprites.set_ship_texture0, (0,0), 2, (1, 0)))
        self.enemy_board.place_ship(Ship(sprites.set_ship_texture0, (0,1), 2, (1, 0)))
        self.enemy_board.place_ship(Ship(sprites.set_ship_texture0, (0,2), 2, (1, 0)))
        self.enemy_board.place_ship(Ship(sprites.set_ship_texture0, (0,3), 3, (1, 0)))
        self.enemy_board.place_ship(Ship(sprites.set_ship_texture0, (0,4), 3, (1, 0)))
        self.enemy_board.place_ship(Ship(sprites.set_ship_texture0, (0,5), 4, (1, 0)))
        self.enemy_board.place_ship(Ship(sprites.set_ship_texture0, (0,6), 4, (1, 0)))
        self.enemy_board.place_ship(Ship(sprites.set_ship_texture0, (0,7), 5, (1, 0)))
        #test hit
        self.player_board.shoot_at((0,1))
        self.enemy_board.shoot_at((0,1))
        self.enemy_board.shoot_at((1,1))

    def update(self, delta_time):
        super().update(delta_time)
    
    
    def draw(self):

        config.window.blit(sprites.img_battlescreen_foreground, (0,0))

        # draw player's ships health squares bottom left
        for y in range(len(self.player_board.ships)):
            ship = self.player_board.ships[y]
            for x in range (ship.length):
                if ship.hit_parts[x]: #träffad
                    pygame.draw.rect(config.window,(255,0,0),(5+25*x,535+(20*y),20,10)) #x,y
                else: #ej träffad
                    pygame.draw.rect(config.window,(0,255,0),(5+25*x,535+(20*y),20,10))

        self.draw_enemy()
        super().draw()

    def draw_enemy(self):
        num_hits = 0
        # draw enemy's ships health squares bottom left
        for y in range(len(self.enemy_board.ships)):
            ship = self.enemy_board.ships[y]
            for x in range (ship.length):
                pygame.draw.rect(config.window,(0,255,0),(995-(25*x),535+(20*y),20,10))
                if all(ship.hit_parts): #only draw's red rectangles if whole ship is sunk
                    pygame.draw.rect(config.window,(255,0,0),(995-(25*x),535+(20*y),20,10)) #x,y
                
>>>>>>> battle_screen_health
