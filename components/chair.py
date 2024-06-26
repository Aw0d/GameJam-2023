import pygame as pg

class Chair(pg.sprite.Sprite):
    img_chair = pg.image.load("ressources/images/background/chair.png")
    def __init__(self, pos):
        super().__init__()

        self.image = Chair.img_chair
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(pos)
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.bottomleft = self.pos

    def update(self, dt, speed):
        self.pos.x -= speed * dt
        self.rect.bottomleft = self.pos