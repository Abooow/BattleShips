import pygame
import config
import surface_change


class Animation():
    ''' The base class for an animation, this class can either be instantiated directly or inherited
    
    example 1:
        anim = Animation(...)

    example 2:
        class Missile(Animation):
            ...


    To update the animation: call the update method, otherwise the animation won't animate

    To display/draw the animation: call the draw method, otherwise the animation won't be shown
    '''


    def __init__(self, frames, fps, scale = (1, 1), rotation = 0, loop = True):
        '''
        :param frames (list[surface]): all the frames to be used
        :param fps (int): the animation speed (frames per second)
        :param scale (tuple[int,int]): the scale of each frame (width, height)
        :param rotation (int): the rotation of each frame
        :param loop (bool): allow the animation to loop
        '''

        self.fps = fps
        self.loop = loop
        self.done = False

        self._scale = scale
        self._rotation = rotation
        self._frame = 0
        self._timer = 0
        self._original_frames = frames

        self.change_transform(scale, rotation)


    def change_transform(self, scale = None, rotation = None) -> None:
        ''' Changes the transform of each frame in the animation

        :param scale (tuple[int,int]): the scale of each frame (width, height)
        :param rotation (int): the rotation of each frame
        
        :returns: nothing
        :rtype: None
        '''

        scale_ = self._scale if scale else scale
        rotation_ = self._rotation if rotation else rotation
        self.frames = [surface_change.transform(img, scale_, rotation_) for img in self._original_frames]

        
    def update(self, delta_time) -> None:
        ''' Used to update the animation

        :param delta_time (int): time since last frame

        :returns: nothing
        :rtype: None
        '''

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
        ''' Used to draw the animation

        :param position (tuple[int,int]): the position to draw the animation

        :returns: nothing
        :rtype: None
        '''

        if len(self.frames) > 0:
            config.window.blit(self.frames[self._frame], position)