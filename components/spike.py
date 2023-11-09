import pygame as pg

class Spike(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # size = 30 # Taille par défaut

        # Définir la couleur du triangle (par exemple, rouge)
        # self.color = (255, 0, 0)

        # # Créer la surface pour le triangle
        # self.image = pg.Surface((size, size))
        # self.image.fill((0, 0, 0, 0))  # Remplit la surface avec une couleur transparente
        # self.image.set_colorkey((0, 0, 0))  # Définit la couleur transparente

        # # Coordonnées des sommets du triangle
        # p1 = (size // 2, 0)
        # p2 = (0, size)
        # p3 = (size, size)

        # # Dessiner le triangle sur la surface
        # pg.draw.polygon(self.image, self.color, [p1, p2, p3])

        # Créer une image pour le triangle
        self.image = pg.image.load("ressources/images/malus/pencil.png")

        # Obtenir le rectangle englobant le triangle
        self.rect = self.image.get_rect()

        self.pos = pg.math.Vector2(pos)
        # Positionner le rectangle aux coordonnées spécifiées (x, y)
        self.rect.bottomleft = self.pos

    def update(self, dt, speed):
        self.pos.x -= speed * dt
        self.rect.bottomleft = self.pos