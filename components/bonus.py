import pygame as pg
from random import randint

class Bonus(pg.sprite.Sprite):
    imgs_bonus = [pg.image.load("images/bonus/books.png"), pg.image.load("images/bonus/lesson.png")]

    def __init__(self, pos):
        super().__init__()

        self.original_image = Bonus.imgs_bonus[randint(0, len(Bonus.imgs_bonus) - 1)]
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(pos)
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.bottomleft = self.pos

        self.zoom = 0.9
        self.zoom_speed = 0.005
        self.max_zoom = 1
        self.min_zoom = 0.8
        self.zoom_direction = 1

    def update(self, dt, speed):
        self.pos.x -= speed * dt
        self.rect.bottomleft = self.pos

        self.zoom += self.zoom_speed * self.zoom_direction
        if self.zoom >= self.max_zoom or self.zoom <= self.min_zoom:
            self.zoom_direction *= -1
        
        # Met à jour l'image et le rect
        self.image = pg.transform.rotozoom(self.original_image, 0, self.zoom)
        self.rect = self.image.get_rect(center=self.rect.center)