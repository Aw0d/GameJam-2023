import pygame as pg
from random import randint

class Malus(pg.sprite.Sprite):
    imgs_malus = [pg.image.load("images/malus/clock.png"), pg.image.load("images/malus/alarm.png")]
    recolt_sound = pg.mixer.Sound("sounds/recolt-malus.mp3")

    def __init__(self, pos):
        super().__init__()

        self.original_image = Malus.imgs_malus[randint(0, len(Malus.imgs_malus) - 1)]
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

    def collect(self):
        self.channel = pg.mixer.Channel(4)
        self.channel.play(Malus.recolt_sound)