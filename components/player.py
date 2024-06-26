import pygame as pg
from components.bonus import Bonus
from components.malus import Malus
from components.spike import Spike
from components.chair import Chair
from components.particle import Particle


class Player(pg.sprite.Sprite):
    run_ani = [pg.image.load("ressources/images/characters/player/run1.png"), pg.image.load("ressources/images/characters/player/run2.png"),
                pg.image.load("ressources/images/characters/player/run3.png"), pg.image.load("ressources/images/characters/player/run4.png"),
                pg.image.load("ressources/images/characters/player/run5.png"),]
    
    jump_ani = [pg.image.load("ressources/images/characters/player/saut1.png"), pg.image.load("ressources/images/characters/player/saut2.png")]

    slide_ani = [pg.image.load("ressources/images/characters/player/slide1.png"), pg.image.load("ressources/images/characters/player/slide2.png")]

    jump_sound = pg.mixer.Sound("ressources/sounds/jump.mp3")
    slide_sound = pg.mixer.Sound("ressources/sounds/slide.mp3")
    running_sound = pg.mixer.Sound("ressources/sounds/running.mp3")

    def __init__(self):
        super().__init__()
        self.image = Player.run_ani[0]
        self.rect = self.image.get_rect()

        # Position
        self.pos = pg.math.Vector2((200, 600))
        self.vel_y = 0
        self.acc_y = 0.06

        self.frame = 0
        self.jumping = False
        self.sliding = False
        self.slide_timer = 0  # Initialisation du compteur de glissade
        self.move_frame = 0

        self.channel = pg.mixer.Channel(0)
        self.channel.play(Player.running_sound , -1)

        self.particles = pg.sprite.RenderUpdates()

    def _update(self,dt, hits):
        # Contrôle de la durée de la glissade
        if self.sliding:
            # Compteur pour la durée de la glissade
            self.slide_timer += dt
            if self.slide_timer >= 700:  # Réduisez ce nombre selon la durée de la glissade souhaitée
                # Rétablir la hauteur normale du personnage
                self.sliding = False
                self.slide_timer = 0

        # Mise à jour de l'animation
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

        # Son de course
        if self.channel.get_sound() != Player.running_sound and not self.jumping and not self.sliding:
            self.channel.play(Player.running_sound , -1)

        # Création des particules
        if not self.jumping and not self.sliding:
            for _ in range(2):
                self.particles.add(Particle((self.pos.x + self.rect.width/2 - 5, self.pos.y)))
        elif not self.jumping:
            for _ in range(5):
                self.particles.add(Particle((self.pos.x + self.rect.width/2 - 5, self.pos.y)))

        # Mise à jour et dessin des particules
        self.particles.update()
        # Suppression des particules en fin de vie
        self.particles.remove([particle for particle in self.particles if particle.lifespan <= 0])

        self.move(dt, hits)

    def move(self,dt, hits):
        # Application de la gravité
        self.vel_y += self.acc_y
        vel_max = 15
        self.pos.y += min(self.vel_y * dt, vel_max) # Updates Position with new values
            
        # Vérification de la colision avec le sol
        self.ground_colision(hits)

        # Mise à jour de la position
        self.rect.midbottom = self.pos

    def ground_colision(self, hits):
      if self.vel_y > 0:
        
        # On enlève les objets sur lesquels on ne peut pas marcher
        i = 0
        while i < len(hits) and isinstance(hits[i], (Bonus, Malus, Spike)):
            i += 1
        if i < len(hits) :

            lowest = hits[i]
            if isinstance(lowest, Chair):
                if self.rect.bottom > lowest.rect.top - 2 + 28 and self.rect.bottom < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1 + 28
                    self.vel_y = 0
                    self.jumping = False
            else:
                if self.rect.bottom > lowest.rect.top - 2 and self.rect.bottom < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel_y = 0
                    self.jumping = False



    def jump(self, hits):
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.channel.play(Player.jump_sound)
            self.jumping = True
            self.move_frame = 0
            self.vel_y = -0.75
    
    def slide(self):
        if not self.sliding:
            self.channel.play(Player.slide_sound)
            self.sliding = True
            self.move_frame = 0