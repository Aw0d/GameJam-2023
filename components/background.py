import random
import pygame as pg

class Background(pg.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        i = random.randint(1, 3)
        self.image = pg.image.load(f"images/background{i}.png")
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2((screen_size[0], 0))
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.topright = self.pos
 
    def update(self, dt, speed):
        self.pos.x = self.pos.x - speed * dt
        if self.pos.x < 0:
            self.pos.x = self.screen_size[0]
        self.rect.topright = self.pos

    def draw(self, screen : pg.Surface):
        x = self.pos.x
        while x < screen.get_size()[0] + self.rect.width :
            screen.blit(self.image, (x, 0))
            x += self.rect.width
