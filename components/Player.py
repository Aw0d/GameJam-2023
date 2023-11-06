import pygame as pg

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):

    def __init__(self, all_objects):
        super().__init__()
        self.image = pg.Surface((20, 60))
        self.rect = self.image.get_rect()
        # Donne une couleur
        self.image.fill("blue")

        self.all_objects = all_objects

        # Position
        self.pos = vec((200, 600))
        self.vel_y = 0
        self.acc_y = 0.5

        self.jumping = False
        self.sliding = False
        self.slide_timer = 0  # Initialisation du compteur de glissade

    def update(self, *args):
        self.move()

        if self.sliding:
            # Compteur pour la durée de la glissade
            self.slide_timer += 1
            if self.slide_timer >= 60:  # Réduisez ce nombre selon la durée de la glissade souhaitée (60 correspond à une seconde)
                # Rétablir la hauteur normale du personnage
                self.image = pg.Surface((20, 60))
                self.image.fill("blue")
                self.rect = self.image.get_rect()
                self.sliding = False
                self.slide_timer = 0
                self.rect.midbottom = self.pos

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
      hits = pg.sprite.spritecollide(self, self.all_objects, False)
      print(hits)
      if self.vel_y > 0:
          if hits:
                lowest = hits[0]
                if self.pos.y - self.vel_y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel_y = 0
                    self.jumping = False

    def jump(self):
        # Check to see if payer is in contact with the ground
        hits = pg.sprite.spritecollide(self, self.all_objects, False)
            
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.jumping = True
            self.vel_y = -12
    
    def slide(self):
        if not self.sliding:
            # Réduire la hauteur du personnage
            self.image = pg.Surface((20, 30))  # Nouvelle surface avec une hauteur réduite
            self.image.fill("blue")
            self.rect = self.image.get_rect()
            self.sliding = True