import pygame as pg

class Book(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        size = 25

        self.image = pg.image.load("images/bonus/books.png")
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2((x, y))
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.midbottom = self.pos

    def update(self, dt, speed):
        self.pos.x -= speed * dt
        self.rect.midbottom = self.pos