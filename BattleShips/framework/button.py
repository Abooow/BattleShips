class Buttons():
    def __init__ (self,canvas,position,size,colorr,action = None):
        self.position = position
        self.size = size
        self.colorr = colorr
        self.action = action
        self.canvas = canvas
        

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        

        if click[0] == 1 and action != None:
            action()


    def draw(self):
        #if(self.position[0]+self.size[0]> mouse[0] < self.position[0] and self.position[1]+self.size[1] > mouse[1] > self.position[1]):

        pygame.draw.rect(config.window, colorr, (self.position[0],self.position[1],self.size[0],self.size[1]))