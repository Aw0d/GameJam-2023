import pygame as pg
from random import randint

class Malus(pg.sprite.Sprite):
    imgs_malus = [pg.image.load("images/malus/clock.png"), pg.image.load("images/malus/alarm.png")]

    def __init__(self, pos):
        super().__init__()

        self.image = Malus.imgs_malus[randint(0, len(Malus.imgs_malus) - 1)]
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(pos)
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.bottomleft = self.pos

    def update(self, dt, speed):
        self.pos.x -= speed * dt
        self.rect.bottomleft = self.pos