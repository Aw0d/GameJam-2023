import pygame as pg
from random import randint

class Bonus(pg.sprite.Sprite):
    imgs_bonus = [pg.image.load("images/bonus/books.png"), pg.image.load("images/bonus/lesson.png")]

    def __init__(self, pos):
        super().__init__()

        self.image = Bonus.imgs_bonus[randint(0, len(Bonus.imgs_bonus) - 1)]
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(pos)
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.bottomleft = self.pos

    def update(self, dt, speed):
        self.pos.x -= speed * dt
        self.rect.bottomleft = self.pos