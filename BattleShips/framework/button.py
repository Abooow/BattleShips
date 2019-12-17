''' This module contains the Button class
'''

import pygame
import config
import surface_change


class Button():
    ''' The base class for a button


    example:
        def load_content(self):
            ...
            test_btn = Button(rect=(100, 100, 100, 50), bg=(100, 0, 220), action=test_btn_clicked)

            self.buttons.append(test_btn)  <- !! the button must be appended to self.buttons in order to update and draw the button correctly


        def test_btn_clicked(self):
            print('Hello World!')


    This example will create a button at position: (100, 100) and a size of: (100, 50),
    the background color will be purple and when the button is pressed it will print out 'Hello World!' to the console
    '''


    def __init__ (self, rect, bg=(255, 255, 255), hc=(100, 100, 100), image=None,  action=None):
        '''
        :param rect (tuple[int,int,int,int]): (x, y, width, height) position and size of the button
        :param bg (tuple[int,int,int]): (red, green, blue) (highlight color) color of the background (use None to remove bg)
        :param hc (tuple[int,int,int]): (red, green, blue) color filter for the image when hovering
        :param image (surface): a image to the button
        :param action (function): the function to instantiate when the button is clicked
        '''

        self.rect = rect
        self.bg = bg
        self.hc = hc
        self.image = image
        self.action = action

        self.active = True
        self.visible = True
        

    def on_click(self) -> None:
        ''' This method is called when the mouse is clicked
        note: this method does NOT check if the mouse is clicked, only call this method after mouse pressed event
        
        :returns: NoReturn
        :rtype: None
        '''

        if self.active and self.action != None and self._is_hovering():
            # instantiate the function associated with the button
            self.action()


    def draw(self) -> None:
        ''' Draw the button
        
        :returns: NoReturn
        :rtype: None
        '''

        # draw only plain color if image is None
        if self.image == None:

            # draw hovering color when hovering
            if self.bg and self._is_hovering():
                self._draw_hovering()
            else:
                pygame.draw.rect(config.window, self.bg, self.rect)
        else:
            # draw image it's not None

            # draw hovering color when hovering
            if self.bg and self._is_hovering():
                self._draw_hovering()

            # centers the image inside the button 
            size = self.image.get_rect().size
            x = (self.rect[0] + self.rect[2] * 0.5) - size[0] * 0.5
            y = (self.rect[1] + self.rect[3] * 0.5) - size[1] * 0.5
            img = surface_change.colorize(self.image, self.hc) if self._is_hovering() else self.image
            config.window.blit(img, (x, y))


    def _draw_hovering(self) -> None:
        ''' Draws the button but with a darker background (35% darker)

        :returns: NoReturn
        :rtype: None
        '''

        if self.bg == None:
            return

        bg = (self.bg[0] * 0.65, self.bg[1] * 0.65, self.bg[2] * 0.65)
        pygame.draw.rect(config.window, bg, self.rect)


    def _is_hovering(self) -> bool:
        ''' Determines if the mouse is hovering over the button
        
        :returns: True is the mouse is hovering the button
        :rtype: bool
        '''

        mouse = pygame.mouse.get_pos()
        return (self.rect[0] + self.rect[2] > mouse[0] > self.rect[0] and
                self.rect[1] + self.rect[3] > mouse[1] > self.rect[1])