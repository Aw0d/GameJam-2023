import pygame as pg

class Ground(pg.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.image = pg.image.load("images/ground.png")
        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width * 2

        self.pos = pg.math.Vector2((0, screen_size[1]))
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.bottomleft = self.pos

    def update(self, dt, speed):
        self.pos.x = self.pos.x - speed * dt
        if self.pos.x < -self.image.get_width():
            self.pos.x = 0
        self.rect.bottomleft = self.pos

    def draw(self, screen : pg.Surface):
        screen.blit(self.image, (self.pos.x, self.rect.top))
        screen.blit(self.image, (self.pos.x + self.image.get_width(), self.rect.top))
