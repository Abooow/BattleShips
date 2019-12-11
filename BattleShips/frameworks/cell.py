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

        self.ship = None
        self.hit = False

    def draw(self, position, rotation, part):
        '''
        param position tuple([int,int]):
        param rotation tuple([int,int]):
        param part string(bottom/middle/top):
        returns None'''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        window.blit(cellImg, (x,y))

        # set rotate value for ship img
        if self.ship != None:
            if rotation == (-1, 0): dir = -90 #LEFT
            elif rotation == (1, 0): dir = 90 #RIGHT
            elif rotation == (0, 1): dir = 180 #DOWN
            else: dir = 0 #UP

        # draw ship img
        if self.ship != None and part == 'bottom': 
            botImg = pygame.transform.rotate(botImg, dir)
            window.blit(botImg, (x,y))
        elif self.ship != None and part == 'middle':
            midImg = pygame.transform.rotate(midImg, dir)
            window.blit(midImg, (x,y))
        elif self.ship != None and part == 'top':
            topImg = pygame.transform.rotate(topImg, dir)
            window.blit(topImg, (x,y))

    def draw_enemy(self, position):
        '''
        param position tuple([int,int]):
        returns None'''

        x = position[0]
        y = position[1]

        # draw cell boarder img 50x50
        window.blit(cellImg, (x,y))

        # draw hitmarker after shot
        if self.hit == True and self.ship != None: 
            window.blit(hitImg, (x,y))
        elif self.hit == True and self.ship == None:
            window.blit(missImg, (x,y))

    