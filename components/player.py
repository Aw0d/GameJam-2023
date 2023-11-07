import pygame as pg

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    run_ani = [pg.image.load("images/characters/player/run1.png"), pg.image.load("images/characters/player/run2.png"),
                pg.image.load("images/characters/player/run3.png"), pg.image.load("images/characters/player/run4.png"),
                pg.image.load("images/characters/player/run5.png"),]
    
    jump_ani = [pg.image.load("images/characters/player/saut1.png"), pg.image.load("images/characters/player/saut2.png")]

    slide_ani = [pg.image.load("images/characters/player/slide1.png"), pg.image.load("images/characters/player/slide2.png")]

    def __init__(self):
        super().__init__()
        self.image = Player.run_ani[0]
        self.rect = self.image.get_rect()
        # Donne une couleur
        #self.image.fill("blue")


        # Position
        self.pos = vec((200, 200))
        self.vel_y = 0
        self.acc_y = 0.09

        self.frame = 0
        self.jumping = False
        self.sliding = False
        self.slide_timer = 0  # Initialisation du compteur de glissade
        self.move_frame = 0

    def _update(self,dt, hits):
        if self.sliding:
            # Compteur pour la durée de la glissade
            self.slide_timer += dt
            if self.slide_timer >= 500:  # Réduisez ce nombre selon la durée de la glissade souhaitée
                # Rétablir la hauteur normale du personnage
                self.sliding = False
                self.slide_timer = 0

        self.frame += 1

        if self.frame % 5 == 0:
            if not self.jumping and not self.sliding:
                self.image = Player.run_ani[self.move_frame]
                self.move_frame = (self.move_frame + 1) % (len(Player.run_ani)-1)
            elif self.jumping and not self.sliding:
                self.image = Player.jump_ani[self.move_frame]
                self.move_frame = 1
            else:
                self.image = Player.slide_ani[self.move_frame]
                self.move_frame = 1
            self.rect = self.image.get_rect()

        self.move(dt, hits)

    def move(self,dt, hits):
        # Application de la gravité
        self.vel_y += self.acc_y
        vel_max = 20
        self.pos.y += min(self.vel_y * dt, vel_max) # Updates Position with new values
            
        # Vérification de la colision avec le sol
        self.ground_colision(hits)

        # Mise à jour de la position
        self.rect.midbottom = self.pos

    def ground_colision(self, hits):
      if self.vel_y > 0:
        i = 0
        while i < len(hits) and (type(hits[i]).__name__ in ["Book"]):
            i += 1
        if i < len(hits) :

            lowest = hits[i]
            if self.rect.bottom > lowest.rect.top - 1 and self.rect.bottom < lowest.rect.bottom:
                self.pos.y = lowest.rect.top + 1
                self.vel_y = 0
                self.jumping = False

    def jump(self, hits):
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.jumping = True
            self.move_frame = 0
            self.vel_y = -1.1
    
    def slide(self):
        if not self.sliding:
            self.sliding = True
            self.move_frame = 0