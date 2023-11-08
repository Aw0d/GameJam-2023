import pygame as pg

class Table(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.image.load("images/background/table.png")
        self.rect = self.image.get_rect()
        # Donne une couleur
        # self.image.fill("brown")

        self.pos = pg.math.Vector2((x, y))
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.midbottom = self.pos

    def update(self, dt, speed):
        self.pos.x -= speed * dt
        self.rect.midbottom = self.pos