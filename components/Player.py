import pygame as pg

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):

    def __init__(self, ground_group):
        super().__init__()
        self.image = pg.Surface((20, 60))
        self.rect = self.image.get_rect()
        # Donne une couleur
        self.image.fill("blue")

        self.ground_group = ground_group

        # Position
        self.pos = vec((200, 600))
        self.vel_y = 0
        self.acc_y = 0.5

        self.jumping = False
        self.sliding = False

    def move(self):
        # Récupération des touches appuyées
        pressed_keys = pg.key.get_pressed()

        if pressed_keys[pg.K_UP]:
            self.jump()
        if pressed_keys[pg.K_DOWN]:
            self.slide()

        # Application de la gravité
        self.vel_y += self.acc_y
        self.pos.y += self.vel_y + 0.5 * self.acc_y  # Updates Position with new values

        # Vérification de la colision avec le sol
        self.ground_colision()

        # Mise à jour de la position
        self.rect.midbottom = self.pos

    def ground_colision(self):
      hits = pg.sprite.spritecollide(self, self.ground_group, False)
      if self.vel_y > 0:
          if hits:
              lowest = hits[0]
              if self.pos.y < lowest.rect.bottom:
                  self.pos.y = lowest.rect.top + 1
                  self.vel_y = 0
                  self.jumping = False

    def jump(self):
        # Check to see if payer is in contact with the ground
        hits = pg.sprite.spritecollide(self, self.ground_group, False)
            
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.jumping = True
            self.vel_y = -12
    
    def slide(self):
        if not self.sliding:
            pass