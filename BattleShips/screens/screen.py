''' This module contains the Screen class
'''


import pygame
import config


class Screen():
    '''Base class for all screens, this class is ment to be inhereted

    A super class that is used for different screens


    How to use:
        class MenuScreen(Screen):
            def __init__(self):
                super().__init__()
                

            def load_content(self):
                super().load_content()


            def update(self, delta_time):
                super().update(delta_time)


            def draw(self):
                super().draw()
    '''


    def __init__(self):
        ''' The initialiazion for the screen
        '''

        # all buttons that belongs to the screen
        self.buttons = []

        # load_content() is called automatically after __init__()
        self.load_content()


    def load_content(self) -> None:
        ''' All content the are supposed to be loaded/initialized only once at the beginning are meant to belong in this method, this method is called once

        :returns: nothing
        :rtype: None
        '''
        
        pass


    def update(self, delta_time) -> list:
        ''' Every thing that are supposed to update every frame are meant to belong in this method, this method is called 60 FPS
        note: This method is called BEFORE the draw() method

        :returns: every events that occured
        :rtype: list[event]
        '''

        # save every event
        events = pygame.event.get()
        for event in events:

            # exit window when X button is clicked
            if event.type == pygame.QUIT:
                config.quit_game = True

            # call on_click() for each button when left mouse button was clicked (the method on_click() checks is the mouse was inside the button)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.buttons:
                    button.on_click()

        return events


    def draw(self) -> None:
        ''' Every thing that are supposed to be drawn are ment to belong in this method, this method is called 60 FPS
        note: This method is called AFTER the update() method

        :returns: nothing
        :rtype: None
        '''

        # draw every button
        for button in self.buttons:
            button.draw()