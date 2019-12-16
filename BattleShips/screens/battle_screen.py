import pygame
import config
import sprites
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
                