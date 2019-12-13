
import pygame
import config
import pic_module


class Cell:
    def __init__(self, ship = None, image_set = None, image_index = 0, rotation = 0):
        '''
        param ship(Ship): the reference to the ship 
        param image_set(list[Surface]): a list of ship parts (images)
        param image_index(int): the index to use from image_set
        param rotation(int): the rotation of the ship image
        '''

        self.ship = ship
        self.ship_image = ship_image
        self.ship_rotation = rotation
        self.ship_part = ship_part

        self.hit = False

        self._fire_anim = None
        self._explotion_anim = None

        #self.mine = False SPRINT3


    def fire_at(self) -> None:
        '''

        returns: nothing
        rtype: None
        '''

        pass


    def update(self, delta_time) -> None:
        '''

        param delta_time(int): the time since last frame

        returns: nothing
        rtype: None
        '''

        pass


    def draw(self, position) -> None:
        ''' 

        param position(tuple[int,int]): where to draw the Cell

        returns: nothing
        rtype: None
        '''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(pic_module.board_cell, (x,y))

        # draw ship img
        if self.ship != None: 
            img = pygame.transform.rotate(self.ship_image, self.ship_rotation)
            config.window.blit(img, (x,y))


    def draw_enemy(self, position) -> None:
        ''' 

        param position(tuple[int,int]): where to draw the Cell

        returns: nothing
        rtype: None
        '''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(pic_module.board_cell, (x,y))

        # draw hitmarker after shot
        if self.hit == True and self.ship != None: 
            config.window.blit(hitImg, (x,y))
        elif self.hit == True and self.ship == None:
            config.window.blit(missImg, (x,y))


    # draw placed mine SPRINT3
    #if self.mine != None: 
    #    config.window.blit(mineImg, (x,y))
    