import pygame as pg

class Ground(pg.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pg.Surface((1024, 80))
        self.rect = self.image.get_rect(center = (512, 728))
 
    def render(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))  