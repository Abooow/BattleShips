''' This module contains the Cell class
'''

import pygame
import config
import sprites

from framework.animation import Animation
from framework.ship import Ship


class Cell:
    ''' Base class for a cell
    
    A Cell contains a part of a ship or it's empty, can contain a mine as well (SPRINT 3)
    this class is meant to be used together with the Board class


    example of a placed ship:
        image_set = [U, #, ^]

        ^  <- prow  | image_index = 2 | ship_part = 3
        #  <- deck  | image_index = 1 | ship_part = 2
        #  <- deck  | image_index = 1 | ship_part = 1
        U  <- stern | image_index = 0 | ship_part = 0
    '''


    def __init__(self, ship = None, image_index = 0, ship_part = 0, rotation = 0):
        '''
        :param ship (Ship): the reference to the ship that stands on this cell
        :param image_index (int): index for the image to use in the ship.image_set
        :param ship_part (int): what part of the ship is on this cell (0 is the part furthest back of the ship (the stern))
        :param rotation (int): the rotation of the ship image
        '''

        self.ship = ship
        self.image_index = image_index
        self.ship_part = ship_part
        self.rotation = rotation

        self.hit = False

        self._fire_anim = Animation(sprites.anim_fire, 12)
        self._explotion_anim = Animation(sprites.anim_explosion, 12, loop=False)


    def shoot_at(self) -> bool:
        ''' Shoot at this cell

        :returns: the ship placed on this cell if there is one otherwise None
        :rtype: Ship
        '''

        self.hit = True
        # the ship that was standing on this cell will take damage, if any
        if self.ship is not None:
            self.ship.get_hit(self.ship_part)
            return True
        else:
            return False


    def update(self, delta_time) -> None:
        ''' Updates all animation in this cell, if any

        :param delta_time (int): the time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        # no need to update any animation if the cell doesn't contain a ship or if the cell have not been shot at
        if self.ship == None or not self.hit:
            return
        elif self.hit:
            # TODO: fix animations, when hit, start explosion animation and fire animation
            pass


    def draw(self, position) -> None:
        ''' Draws everything that's in this cell

        :param position (tuple[int,int]): where to draw the Cell

        :returns: NoReturn
        :rtype: None
        '''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(sprites.img_cell, (x, y))

        # draw ship img
        if self.ship != None:
            # TODO: if the ship is hit, draw a destroyed sprite instead
            img = pygame.transform.rotate(self.ship.image_set[self.image_index], self.rotation)
            config.window.blit(img, (x, y))

        # TODO: draw explosion and fire animation if hit


    def draw_enemy(self, position) -> None:
        ''' Draws hit/miss but not the ship

        :param position (tuple[int,int]): where to draw the Cell

        :returns: NoReturn
        :rtype: None
        '''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(sprites.img_cell.board_cell, (x, y))

        # draw hitmarker after shot
        if self.hit:
            # TODO: if the ship is hit draw a destroyed sprite
            if self.ship != None:
                config.window.blit(hitImg, (x, y))
            elif self.ship == None:
                config.window.blit(missImg, (x, y))
                
        # TODO: draw explosion and fire animation if hit