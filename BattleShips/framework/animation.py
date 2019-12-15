''' This module contains the Animation class
'''

import pygame
import config
import surface_change


class Animation():
    ''' The base class for an animation, this class can either be instantiated directly or inherited
    
    The Animation class uses a list of images as frames and changes what frame to draw after some time


    how to use, example 1:

        def load_content(self):
            ...
            anim = Animation(...)

        def update(self, delta_time):
            ...
            anim.update(delta_time)

        def draw(self):
            ...
            anim.draw(...)


    how to use, example 2:
        class Missile(Animation):
            def __init__(self, ...):
                super().__init__(...)

            def update(self, delta_time):
                super().update(delta_time)

            def draw(self):
                super().draw(...)


    To update the animation: call the update method, otherwise the animation won't animate
    To display/draw the animation: call the draw method, otherwise the animation won't be shown
    '''


    def __init__(self, frames, fps, loop = True, offset = 0):
        '''
        :param frames (list[surface]): all the frames to be used
        :param fps (int): the animation speed (frames per second)
        :param loop (bool): allow the animation to loop
        :param offset (int): what frame to start animate from
        '''

        self.frames = frames
        self.fps = fps
        self.loop = loop
        self.done = False

        self._frame = offset % len(frames)
        self._timer = 0

        
    def update(self, delta_time) -> None:
        ''' Updates the animation

        :param delta_time (int): time since last frame

        :returns: NoReturn
        :rtype: None
        '''

        # only update if the animation isn't finished
        if not self.done:
            # update the timer
            self._timer += delta_time

            # change frame when time is right
            if self._timer >= 1000 / self.fps:
                self._timer = 0
                self._frame += 1

                # restart the animation to frame 0 if loop is True, otherwise mark the animation as done
                if self._frame >= len(self.frames):
                    if self.loop:
                        self._frame = 0
                    else:
                        self.done = True


    def draw(self, position) -> None:
        ''' Draws the animation

        :param position (tuple[int,int]): the position to draw the animation

        :returns: NoReturn
        :rtype: None
        '''

        if len(self.frames) > 0:
            config.window.blit(self.frames[self._frame], position)