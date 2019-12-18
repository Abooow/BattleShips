''' This module contains the Cell class
'''

import pygame
import config
import sprites
import surface_change
import framework.animations as animations

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

        self._fire_anim = animations.Fire()
        self._explotion_anim = animations.Explosion()
        self._water_splash_anim = None


    def shoot_at(self) -> bool:
        ''' Shoot at this cell

        :returns: the ship placed on this cell if there is one otherwise None
        :rtype: Ship
        '''

        self.hit = True
        # the ship that was standing on this cell will take damage, if any
        if self.ship is not None:
            self.ship.hit(self.ship_part)
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
        if self.hit:
            # explosion animation
            if self.ship is not None:
                # update explosion
                if not self._explotion_anim.done:
                    self._explotion_anim.update(delta_time)

                # update fire
                self._fire_anim.update(delta_time)

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

        # TODO: draw explosion and fire animation if hit
        if self.ship != None: # if it's a cell on this cell
            img = pygame.transform.rotate(self.ship.image_set[self.image_index], self.rotation)

            # draw ship image
            if self.hit: # hit, draw the ship part red
                config.window.blit(surface_change.colorize(img, (150, 0, 0)), (x, y))
            else: # not hit, draw the ship part normally
                config.window.blit(img, (x, y))
        elif self.hit: # not a ship part, draw miss marker if hit
            config.window.blit(sprites.img_missmarker, (x+1, y+1))

        self._draw_animations(position)


    def draw_enemy(self, position) -> None:
        ''' Draws hit/miss but not the ship

        :param position (tuple[int,int]): where to draw the Cell

        :returns: NoReturn
        :rtype: None
        '''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(sprites.img_cell, (x, y))

        # draw hitmarker after shot
        if self.hit:
            # TODO: if the ship is hit draw a destroyed sprite
            if self.ship != None: # Hit
                config.window.blit(sprites.img_hitmarker, (x+1, y+1))
                #pygame.draw.rect(config.window, (0, 100, 70), (x+1, y+1, 40, 40))
            elif self.ship == None: # Miss
                config.window.blit(sprites.img_missmarker, (x+1, y+1))
                #pygame.draw.rect(config.window, (100, 30, 30), (x+1, y+1, 40, 40))
                
        self._draw_animations(position)


    def _draw_animations(self, position):
        x = position[0]
        y = position[1]

        if self.hit:
            if self.ship is not None:
                # fire anim
                self._fire_anim.draw((x - 30, y - 30))
                self._fire_anim.draw((x - 20, y - 20))

                 # explosion anim
                if not self._explotion_anim.done:
                    self._explotion_anim.draw((x - 100, y - 100))