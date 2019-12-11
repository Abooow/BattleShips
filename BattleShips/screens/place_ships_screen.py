# The screen for place ships,
# everything that have to do with PlaceShips state should be in in here


from screens import screen
import pygame
import config
import random


class PlaceShipScreen(screen.Screen):
    def __init__(self):
        super().__init__()


    def load_content(self):
        self.image = pygame.image.load(r'content\sprites\placeYourShips.png')
        self.amount = 50
        self.xy = []
        self.creat_rain()
        super().load_content()
        

    def creat_rain(self):

        for i in range(self.amount):
            x = random.randint(0,config.SCREEN_WIDTH)
            y = random.randint(0,config.SCREEN_HEIGHT)
            speed = random.randint(10,20)
            self.xy.append((x,y,speed))

    def update(self, delta_time):
        for i in range(self.amount):
            if (self.xy[i][1] > config.SCREEN_HEIGHT):
                x = random.randint(0,config.SCREEN_WIDTH)
                self.xy[i] = (x, -100, self.xy[i][2])
            self.xy[i] = (self.xy[i][0], self.xy[i][1]  + self.xy[i][2], self.xy[i][2])

        super().update(delta_time)


    def draw(self):
        for i in self.xy:
            green = (i[2], 255-i[2]*1.5, 72-i[2])
            pygame.draw.rect(config.window, green, (i[0],i[1],10,100))

        config.window.blit(self.image, (config.SCREEN_WIDTH*0.5-self.image.get_rect().size[0]*0.5, config.SCREEN_HEIGHT*0.05))
        super().draw() 