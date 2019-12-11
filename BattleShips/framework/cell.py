import config
class Cell:
    
    cellImg = pygame.image.load(r'content\sprites\Ruta.png')
    botImg = pygame.image.load(r'content\sprites\boat_bottom.png')
    midImg = pygame.image.load(r'content\sprites\boat_middle.png')
    topImg = pygame.image.load(r'content\sprites\boat_top.png')
    missImg = pygame.image.load(r'content\sprites\hitmarker.png')
    hitImg = pygmae.image.load(r'content\sprites\hitmarker_red.png')

    def __init__(self):
        '''
        param None
        returns None'''

        self.ship_image = None
        self.ship = None
        self.hit = False
        #self.mine = False SPRINT3

    def draw(self, position):
        '''
        param position tuple([int,int]):
        param rotation tuple([int,int]):
        param part string(bottom/middle/top):
        returns None'''
        position = (5,5)

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        config.window.blit(cellImg, (x,y))

        # draw ship img
        if self.ship != None: 
            config.window.blit(self.ship_image, (x,y))


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
    