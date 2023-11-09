import pygame as pg
import random

# Classe pour les particules
class Particle(pg.sprite.Sprite):
    imgs_particles = [pg.image.load("images/particles/particles1.png"), pg.image.load("images/particles/particles2.png"),
                      pg.image.load("images/particles/particles3.png"), pg.image.load("images/particles/particles4.png")]

    def __init__(self, pos):
        super().__init__()

        self.image = Particle.imgs_particles[random.randint(0, len(Particle.imgs_particles) - 1)]
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(pos)
        self.vel_x = random.uniform(-4, 0)
        self.vel_y = random.uniform(-1, 0)
        self.lifespan = 30  # Nombre de frames que la particule reste à l'écran

        self.rect.center = self.pos

    def update(self):
        self.pos.x += self.vel_x
        self.pos.y += self.vel_y
        self.rect.center = self.pos
        self.lifespan -= 1
        if self.lifespan > 0:
            self.image.set_alpha(255 * 30 / self.lifespan)
        else:
            self.image.set_alpha(0)