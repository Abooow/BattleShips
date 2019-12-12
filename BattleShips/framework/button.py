import pygame
import config

class Button():
    def __init__ (self, rect, bg = (255, 255, 255), fg = (0, 0, 0), image = None,  action = None):
        '''

        param position(tuple[int,int]):

        '''

        self.rect = rect
        self.bg = bg
        self.fg = fg
        self.image = image
        self.action = action
        

    def update(self, obj):
        mouse = pygame.mouse.get_pos()
        
        if (self.action != None and
            self._is_hovering()):
            self.action(obj)


    def draw(self):
        if self.image == None:
            if self._is_hovering():
                bg = (self.bg[0] * 0.65, self.bg[1] * 0.65, self.bg[2] * 0.65)
                pygame.draw.rect(config.window, bg, self.rect)
            else:
                pygame.draw.rect(config.window, self.bg, self.rect)
        else:
            if self._is_hovering():
                bg = (self.bg[0] * 0.65, self.bg[1] * 0.65, self.bg[2] * 0.65)
                pygame.draw.rect(config.window, bg, self.rect)

            size = self.image.get_rect().size
            x = (self.rect[0] + self.rect[2] * 0.5) - size[0] * 0.5
            y = (self.rect[1] + self.rect[3] * 0.5) - size[1] * 0.5
            config.window.blit(self.image, (x, y))


    def _is_hovering(self):
        mouse = pygame.mouse.get_pos()
        return (self.rect[0] + self.rect[2] > mouse[0] > self.rect[0] and
                self.rect[1] + self.rect[3] > mouse[1] > self.rect[1])