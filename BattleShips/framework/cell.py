
import pygame
import config
import pic_module

from framework.animation import Animation
from framework.ship import Ship


class Cell:
    ''' Base class for a cell
    

    '''


    def __init__(self, ship = None, image_index = 0, ship_part = 0, rotation = 0):
        '''
        :param ship (Ship): the reference to the ship 
        :param image_index (int): index for the image to use in the ship.image_set
        :param ship_part (int): what part of the this is on this cell (0 is the part furthest back (the stern))
        :param rotation (int): the rotation of the ship image
        '''

        self.ship = ship
        self.image_index = image_index
        self.ship_part = ship_part
        self.rotation = rotation

        self.hit = False

        self._fire_anim = Animation(pic_module.fire_anim, 12)
        self._explotion_anim = Animation(pic_module.explosion_anim, 12, loop=False)


    def shoot_at(self) -> bool:
        ''' Shoot at this cell

        :returns: the ship placed on this cell if there is one otherwise None
        :rtype: Ship
        '''

        self.hit = True
        if self.ship is not None:
            self.ship.get_hit()
            return True
        else:
            return False


    def update(self, delta_time) -> None:
        ''' Updates all animation in this cell if any

        :param delta_time (int): the time since last frame

        :returns: nothing
        :rtype: None
        '''

        # TODO: fix animations, when hit then start explosion and after start fire animation
        self._fire_anim.update(delta_time)


    def draw(self, position) -> None:
        ''' Draws everything on this cell

        :param position (tuple[int,int]): where to draw the Cell

        :returns: nothing
        :rtype: None
        '''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(pic_module.board_cell, (x, y))

        # draw ship img
        if self.ship != None: 
            img = pygame.transform.rotate(self.ship_image, self.ship_rotation)
            config.window.blit(img, (x, y))


    def draw_enemy(self, position) -> None:
        ''' Draws hit/miss but not the ship

        :param position (tuple[int,int]): where to draw the Cell

        :returns: nothing
        :rtype: None
        '''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(pic_module.board_cell, (x, y))

        # draw hitmarker after shot
        if self.hit:
            if self.ship != None:
                config.window.blit(hitImg, (x, y))
            elif self.ship == None:
                config.window.blit(missImg, (x, y))
    