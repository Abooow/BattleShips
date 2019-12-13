import pygame
import pic_module
import config

from framework.animation import Animation


class Jet(Animation):
    def __init__(self, position, velocity, fps=14, scale=1, rotation=0):
        super().__init__(pic_module.jet_anim, fps, scale, rotation, True)

        self.position = position
        self.velocity = velocity

        self.missiles = []


    def update(self, delta_time):
        super().update(delta_time)

        self.x += 8
        #if self.x >= 1124:
            #self.x = -200

        for missile in self.missiles:
            missile.update(delta_time)
                #self.missiles.remove(missile)

        if 1024 > self.x > 0 and random.random() < 0.05:
            self._drop_bomb()


    def draw(self):
        super().draw((self.x, self.y))

        for missile in self.missiles:
            missile.draw()


    def drop_bomb(self):
        self.missiles.append(Missile(self.x, self.y))


class Missile(Animation):
    def __init__(self, x, y, fps = 12):
        super().__init__(pic_module.missile_anim, fps, True)

        self.x = x
        self.y = y
        self.max_y = 550 - random.random() * 100
        self._explode = False
        self._explodsion_anim = Animation(pic_module.explosion_anim, 12, 1, 0, False)
        self._fire_anim = Animation(pic_module.fire_anim, 12, 3, 0, True)


    def update(self, delta_time):
        if not self._explode:
            super().update(delta_time)
            self.y += 5

            if self.y >= self.max_y:
                self._explode = True
        else:
            if self._explodsion_anim.done:
                self._fire_anim.update(delta_time)
            else:
                self._explodsion_anim.update(delta_time)


    def draw(self):
        if not self._explode:
            super().draw((self.x, self.y))
        else:
            if self._explodsion_anim.done:
                self._fire_anim.draw((self.x - 90, self.y - 50))
            else:
                self._explodsion_anim.draw((self.x - 70, self.y - 50))