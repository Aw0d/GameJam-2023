import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = pg.Surface((20, 20))
        self.rect = self.image.get_rect()
        # Donne une couleur
        self.image.fill("blue")
