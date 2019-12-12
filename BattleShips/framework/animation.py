
import config


class Animation():
    def __init__(self, frames, fps, loop = True):
        self.frames = frames
        self.fps = fps
        self.loop = loop
        self.done = False

        self._frame = 0
        self._timer = 0


    def update(self, delta_time):
        if not self.done:
            self._timer += delta_time

            if self._timer >= 1000 / self.fps:
                self._timer = 0
                self._frame += 1

                if self._frame >= len(self.frames):
                    if self.loop:
                        self._frame = 0
                    else:
                        self.done = True


    def draw(self, position):
        if len(self.frames) > 0:
            config.window.blit(self.frames[self._frame], position)