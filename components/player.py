import pygame as pg

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 60))
        self.rect = self.image.get_rect()
        # Donne une couleur
        self.image.fill("blue")

        # Position
        self.pos = vec((200, 600))
        self.vel_y = 0
        self.acc_y = 0.12
        self.jumping = False
        self.sliding = False
        self.slide_timer = 0  # Initialisation du compteur de glissade

    def _update(self,dt, hits):
        self.move(dt, hits)

        if self.sliding:
            # Compteur pour la durée de la glissade
            self.slide_timer += dt
            if self.slide_timer >= 500:  # Réduisez ce nombre selon la durée de la glissade souhaitée
                # Rétablir la hauteur normale du personnage
                self.image = pg.Surface((20, 60))
                self.image.fill("blue")
                self.rect = self.image.get_rect()
                self.sliding = False
                self.slide_timer = 0
                self.rect.midbottom = self.pos

    def move(self,dt, hits):
        # Application de la gravité
        self.vel_y += self.acc_y
        self.pos.y += self.vel_y * dt # Updates Position with new values
        # Vérification de la colision avec le sol
        self.ground_colision(hits)

        # Mise à jour de la position
        self.rect.midbottom = self.pos

    def ground_colision(self, hits):
      if self.vel_y > 0:
          if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel_y = 0
                    self.jumping = False

    def jump(self, hits):
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.jumping = True
            self.vel_y = -1.2
    
    def slide(self):
        if not self.sliding:
            # Réduire la hauteur du personnage
            self.image = pg.Surface((20, 30))  # Nouvelle surface avec une hauteur réduite
            self.image.fill("blue")
            self.rect = self.image.get_rect()
            self.sliding = True