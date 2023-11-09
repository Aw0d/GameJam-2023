import random
import pygame as pg

class Background(pg.sprite.Sprite):
    background_img = [pg.image.load("ressources/images/background/background1.png"), pg.image.load("ressources/images/background/background2.png"),
                      pg.image.load("ressources/images/background/background3.png"), pg.image.load("ressources/images/background/background4.png"),
                      pg.image.load("ressources/images/background/background5.png")]
    
    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.image = pg.image.load("ressources/images/background/first_background.png")
        self.image2 = pg.image.load("ressources/images/background/second_background.png")
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2((0, 0))
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.topleft = self.pos
 
    def update(self, dt, speed):
        self.pos.x = self.pos.x - speed* 0.8 * dt
        if self.pos.x < -self.image.get_width():
            self.pos.x = 0
            self.image = self.image2
            self.rect = self.image.get_rect()
            self.image2 = Background.background_img[random.randint(0, len(Background.background_img))-1]

        self.rect.topleft = self.pos

    def draw(self, screen : pg.Surface):
        screen.blit(self.image, (self.pos.x, 0))
        screen.blit(self.image2, (self.pos.x + self.image.get_width(), 0))
