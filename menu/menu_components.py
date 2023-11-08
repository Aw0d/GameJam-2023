import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, x , y, image, func):
        super().__init__()
        #self.image = pg.Surface((100, 50))
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #on enregistre l'Etat du button(True si il est clicked, FALSE sinon)
        self.state = False
        self.func = func

class Text(pg.sprite.Sprite):
    def __init__(self, x , y, image):
        super().__init__()
        #self.image = pg.Surface((100, 50))
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)