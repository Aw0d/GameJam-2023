import random
import pygame as pg

class Background(pg.sprite.Sprite):
    background_img = [pg.image.load("images/background1.png"), pg.image.load("images/background2.png"),
                      pg.image.load("images/background3.png"), pg.image.load("images/background4.png")]
    
    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.image = Background.background_img[0]
        self.image2 = Background.background_img[1]
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2((0, 0))
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.topleft = self.pos
 
    def update(self, dt, speed):
        self.pos.x = self.pos.x - speed * dt
        if self.pos.x < -self.image.get_width():
            self.pos.x = 0
            self.image = self.image2
            self.rect = self.image.get_rect()
            self.image2 = Background.background_img[random.randint(0, 3)]

        self.rect.topleft = self.pos

    def draw(self, screen : pg.Surface):
        screen.blit(self.image, (self.pos.x, 0))
        screen.blit(self.image2, (self.pos.x + self.image.get_width(), 0))
