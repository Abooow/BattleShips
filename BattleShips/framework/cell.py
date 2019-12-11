import config
import pygame
class Cell:
    
    cellImg = pygame.image.load(r'content\sprites\Ruta.png')
    botImg = pygame.image.load(r'content\sprites\boat_bottom.png')
    midImg = pygame.image.load(r'content\sprites\boat_middle.png')
    topImg = pygame.image.load(r'content\sprites\boat_top.png')
    missImg = pygame.image.load(r'content\sprites\hitmarker.png')
    hitImg = pygame.image.load(r'content\sprites\hitmarker_red.png')

    def __init__(self, image = None, rotation = 0, ship= None):
        '''
        param None
        returns None'''

        self.ship_image = image
        self.ship_rotation = rotation
        self.ship = ship
        self.hit = False
        #self.mine = False SPRINT3

    def draw(self, position):
        '''
        param position tuple([int,int]):
        param rotation tuple([int,int]):
        param part string(bottom/middle/top):
        returns None'''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(Cell.cellImg, (x,y))

        # draw ship img
        if self.ship != None: 
            img = pygame.transform.rotate(self.ship_image, self.ship_rotation)
            config.window.blit(img, (x,y))


    def draw_enemy(self, position):
        '''
        param position tuple([int,int]):
        returns None'''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(cellImg, (x,y))

        # draw hitmarker after shot
        if self.hit == True and self.ship != None: 
            config.window.blit(hitImg, (x,y))
        elif self.hit == True and self.ship == None:
            config.window.blit(missImg, (x,y))

        # draw placed mine SPRINT3
        #if self.mine != None: 
        #    config.window.blit(mineImg, (x,y))
    