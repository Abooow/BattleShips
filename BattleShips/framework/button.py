import pygame
import config


class Button():
    ''' The base class for a button


    example:
        def load_content(self):
            ...
            test_btn = Button(rect=(100, 100, 100), bg=(100, 0, 220), action=test_btn_clicked)

            self.buttons.append(test_btn)  <- the button must be appended to self.buttons in order to update and draw the button correctly


        def test_btn_clicked(self):
            print('Hello World!')
    '''


    def __init__ (self, rect, bg = (255, 255, 255), fg = (0, 0, 0), image = None,  action = None):
        '''
        :param rect (tuple[int,int,int,int]): (x, y, width, height) position and size of the button
        :param bg (tuple[int,int,int]): (red, green, blue) color of the background (use None to remove bg)
        :param fg (tuple[int,int,int]): (red, green, blue) color of the foreground (use None to remove fg)
        :param image (surface): a image to the button
        :param action (function): the function to instantiate when the button is clicked
        '''

        self.rect = rect
        self.bg = bg
        self.fg = fg
        self.image = image
        self.action = action

        self.active = True
        self.visible = True
        

    def on_click(self) -> None:
        ''' This method is called when the mouse is clicked
        note: this method does NOT check if the mouse is clicked, only call this method after mouse pressed event
        
        :returns: nothing
        :rtype: None
        '''

        if self.active and self.action != None and self._is_hovering():
            # instantiate the function associated with the button
            self.action()


    def draw(self) -> None:
        ''' Draw the button
        
        :returns: nothing
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
            config.window.blit(self.image, (x, y))


    def _draw_hovering(self) -> None:
        ''' Draws 

        :returns: nothing
        :rtype: None
        '''

        bg = (self.bg[0] * 0.65, self.bg[1] * 0.65, self.bg[2] * 0.65)
        pygame.draw.rect(config.window, bg, self.rect)


    def _is_hovering(self) -> bool:
        '''
        
        :returns: True is the mouse is hovering the button
        :rtype: bool
        '''

        mouse = pygame.mouse.get_pos()
        return (self.rect[0] + self.rect[2] > mouse[0] > self.rect[0] and
                self.rect[1] + self.rect[3] > mouse[1] > self.rect[1])