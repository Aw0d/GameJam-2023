import pygame as pg

class Ground(pg.sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()

        self.size = size

        self.image = pg.Surface(size)
        self.rect = self.image.get_rect()
        
        self.tile_image = pg.image.load("images/ground1.png")
        self.tile_size = self.tile_image.get_size()

        self.pos = pg.math.Vector2(pos)
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.bottomleft = self.pos

        for x in range(0, self.size[0], self.tile_size[0]):
            for y in range(0, self.size[1], self.tile_size[1]):
                self.image.blit(self.tile_image, (x, y))

    def update(self, dt, speed):
        self.pos.x = self.pos.x - speed * dt
        self.rect.bottomleft = self.pos


        
